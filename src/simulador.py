# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: simulador.py
#
# Objetivo:
#   Centralizar toda a lógica de simulação do sistema, permitindo ao usuário
#   escolher entre simulação determinística e simulação por eventos discretos (DES).
#   Gera estatísticas detalhadas, integra exportação automática de PDF e,
#   se fornecido o layout, gera imagens e animação GIF minuto a minuto do restaurante.
#
# Importante:
#   A simulação é limitada pelo parâmetro 'tempo_total_simulacao' (em minutos),
#   que define o tempo máximo de funcionamento do restaurante. Nenhum evento
#   é processado após esse tempo, garantindo que todos os resultados, estatísticas
#   e visualizações respeitem o período real de operação definido pelo usuário.
#   A lista de ocupação das mesas para visualização é alimentada apenas uma vez por minuto,
#   garantindo que o número de frames do GIF seja compatível com o tempo simulado.
#
# Funções principais:
#   - rodar_simulacao: executa a simulação conforme o método escolhido.
#   - simular_eventos_discretos: simulação DES com visualização.
#   - simular_deterministico: simulação baseada em médias fixas.
#
# Autor: Christian Mulato
# Data: 28/05/2025
# ===============================================

import traceback
import heapq
import os
import random
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from src.logger_config import get_logger

logger = get_logger()

class Evento:
    def __init__(self, tempo, tipo, cliente_id=None):
        self.tempo = tempo
        self.tipo = tipo  # Ex: 'chegada', 'buffet', 'balcao', 'pesagem', 'caixa', 'pagamento', 'procura_mesa', 'saida'
        self.cliente_id = cliente_id

    def __lt__(self, other):
        return self.tempo < other.tempo

def _amostrar_tempo(media, variabilidade_frac):
    """
    Amostra um tempo positivo a partir de uma média e uma variabilidade fracionária.
    Ex.: variabilidade_frac=0.15 → desvio-padrão = 0.15 * media.
    """
    try:
        v = float(variabilidade_frac or 0)
    except Exception:
        v = 0.0
    if v <= 0:
        return float(media)
    mu = float(media)
    sigma = abs(mu) * v
    amostra = random.gauss(mu, sigma)
    return max(0.1, float(amostra))


def _as_int(v: Any, default: int) -> int:
    try:
        return int(v)
    except Exception:
        return default


def _as_float(v: Any, default: float) -> float:
    try:
        return float(v)
    except Exception:
        return default


def _clamp_positive(v: float, default: float, min_value: float = 0.0) -> float:
    try:
        vf = float(v)
        if vf < min_value:
            return default
        return vf
    except Exception:
        return default


def _normalizar_parametros(parametros: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normaliza e valida parâmetros para evitar inconsistências silenciosas.

    Regras principais:
    - `tempo_total_simulacao` é limitado a 720 (12h) por segurança operacional.
    - Se `tempo_entre_clientes` não for fornecido, é derivado de `clientes_por_minuto`.
    - Tempos médios e capacidades são forçados a valores físicos (>= 0), com defaults.

    Esta função NÃO depende de interface (Tkinter), permitindo testes unitários do núcleo.
    """
    p = dict(parametros or {})

    p["tempo_total_simulacao"] = _as_int(p.get("tempo_total_simulacao", 120), 120)
    if p["tempo_total_simulacao"] > 720:
        logger.warning("tempo_total_simulacao maior que 720 minutos. Ajustando para 720.")
        p["tempo_total_simulacao"] = 720
    if p["tempo_total_simulacao"] < 0:
        raise ValueError("tempo_total_simulacao deve ser >= 0.")

    p["clientes_por_minuto"] = _as_float(p.get("clientes_por_minuto", 10), 10.0)
    if p["clientes_por_minuto"] < 0:
        raise ValueError("clientes_por_minuto deve ser >= 0.")

    # Se tempo_entre_clientes vier inconsistente, mantemos o valor explícito (assumido como calibração),
    # mas garantimos que seja positivo. Caso não exista, derivamos do feed rate.
    tec = p.get("tempo_entre_clientes", None)
    if tec is None:
        cpm = _clamp_positive(p["clientes_por_minuto"], default=10.0, min_value=0.0)
        p["tempo_entre_clientes"] = 1.0 / max(cpm, 0.0001)
    else:
        p["tempo_entre_clientes"] = _clamp_positive(tec, default=1.0, min_value=0.0001)

    # Capacidades físicas e tempos médios
    p["numero_de_mesas"] = _as_int(p.get("numero_de_mesas", 10), 10)
    p["cadeiras_por_mesa"] = _as_int(p.get("cadeiras_por_mesa", 4), 4)
    if p["numero_de_mesas"] < 0 or p["cadeiras_por_mesa"] < 0:
        raise ValueError("numero_de_mesas e cadeiras_por_mesa devem ser >= 0.")

    p["numero_caixas"] = _as_int(p.get("numero_caixas", 1), 1)
    if p["numero_caixas"] < 1:
        logger.warning("numero_caixas < 1. Ajustando para 1.")
        p["numero_caixas"] = 1

    p["numero_buffets"] = _as_int(p.get("numero_buffets", 1), 1)
    if p["numero_buffets"] < 1:
        p["numero_buffets"] = 1

    p["tempo_medio_almoco"] = _clamp_positive(p.get("tempo_medio_almoco", 30), default=30.0, min_value=0.0)
    p["tempo_buffet"] = _clamp_positive(p.get("tempo_buffet", 2), default=2.0, min_value=0.0)
    p["tempo_balcao"] = _clamp_positive(p.get("tempo_balcao", 1), default=1.0, min_value=0.0)
    p["tempo_medio_atendimento"] = _clamp_positive(p.get("tempo_medio_atendimento", 2), default=2.0, min_value=0.0)

    p["variabilidade_chegada"] = _clamp_positive(p.get("variabilidade_chegada", 0), default=0.0, min_value=0.0)
    p["variabilidade_almoco"] = _clamp_positive(p.get("variabilidade_almoco", 0), default=0.0, min_value=0.0)

    # Limites de fila / abandono (edge cases)
    # capacidade_maxima_fila: limite de buffer para fila de mesas (saturação física de espera)
    p["capacidade_maxima_fila"] = _as_int(p.get("capacidade_maxima_fila", 0), 0)
    if p["capacidade_maxima_fila"] < 0:
        p["capacidade_maxima_fila"] = 0

    # tempo_max_espera_fila: se definido, cliente abandona após esse tempo esperando mesa
    tmax = p.get("tempo_max_espera_fila", None)
    if tmax is None or tmax == "":
        p["tempo_max_espera_fila"] = None
    else:
        p["tempo_max_espera_fila"] = _clamp_positive(tmax, default=0.0, min_value=0.0)

    # Modo de pós-fechamento: por padrão, respeita janela operacional (não processa após tempo_total_simulacao).
    p["processar_pos_fechamento"] = bool(p.get("processar_pos_fechamento", False))

    return p


@dataclass
class _EstacaoStats:
    """
    Estatísticas operacionais de uma estação (operação unitária).

    Analogia de operações unitárias:
    - A fila atua como um "buffer" (inventário intermediário / holdup).
    - O serviço atua como uma taxa de processamento (capacidade μ) com variabilidade.
    """

    nome: str
    capacidade_servidores: int
    total_processados: int = 0
    tempo_total_espera: float = 0.0
    tempo_total_servico: float = 0.0
    fila_max: int = 0

    def registrar_espera(self, espera: float) -> None:
        self.tempo_total_espera += max(0.0, float(espera))

    def registrar_servico(self, duracao: float) -> None:
        self.tempo_total_servico += max(0.0, float(duracao))
        self.total_processados += 1

    def registrar_fila(self, tamanho: int) -> None:
        self.fila_max = max(self.fila_max, int(tamanho))

    def kpis(self, tempo_janela: float) -> Dict[str, Any]:
        cap = max(1, int(self.capacidade_servidores))
        janela = max(0.0001, float(tempo_janela))
        utilizacao = (self.tempo_total_servico / (cap * janela)) * 100.0
        return {
            "capacidade_servidores": cap,
            "processados": self.total_processados,
            "tempo_medio_espera": (self.tempo_total_espera / self.total_processados) if self.total_processados else 0.0,
            "tempo_medio_servico": (self.tempo_total_servico / self.total_processados) if self.total_processados else 0.0,
            "fila_max": self.fila_max,
            "utilizacao_percent": utilizacao,
        }


def simular_eventos_discretos(parametros, layout=None, coletar_series=False):
    """
    Simulação baseada em eventos discretos (DES) com coleta de estatísticas para relatório.
    Também gera imagens do layout e um GIF animado minuto a minuto, se layout for fornecido.

    Interpretação em termos de Engenharia de Processos (analogia de Operações Unitárias):
    - **Chegada**: alimentação (feed) com taxa lambda (λ) e variabilidade (ruído estocástico).
    - **Buffet / Balança / Caixa**: operações unitárias discretas com capacidade finita (n servidores) e tempo de serviço (μ).
      Cada estação atua como um "reator/serviço" que processa entidades e forma **buffers** (filas) quando a alimentação supera μ.
    - **Mesas/Cadeiras**: volume de residência (holdup) — restrição física de capacidade do sistema.

    Rigor de confiabilidade (Mass Balance):
    Ao final, sempre retornamos um balanço conservativo:
      Entradas = Saídas atendidas + Saídas por rejeição + No sistema (ainda não concluídos na janela).
    """
    p = _normalizar_parametros(parametros)

    tempo_atual = 0.0
    agenda: List[Evento] = []
    heapq.heapify(agenda)
    eventos_processados = 0

    tempo_total_simulacao = float(p["tempo_total_simulacao"])
    janela_operacional = tempo_total_simulacao
    processar_pos_fechamento = bool(p.get("processar_pos_fechamento", False))

    # ------------------------------
    # Rastreamento por cliente (conservação e tempos por etapa)
    # ------------------------------
    tempos_chegada: Dict[int, float] = {}
    tempos_saida: Dict[int, float] = {}
    tempos_rejeicao: Dict[int, float] = {}
    status: Dict[int, str] = {}  # estados: buffet_q, buffet_s, balcao_q, balcao_s, caixa_q, caixa_s, fila_mesa, mesa, saiu, rejeitado

    # Traços por etapa (espera + serviço), usados para auditoria e KPIs
    trace: Dict[int, Dict[str, float]] = {}

    def _trace(cid: int) -> Dict[str, float]:
        if cid not in trace:
            trace[cid] = {}
        return trace[cid]

    # ------------------------------
    # Estações (operações unitárias)
    # ------------------------------
    est_buffet = _EstacaoStats("buffet", capacidade_servidores=int(p["numero_buffets"]))
    est_balcao = _EstacaoStats("balcao", capacidade_servidores=1)
    est_caixa = _EstacaoStats("caixa", capacidade_servidores=int(p["numero_caixas"]))

    fila_buffet: List[Tuple[int, float]] = []
    fila_balcao: List[Tuple[int, float]] = []
    fila_caixa: List[Tuple[int, float]] = []
    buffet_ocupados = 0
    balcao_ocupados = 0
    caixa_ocupados = 0

    variabilidade_chegada = float(p.get("variabilidade_chegada", 0.0) or 0.0)
    variabilidade_almoco = float(p.get("variabilidade_almoco", 0.0) or 0.0)

    def _tentar_iniciar_buffet(agora: float) -> None:
        nonlocal buffet_ocupados
        while buffet_ocupados < est_buffet.capacidade_servidores and fila_buffet:
            cid, t_q = fila_buffet.pop(0)
            if status.get(cid) != "buffet_q":
                continue
            buffet_ocupados += 1
            status[cid] = "buffet_s"
            _trace(cid)["buffet_start"] = agora
            est_buffet.registrar_espera(agora - t_q)
            tempo_serv = _amostrar_tempo(p.get("tempo_buffet", 2), variabilidade_chegada)
            heapq.heappush(agenda, Evento(agora + tempo_serv, "buffet_fim", cliente_id=cid))
            est_buffet.registrar_fila(len(fila_buffet))

    def _tentar_iniciar_balcao(agora: float) -> None:
        nonlocal balcao_ocupados
        while balcao_ocupados < est_balcao.capacidade_servidores and fila_balcao:
            cid, t_q = fila_balcao.pop(0)
            if status.get(cid) != "balcao_q":
                continue
            balcao_ocupados += 1
            status[cid] = "balcao_s"
            _trace(cid)["balcao_start"] = agora
            est_balcao.registrar_espera(agora - t_q)
            tempo_serv = _amostrar_tempo(p.get("tempo_balcao", 1), variabilidade_chegada)
            heapq.heappush(agenda, Evento(agora + tempo_serv, "balcao_fim", cliente_id=cid))
            est_balcao.registrar_fila(len(fila_balcao))

    def _tentar_iniciar_caixa(agora: float) -> None:
        nonlocal caixa_ocupados
        while caixa_ocupados < est_caixa.capacidade_servidores and fila_caixa:
            cid, t_q = fila_caixa.pop(0)
            if status.get(cid) != "caixa_q":
                continue
            caixa_ocupados += 1
            status[cid] = "caixa_s"
            _trace(cid)["caixa_start"] = agora
            est_caixa.registrar_espera(agora - t_q)
            tempo_serv = _amostrar_tempo(p.get("tempo_medio_atendimento", 2), variabilidade_chegada)
            heapq.heappush(agenda, Evento(agora + tempo_serv, "caixa_fim", cliente_id=cid))
            est_caixa.registrar_fila(len(fila_caixa))

    # ------------------------------
    # Mesas/cadeiras (residência física) + fila de mesa (buffer)
    # ------------------------------
    numero_de_mesas = int(p["numero_de_mesas"])
    cadeiras_por_mesa = int(p["cadeiras_por_mesa"])
    capacidade_cadeiras = max(0, numero_de_mesas * cadeiras_por_mesa)

    # Modelamos cadeiras como slots individuais para respeitar saturação física.
    # chair_slots[i] = (cliente_id, tempo_saida) ou None
    chair_slots: List[Optional[Tuple[int, float]]] = [None for _ in range(capacidade_cadeiras)]
    cliente_assento: Dict[int, int] = {}
    fila_mesa: List[Tuple[int, float]] = []  # (cliente_id, t_entrada_fila)
    tamanho_max_fila_mesa = 0
    tempo_total_espera_fila_mesa = 0.0
    clientes_que_esperaram_mesa = 0

    # Ocupação integrada (cadeiras) para KPI físico (taxa de ocupação)
    ocupacao_cadeiras = 0.0
    ocupacao_mesas_integral = 0.0
    ultimo_tempo = 0.0

    # Visualização minuto a minuto (continua reportando "mesas ocupadas" para compatibilidade)
    layout_base = layout if layout and isinstance(layout, list) else None
    lista_mesas_ocupadas_por_tempo: List[List[int]] = [[] for _ in range(int(tempo_total_simulacao) + 1)]

    # Séries temporais (para scripts/figuras)
    series = None
    residence_times: List[float] = []
    if coletar_series:
        series = {
            "minutos": list(range(int(tempo_total_simulacao) + 1)),
            "mesas_ocupadas": [0 for _ in range(int(tempo_total_simulacao) + 1)],  # mesas com >=1 cadeira ocupada
            "fila_mesa": [0 for _ in range(int(tempo_total_simulacao) + 1)],
            "fila_buffet": [0 for _ in range(int(tempo_total_simulacao) + 1)],
            "fila_balcao": [0 for _ in range(int(tempo_total_simulacao) + 1)],
            "fila_caixa": [0 for _ in range(int(tempo_total_simulacao) + 1)],
            "saidas_por_minuto": [0 for _ in range(int(tempo_total_simulacao) + 1)],
        }

    tempo_max_espera_fila = p.get("tempo_max_espera_fila", None)
    capacidade_maxima_fila = int(p.get("capacidade_maxima_fila", 0) or 0)

    def _mesas_ocupadas_indices() -> List[int]:
        if numero_de_mesas <= 0 or cadeiras_por_mesa <= 0:
            return []
        ocupadas: List[int] = []
        for m in range(numero_de_mesas):
            ini = m * cadeiras_por_mesa
            fim = ini + cadeiras_por_mesa
            if any(chair_slots[i] is not None for i in range(ini, min(fim, len(chair_slots)))):
                ocupadas.append(m)
        return ocupadas

    def _cadeiras_ocupadas_qtd() -> int:
        return sum(1 for s in chair_slots if s is not None)

    def _tentar_alocar_cadeira(cid: int, agora: float) -> bool:
        """
        Tenta alocar 1 cadeira para o cliente. Retorna True se alocado.

        Analogia físico-química: esta função impõe uma restrição de capacidade
        do "volume de residência" (holdup) — se o volume está cheio, a entidade
        acumula no buffer (fila) ou é rejeitada (overflow).
        """
        for idx, slot in enumerate(chair_slots):
            if slot is None:
                tempo_refeicao = _amostrar_tempo(p["tempo_medio_almoco"], variabilidade_almoco)
                t_saida = agora + tempo_refeicao
                chair_slots[idx] = (cid, t_saida)
                cliente_assento[cid] = idx
                status[cid] = "mesa"
                _trace(cid)["mesa_start"] = agora
                heapq.heappush(agenda, Evento(t_saida, "saida", cliente_id=cid))
                return True
        return False

    def _enfileirar_mesa(cid: int, agora: float) -> None:
        nonlocal tamanho_max_fila_mesa
        if capacidade_maxima_fila and len(fila_mesa) >= capacidade_maxima_fila:
            # Saturação do buffer: rejeição controlada (contabiliza saída por rejeição)
            status[cid] = "rejeitado"
            tempos_rejeicao[cid] = agora
            _trace(cid)["rejeicao"] = agora
            return

        fila_mesa.append((cid, agora))
        status[cid] = "fila_mesa"
        _trace(cid)["mesa_fila_entrada"] = agora
        tamanho_max_fila_mesa = max(tamanho_max_fila_mesa, len(fila_mesa))

        # Se existir regra de abandono, agenda verificação futura (evento não cancela; apenas valida estado na hora).
        if tempo_max_espera_fila is not None:
            try:
                t_abandono = agora + float(tempo_max_espera_fila)
                heapq.heappush(agenda, Evento(t_abandono, "abandono_fila_mesa", cliente_id=cid))
            except Exception:
                pass

    def _tentar_atender_fila_mesa(agora: float) -> None:
        nonlocal tempo_total_espera_fila_mesa, clientes_que_esperaram_mesa
        # Enquanto houver cadeira livre e fila não vazia
        while fila_mesa and any(s is None for s in chair_slots):
            cid, t_entrada = fila_mesa.pop(0)
            if status.get(cid) != "fila_mesa":
                continue
            espera = agora - t_entrada
            tempo_total_espera_fila_mesa += max(0.0, espera)
            clientes_que_esperaram_mesa += 1
            _trace(cid)["mesa_fila_saida"] = agora
            _trace(cid)["mesa_espera"] = max(0.0, espera)
            ok = _tentar_alocar_cadeira(cid, agora)
            if not ok:
                # Se falhar (condição de corrida), recoloca no início e sai
                fila_mesa.insert(0, (cid, t_entrada))
                status[cid] = "fila_mesa"
                break

    # ------------------------------
    # Chegadas (feed) — agenda até o fim da janela operacional
    # ------------------------------
    def _agendar_proxima_chegada(cid_atual: int, agora: float) -> None:
        dt = _amostrar_tempo(p.get("tempo_entre_clientes", 1.0), variabilidade_chegada)
        prox = agora + dt
        if prox <= tempo_total_simulacao:
            heapq.heappush(agenda, Evento(prox, "chegada", cliente_id=cid_atual + 1))

    heapq.heappush(agenda, Evento(0.0, "chegada", cliente_id=1))

    # ------------------------------
    # Execução da agenda de eventos
    # ------------------------------
    while agenda:
        evento = heapq.heappop(agenda)

        # Respeita a janela operacional por padrão (não processa eventos após o fechamento).
        if (not processar_pos_fechamento) and evento.tempo > tempo_total_simulacao:
            logger.info(
                f"Evento no tempo {evento.tempo} ignorado (limite tempo_total_simulacao = {tempo_total_simulacao})."
            )
            break

        # Atualiza ocupação integrada de cadeiras e séries por minuto
        start_min = int(ultimo_tempo)
        end_min = int(min(evento.tempo, tempo_total_simulacao))
        if start_min < 0:
            start_min = 0
        if end_min < 0:
            end_min = 0
        if end_min > int(tempo_total_simulacao):
            end_min = int(tempo_total_simulacao)

        if layout_base or coletar_series:
            for minuto in range(start_min, end_min + 1):
                mesas_ocupadas_pos = _mesas_ocupadas_indices()
                if layout_base and 0 <= minuto < len(lista_mesas_ocupadas_por_tempo):
                    lista_mesas_ocupadas_por_tempo[minuto] = list(mesas_ocupadas_pos)
                if coletar_series and series and 0 <= minuto < len(series["mesas_ocupadas"]):
                    series["mesas_ocupadas"][minuto] = len(mesas_ocupadas_pos)
                    series["fila_mesa"][minuto] = len(fila_mesa)
                    series["fila_buffet"][minuto] = len(fila_buffet)
                    series["fila_balcao"][minuto] = len(fila_balcao)
                    series["fila_caixa"][minuto] = len(fila_caixa)

        delta = float(evento.tempo) - float(ultimo_tempo)
        if delta > 0:
            ocupacao_cadeiras += _cadeiras_ocupadas_qtd() * delta
            ocupacao_mesas_integral += len(_mesas_ocupadas_indices()) * delta
        ultimo_tempo = float(evento.tempo)

        tempo_atual = float(evento.tempo)
        eventos_processados += 1

        # ------------------------------
        # Processamento do evento
        # ------------------------------
        if evento.tipo == "chegada":
            cid = int(evento.cliente_id)
            tempos_chegada[cid] = tempo_atual
            status[cid] = "buffet_q"
            _trace(cid)["chegada"] = tempo_atual
            _trace(cid)["buffet_fila_entrada"] = tempo_atual

            _agendar_proxima_chegada(cid, tempo_atual)

            fila_buffet.append((cid, tempo_atual))
            est_buffet.registrar_fila(len(fila_buffet))
            _tentar_iniciar_buffet(tempo_atual)

        elif evento.tipo == "buffet_fim":
            cid = int(evento.cliente_id)
            if status.get(cid) != "buffet_s":
                continue
            buffet_ocupados = max(0, buffet_ocupados - 1)
            _trace(cid)["buffet_end"] = tempo_atual
            # duração de serviço (buffet)
            try:
                est_buffet.registrar_servico(tempo_atual - _trace(cid).get("buffet_start", tempo_atual))
            except Exception:
                est_buffet.registrar_servico(0.0)

            # Roteia para balcao
            status[cid] = "balcao_q"
            _trace(cid)["balcao_fila_entrada"] = tempo_atual
            fila_balcao.append((cid, tempo_atual))
            est_balcao.registrar_fila(len(fila_balcao))
            _tentar_iniciar_balcao(tempo_atual)
            _tentar_iniciar_buffet(tempo_atual)

        elif evento.tipo == "balcao_fim":
            cid = int(evento.cliente_id)
            if status.get(cid) != "balcao_s":
                continue
            balcao_ocupados = max(0, balcao_ocupados - 1)
            _trace(cid)["balcao_end"] = tempo_atual
            try:
                est_balcao.registrar_servico(tempo_atual - _trace(cid).get("balcao_start", tempo_atual))
            except Exception:
                est_balcao.registrar_servico(0.0)

            # Roteia para caixa
            status[cid] = "caixa_q"
            _trace(cid)["caixa_fila_entrada"] = tempo_atual
            fila_caixa.append((cid, tempo_atual))
            est_caixa.registrar_fila(len(fila_caixa))
            _tentar_iniciar_caixa(tempo_atual)
            _tentar_iniciar_balcao(tempo_atual)

        elif evento.tipo == "caixa_fim":
            cid = int(evento.cliente_id)
            if status.get(cid) != "caixa_s":
                continue
            caixa_ocupados = max(0, caixa_ocupados - 1)
            _trace(cid)["caixa_end"] = tempo_atual
            try:
                est_caixa.registrar_servico(tempo_atual - _trace(cid).get("caixa_start", tempo_atual))
            except Exception:
                est_caixa.registrar_servico(0.0)

            # Procura mesa (tenta alocar; se não, vai para fila)
            if not _tentar_alocar_cadeira(cid, tempo_atual):
                _enfileirar_mesa(cid, tempo_atual)
            _tentar_iniciar_caixa(tempo_atual)

        elif evento.tipo == "abandono_fila_mesa":
            cid = int(evento.cliente_id)
            if status.get(cid) != "fila_mesa":
                continue
            # Remove da fila (best-effort)
            for i, (c, t_ent) in enumerate(list(fila_mesa)):
                if c == cid:
                    fila_mesa.pop(i)
                    break
            status[cid] = "rejeitado"
            tempos_rejeicao[cid] = tempo_atual
            _trace(cid)["rejeicao"] = tempo_atual

        elif evento.tipo == "saida":
            cid = int(evento.cliente_id)
            if status.get(cid) != "mesa":
                continue
            tempos_saida[cid] = tempo_atual
            status[cid] = "saiu"
            _trace(cid)["saida"] = tempo_atual

            # Libera cadeira
            idx = cliente_assento.get(cid, None)
            if idx is not None and 0 <= idx < len(chair_slots):
                chair_slots[idx] = None
            cliente_assento.pop(cid, None)

            if coletar_series and series:
                m = int(tempo_atual)
                if 0 <= m <= int(tempo_total_simulacao):
                    series["saidas_por_minuto"][m] += 1

            # Atende fila de mesas se possível
            _tentar_atender_fila_mesa(tempo_atual)

        # keep queues served as time progresses

    # Preenche séries/visualização até o fim da janela operacional
    if layout_base or coletar_series:
        for minuto in range(int(ultimo_tempo), int(tempo_total_simulacao) + 1):
            mesas_ocupadas_pos = _mesas_ocupadas_indices()
            if layout_base and 0 <= minuto < len(lista_mesas_ocupadas_por_tempo):
                lista_mesas_ocupadas_por_tempo[minuto] = list(mesas_ocupadas_pos)
            if coletar_series and series and 0 <= minuto < len(series["mesas_ocupadas"]):
                series["mesas_ocupadas"][minuto] = len(mesas_ocupadas_pos)
                series["fila_mesa"][minuto] = len(fila_mesa)
                series["fila_buffet"][minuto] = len(fila_buffet)
                series["fila_balcao"][minuto] = len(fila_balcao)
                series["fila_caixa"][minuto] = len(fila_caixa)

    # Atualiza ocupação integrada até o fim da janela (apenas se não processamos até além do fechamento)
    if not processar_pos_fechamento:
        delta = float(tempo_total_simulacao) - float(ultimo_tempo)
        if delta > 0:
            ocupacao_cadeiras += _cadeiras_ocupadas_qtd() * delta
            ocupacao_mesas_integral += len(_mesas_ocupadas_indices()) * delta

    # ------------------------------
    # Estatísticas finais e Mass Balance Check
    # ------------------------------
    clientes_entraram = len(tempos_chegada)
    clientes_sairam = len(tempos_saida)
    clientes_rejeitados = len(tempos_rejeicao)
    clientes_em_sistema = max(0, clientes_entraram - clientes_sairam - clientes_rejeitados)

    # Tempos de residência (do feed à saída), apenas para quem saiu dentro da janela processada
    tempo_total_permanencia = 0.0
    tempo_total_refeicao = 0.0
    refeicoes_medidas = 0
    for cid, t_in in tempos_chegada.items():
        t_out = tempos_saida.get(cid)
        if t_out is None:
            continue
        dt = t_out - t_in
        tempo_total_permanencia += dt
        t_mesa_start = trace.get(cid, {}).get("mesa_start")
        if t_mesa_start is not None:
            tempo_total_refeicao += (t_out - float(t_mesa_start))
            refeicoes_medidas += 1
        if coletar_series:
            residence_times.append(dt)

    clientes_processados = clientes_sairam

    uso_medio_cadeiras = (
        (ocupacao_cadeiras / (capacidade_cadeiras * max(tempo_total_simulacao, 0.0001))) * 100.0
        if capacidade_cadeiras > 0 and tempo_total_simulacao > 0
        else 0.0
    )
    uso_medio_mesas_percent = (
        (ocupacao_mesas_integral / (max(1, numero_de_mesas) * max(tempo_total_simulacao, 0.0001))) * 100.0
        if numero_de_mesas > 0 and tempo_total_simulacao > 0
        else 0.0
    )

    # Bottleneck analysis: maior utilização (preferencial) e também maior espera média
    kpi_buffet = est_buffet.kpis(janela_operacional)
    kpi_balcao = est_balcao.kpis(janela_operacional)
    kpi_caixa = est_caixa.kpis(janela_operacional)
    estacoes_kpis = {"buffet": kpi_buffet, "balcao": kpi_balcao, "caixa": kpi_caixa}

    bottleneck_por_util = max(estacoes_kpis.items(), key=lambda kv: float(kv[1].get("utilizacao_percent", 0.0)))[0]
    bottleneck_por_espera = max(estacoes_kpis.items(), key=lambda kv: float(kv[1].get("tempo_medio_espera", 0.0)))[0]
    bottleneck = bottleneck_por_util

    mass_balance_ok = (clientes_entraram == (clientes_sairam + clientes_rejeitados + clientes_em_sistema))

    resultado_des: Dict[str, Any] = {
        "eventos_processados": eventos_processados,
        "clientes_simulados": clientes_entraram,
        "clientes_processados": clientes_processados,
        "clientes_nao_atendidos": clientes_rejeitados,  # compatibilidade: rejeição/abandono = não atendidos
        "clientes_em_sistema": clientes_em_sistema,
        "tempo_total_simulacao_min": int(p["tempo_total_simulacao"]),
        "tempo_medio_permanencia_cliente": round((tempo_total_permanencia / clientes_processados), 2) if clientes_processados else 0,
        "clientes_que_esperaram_mesa": clientes_que_esperaram_mesa,
        "tempo_medio_espera_fila_mesa": round((tempo_total_espera_fila_mesa / clientes_que_esperaram_mesa), 2) if clientes_que_esperaram_mesa else 0,
        "tamanho_max_fila_mesa": tamanho_max_fila_mesa,
        "uso_medio_mesas": round(uso_medio_cadeiras, 1),  # compatibilidade: agora é ocupação de cadeiras (mais físico)
        "uso_medio_mesas_percent": round(uso_medio_mesas_percent, 1),
        "uso_medio_cadeiras_percent": round(uso_medio_cadeiras, 1),
        "kpis": {
            "ocupacao_cadeiras_percent": round(uso_medio_cadeiras, 2),
            "ocupacao_mesas_percent": round(uso_medio_mesas_percent, 2),
            "tempo_medio_ciclo_min": round((tempo_total_permanencia / clientes_processados), 3) if clientes_processados else 0.0,
            "tempo_medio_refeicao_min": round((tempo_total_refeicao / refeicoes_medidas), 3) if refeicoes_medidas else 0.0,
            "bottleneck": {
                "por_utilizacao": bottleneck_por_util,
                "por_espera_media": bottleneck_por_espera,
                "principal": bottleneck,
            },
        },
        "tempos_etapas": {
            "fila_mesa_tempo_medio": round((tempo_total_espera_fila_mesa / clientes_que_esperaram_mesa), 3) if clientes_que_esperaram_mesa else 0.0,
            "buffet": {"espera_media": round(float(kpi_buffet.get("tempo_medio_espera", 0.0)), 3), "servico_medio": round(float(kpi_buffet.get("tempo_medio_servico", 0.0)), 3)},
            "balcao": {"espera_media": round(float(kpi_balcao.get("tempo_medio_espera", 0.0)), 3), "servico_medio": round(float(kpi_balcao.get("tempo_medio_servico", 0.0)), 3)},
            "caixa": {"espera_media": round(float(kpi_caixa.get("tempo_medio_espera", 0.0)), 3), "servico_medio": round(float(kpi_caixa.get("tempo_medio_servico", 0.0)), 3)},
        },
        "estacoes": estacoes_kpis,
        "mass_balance": {
            "entraram": clientes_entraram,
            "sairam": clientes_sairam,
            "rejeitados": clientes_rejeitados,
            "no_sistema": clientes_em_sistema,
            "ok": mass_balance_ok,
        },
    }
    resultado_des.update(p)

    if coletar_series and series:
        resultado_des["series"] = series
        resultado_des["residence_times"] = residence_times

    # Gera animação se layout foi fornecido (best-effort; evita importar pesado em testes)
    if layout_base and lista_mesas_ocupadas_por_tempo:
        try:
            from src.visualizador_layout import gerar_animacao

            caminho_gif = gerar_animacao(layout_base, lista_mesas_ocupadas_por_tempo)
            resultado_des["gif_layout"] = caminho_gif
            logger.info(f"GIF animado do layout gerado em: {caminho_gif}")
        except Exception as e:
            logger.error(f"Erro ao gerar GIF animado do layout: {e}")

    return resultado_des

def simular_deterministico(parametros, layout=None):
    """
    Simulação determinística simples.
    """
    clientes_por_minuto = parametros['clientes_por_minuto']
    tempo_almoco = parametros['tempo_medio_almoco']
    cadeiras_por_mesa = parametros['cadeiras_por_mesa']
    numero_de_mesas = parametros['numero_de_mesas']

    tempo_medio_atendimento = parametros.get('tempo_medio_atendimento', 0)
    tempo_medio_espera = parametros.get('tempo_medio_espera', 0)
    tempo_total_simulacao = parametros.get('tempo_total_simulacao', 120)
    variabilidade_almoco = parametros.get('variabilidade_almoco', 0)
    variabilidade_chegada = parametros.get('variabilidade_chegada', 0)
    capacidade_maxima_fila = parametros.get('capacidade_maxima_fila', 0)
    modo_ocupacao = parametros.get('modo_ocupacao', 'padrao')
    numero_caixas = parametros.get('numero_caixas', 1)
    tempo_entre_clientes = parametros.get('tempo_entre_clientes', 0)

    total_clientes = int(clientes_por_minuto * tempo_total_simulacao)
    capacidade_total = cadeiras_por_mesa * numero_de_mesas
    mesas_ocupadas = min(numero_de_mesas, total_clientes // cadeiras_por_mesa)
    tempo_total_gasto = total_clientes * tempo_almoco
    uso_medio_mesas = mesas_ocupadas / numero_de_mesas if numero_de_mesas > 0 else 0

    resultado = {
        'clientes_por_minuto': clientes_por_minuto,
        'tempo_total_simulacao_min': tempo_total_simulacao,
        'total_clientes': total_clientes,
        'tempo_medio_almoco_min': tempo_almoco,
        'capacidade_total': capacidade_total,
        'numero_de_mesas': numero_de_mesas,
        'cadeiras_por_mesa': cadeiras_por_mesa,
        'mesas_ocupadas': mesas_ocupadas,
        'uso_medio_mesas': round(uso_medio_mesas, 2),
        'tempo_total_gasto_cliente_min': tempo_total_gasto,
        'tempo_medio_atendimento': tempo_medio_atendimento,
        'tempo_medio_espera': tempo_medio_espera,
        'variabilidade_almoco': variabilidade_almoco,
        'variabilidade_chegada': variabilidade_chegada,
        'capacidade_maxima_fila': capacidade_maxima_fila,
        'modo_ocupacao': modo_ocupacao,
        'numero_caixas': numero_caixas,
        'tempo_entre_clientes': tempo_entre_clientes
    }
    resultado.update(parametros)
    return resultado

def rodar_simulacao(parametros, layout=None, exportar_pdf_automatico=False, caminho_pdf="resultados/relatorios/resultado_simulacao.pdf", usar_des=True):
    """
    Executa a simulação de tempo de permanência no restaurante.

    Parâmetros:
        parametros (dict): contém os valores de entrada da simulação
        layout (opcional): estrutura de layout ASCII
        exportar_pdf_automatico (bool): se True, gera PDF automaticamente
        caminho_pdf (str): caminho para salvar o PDF (usado se exportar_pdf_automatico=True)
        usar_des (bool): se True, executa simulação DES; se False, determinística

    Retorna:
        dict com os resultados da simulação
    """
    try:
        # Normaliza para evitar inconsistências (e mantém compatibilidade com chamadas existentes)
        parametros = _normalizar_parametros(parametros)

        logger.info("Iniciando simulação com os seguintes parâmetros:")
        logger.info(f"ENTRADA: {parametros}")
        if layout:
            if isinstance(layout, list):
                logger.info(f"LAYOUT (primeiras linhas): {layout[:5]}")
            else:
                logger.info(f"LAYOUT: {layout}")

        if usar_des:
            logger.info("Executando simulação por eventos discretos (DES).")
            resultado = simular_eventos_discretos(parametros, layout, coletar_series=bool(parametros.get("coletar_series")))
        else:
            logger.info("Executando simulação determinística.")
            resultado = simular_deterministico(parametros, layout)

        logger.info("Simulação concluída com sucesso.")
        logger.info(f"SAÍDA: {resultado}")

        # Exporta PDF automaticamente, se solicitado
        if exportar_pdf_automatico:
            try:
                parametros_export = dict(parametros)
                if layout and isinstance(layout, list):
                    if isinstance(layout[0], list):
                        linhas = ["".join(linha) for linha in layout]
                    else:
                        linhas = layout
                    total_buffets = sum(linha.count('B') for linha in linhas)
                    parametros_export['numero_buffets'] = total_buffets
                # Import tardio: não acopla a execução do núcleo a dependências de relatório
                from src.pdf_exporter import exportar_pdf

                exportar_pdf(
                    resultado,
                    caminho_pdf,
                    parametros=parametros_export,
                    layout_ascii=layout
                )
                logger.info(f"PDF de resumo exportado automaticamente em: {caminho_pdf}")
                # NOVO: Informa também o GIF animado, se gerado
                if resultado.get('gif_layout'):
                    logger.info(f"GIF animado do layout salvo em: {resultado['gif_layout']}")
            except Exception as e:
                logger.error(f"Erro ao exportar PDF automaticamente: {e}")
        return resultado

    except Exception as e:
        logger.error("Erro ao executar a simulação.")
        logger.error(traceback.format_exc())
        raise

# Alias para compatibilidade com outros módulos
executar_simulacao = rodar_simulacao