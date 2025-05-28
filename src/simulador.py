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

from src.logger_config import get_logger
from src.pdf_exporter import exportar_pdf

# NOVO: Importa visualizador para imagens e animação
from src.visualizador_layout import desenhar_layout, gerar_animacao

logger = get_logger()

class Evento:
    def __init__(self, tempo, tipo, cliente_id=None):
        self.tempo = tempo
        self.tipo = tipo  # Ex: 'chegada', 'buffet', 'balcao', 'pesagem', 'caixa', 'pagamento', 'procura_mesa', 'saida'
        self.cliente_id = cliente_id

    def __lt__(self, other):
        return self.tempo < other.tempo

def simular_eventos_discretos(parametros, layout=None):
    """
    Simulação baseada em eventos discretos (DES) com coleta de estatísticas para relatório.
    Também gera imagens do layout e um GIF animado minuto a minuto, se layout for fornecido.
    """
    tempo_atual = 0
    agenda = []
    heapq.heapify(agenda)
    clientes_gerados = 0
    total_clientes = int(parametros['clientes_por_minuto'] * parametros['tempo_total_simulacao'])
    eventos_processados = 0

    # Estatísticas
    tempo_total_permanencia = 0
    tempo_total_espera_fila_mesa = 0
    clientes_que_esperaram_mesa = 0
    tamanho_max_fila_mesa = 0
    clientes_nao_atendidos = 0

    # Controle de filas e tempos individuais
    fila_mesa = []
    fila_buffet = []
    fila_balcao = []
    fila_caixa = []
    mesas_livres = parametros['numero_de_mesas']
    cadeiras_por_mesa = parametros['cadeiras_por_mesa']
    tempos_chegada = {}
    tempos_saida = {}

    # --- NOVO: Controle real de ocupação das mesas ---
    numero_de_mesas = parametros['numero_de_mesas']
    tempo_total_simulacao = parametros['tempo_total_simulacao']
    ocupacao_mesas = 0  # Soma do tempo em que cada mesa esteve ocupada
    ultimo_tempo = 0
    mesas_ocupadas = 0

    # Cada mesa: None (livre) ou (cliente_id, tempo_saida)
    mesas = [None for _ in range(numero_de_mesas)]

    # --- NOVO: Para visualização minuto a minuto ---
    layout_base = layout if layout and isinstance(layout, list) else None
    lista_mesas_ocupadas_por_tempo = [[] for _ in range(tempo_total_simulacao + 1)]

    # Parâmetro para rejeição: tempo máximo de espera na fila (opcional)
    tempo_max_espera_fila = parametros.get('tempo_max_espera_fila', None)

    # Agendar chegada do primeiro cliente
    heapq.heappush(agenda, Evento(0, 'chegada', cliente_id=1))

    minuto_visual = 0

    while agenda and clientes_gerados < total_clientes:
        evento = heapq.heappop(agenda)
        if evento.tempo > tempo_total_simulacao:
            logger.info(f"Evento no tempo {evento.tempo} ignorado (limite tempo_total_simulacao = {tempo_total_simulacao}).")
            break

        # Atualiza ocupação das mesas para todos os minutos entre ultimo_tempo e evento.tempo
        if layout_base:
            for minuto in range(int(ultimo_tempo), int(evento.tempo)):
                if minuto > tempo_total_simulacao:
                    break
                mesas_ocupadas_pos = [idx for idx, mesa in enumerate(mesas) if mesa is not None]
                lista_mesas_ocupadas_por_tempo[minuto] = list(mesas_ocupadas_pos)
                logger.debug(f"Mesas ocupadas no minuto {minuto}: {mesas_ocupadas_pos}")

        # --- Atualiza ocupação das mesas ---
        delta = evento.tempo - ultimo_tempo
        ocupacao_mesas += sum(1 for m in mesas if m is not None) * delta
        ultimo_tempo = evento.tempo
        tempo_atual = evento.tempo
        eventos_processados += 1

        if evento.tipo == 'chegada':
            clientes_gerados += 1
            tempos_chegada[evento.cliente_id] = tempo_atual
            if clientes_gerados < total_clientes:
                proxima_chegada = tempo_atual + parametros.get('tempo_entre_clientes', 1)
                heapq.heappush(agenda, Evento(proxima_chegada, 'chegada', cliente_id=clientes_gerados+1))
            # Cliente entra na fila do buffet
            fila_buffet.append(evento.cliente_id)
            if len(fila_buffet) == 1:
                heapq.heappush(agenda, Evento(tempo_atual, 'buffet', cliente_id=evento.cliente_id))

        elif evento.tipo == 'buffet':
            tempo_buffet = parametros.get('tempo_buffet', 2)
            cliente_id = evento.cliente_id
            fila_buffet.pop(0)
            # Agenda pesagem na balança
            heapq.heappush(agenda, Evento(tempo_atual + tempo_buffet, 'balcao', cliente_id=cliente_id))
            # Atende próximo da fila do buffet, se houver
            if fila_buffet:
                prox_cliente = fila_buffet[0]
                heapq.heappush(agenda, Evento(tempo_atual, 'buffet', cliente_id=prox_cliente))

        elif evento.tipo == 'balcao':
            cliente_id = evento.cliente_id
            fila_balcao.append(cliente_id)
            if len(fila_balcao) == 1:
                heapq.heappush(agenda, Evento(tempo_atual, 'pesagem', cliente_id=cliente_id))

        elif evento.tipo == 'pesagem':
            tempo_balcao = parametros.get('tempo_balcao', 1)
            cliente_id = evento.cliente_id
            fila_balcao.pop(0)
            # Agenda pagamento no caixa
            heapq.heappush(agenda, Evento(tempo_atual + tempo_balcao, 'caixa', cliente_id=cliente_id))
            # Atende próximo da fila da balança, se houver
            if fila_balcao:
                prox_cliente = fila_balcao[0]
                heapq.heappush(agenda, Evento(tempo_atual, 'pesagem', cliente_id=prox_cliente))

        elif evento.tipo == 'caixa':
            cliente_id = evento.cliente_id
            fila_caixa.append(cliente_id)
            if len(fila_caixa) == 1:
                heapq.heappush(agenda, Evento(tempo_atual, 'pagamento', cliente_id=cliente_id))

        elif evento.tipo == 'pagamento':
            tempo_caixa = parametros.get('tempo_medio_atendimento', 2)
            cliente_id = evento.cliente_id
            fila_caixa.pop(0)
            # Agenda procura mesa
            heapq.heappush(agenda, Evento(tempo_atual + tempo_caixa, 'procura_mesa', cliente_id=cliente_id))
            # Atende próximo da fila do caixa, se houver
            if fila_caixa:
                prox_cliente = fila_caixa[0]
                heapq.heappush(agenda, Evento(tempo_atual, 'pagamento', cliente_id=prox_cliente))

        elif evento.tipo == 'procura_mesa':
            # Libera mesas cujo tempo de saída já passou
            for idx, mesa in enumerate(mesas):
                if mesa is not None and mesa[1] <= tempo_atual:
                    mesas[idx] = None
            # Tenta alocar mesa livre
            mesa_alocada = None
            for idx, mesa in enumerate(mesas):
                if mesa is None:
                    mesa_alocada = idx
                    break
            if mesa_alocada is not None:
                tempo_refeicao = parametros['tempo_medio_almoco']
                tempo_saida = tempo_atual + tempo_refeicao
                mesas[mesa_alocada] = (evento.cliente_id, tempo_saida)
                heapq.heappush(agenda, Evento(tempo_saida, 'saida', cliente_id=evento.cliente_id))
            else:
                fila_mesa.append((evento.cliente_id, tempo_atual))
                tamanho_max_fila_mesa = max(tamanho_max_fila_mesa, len(fila_mesa))

        elif evento.tipo == 'saida':
            tempos_saida[evento.cliente_id] = tempo_atual
            # Libera mesa ocupada pelo cliente
            for idx, mesa in enumerate(mesas):
                if mesa is not None and mesa[0] == evento.cliente_id:
                    mesas[idx] = None
                    break
            # Atende próximo da fila de mesas, se houver
            if fila_mesa:
                prox_cliente_id, tempo_entrada_fila = fila_mesa.pop(0)
                espera = tempo_atual - tempo_entrada_fila
                tempo_total_espera_fila_mesa += espera
                clientes_que_esperaram_mesa += 1
                mesa_alocada = None
                for idx, mesa in enumerate(mesas):
                    if mesa is None:
                        mesa_alocada = idx
                        break
                if mesa_alocada is not None:
                    tempo_refeicao = parametros['tempo_medio_almoco']
                    tempo_saida = tempo_atual + tempo_refeicao
                    mesas[mesa_alocada] = (prox_cliente_id, tempo_saida)
                    heapq.heappush(agenda, Evento(tempo_saida, 'saida', cliente_id=prox_cliente_id))

    # --- Após processar todos os eventos, preenche até o fim do tempo_total_simulacao ---
    if layout_base:
        for minuto in range(int(ultimo_tempo), tempo_total_simulacao + 1):
            mesas_ocupadas_pos = [idx for idx, mesa in enumerate(mesas) if mesa is not None]
            lista_mesas_ocupadas_por_tempo[minuto] = list(mesas_ocupadas_pos)
            logger.debug(f"Mesas ocupadas no minuto {minuto}: {mesas_ocupadas_pos}")

    # --- Atualiza ocupação até o fim da simulação ---
    delta = tempo_total_simulacao - ultimo_tempo
    ocupacao_mesas += sum(1 for m in mesas if m is not None) * delta

    # Calcule estatísticas finais
    clientes_processados = 0
    for cid in tempos_chegada:
        if cid in tempos_saida:
            tempo_total_permanencia += tempos_saida[cid] - tempos_chegada[cid]
            clientes_processados += 1

    uso_medio_mesas = (ocupacao_mesas / (numero_de_mesas * tempo_total_simulacao)) * 100 if numero_de_mesas > 0 and tempo_total_simulacao > 0 else 0

    resultado_des = {
        'eventos_processados': eventos_processados,
        'clientes_simulados': clientes_gerados,
        'clientes_processados': clientes_processados,
        'tempo_medio_permanencia_cliente': round(tempo_total_permanencia / clientes_processados, 2) if clientes_processados else 0,
        'clientes_que_esperaram_mesa': clientes_que_esperaram_mesa,
        'tempo_medio_espera_fila_mesa': round(tempo_total_espera_fila_mesa / clientes_que_esperaram_mesa, 2) if clientes_que_esperaram_mesa else 0,
        'tamanho_max_fila_mesa': tamanho_max_fila_mesa,
        'clientes_nao_atendidos': clientes_nao_atendidos,
        'uso_medio_mesas': round(uso_medio_mesas, 1),
    }
    resultado_des.update(parametros)

    # --- Gera animação se layout foi fornecido ---
    if layout_base and lista_mesas_ocupadas_por_tempo:
        try:
            caminho_gif = gerar_animacao(layout_base, lista_mesas_ocupadas_por_tempo)
            resultado_des['gif_layout'] = caminho_gif
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
        logger.info("Iniciando simulação com os seguintes parâmetros:")
        logger.info(f"ENTRADA: {parametros}")
        if layout:
            if isinstance(layout, list):
                logger.info(f"LAYOUT (primeiras linhas): {layout[:5]}")
            else:
                logger.info(f"LAYOUT: {layout}")

        if usar_des:
            logger.info("Executando simulação por eventos discretos (DES).")
            resultado = simular_eventos_discretos(parametros, layout)
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