# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: pdf_exporter.py
# Descrição:
#   Gera um relatório executivo em PDF com os resultados da simulação
#   de tempo de permanência de clientes no restaurante, utilizando o
#   método de Simulação por Eventos Discretos (DES).
#   O relatório inclui:
#     - Resumo dos parâmetros e resultados da simulação
#     - Gráfico de barras (clientes atendidos vs. rejeitados)
#     - Visualização do layout físico do restaurante (ASCII)
#     - (Opcional) Layout com fluxo do cliente, destacando o caminho típico
#       percorrido no ambiente (pode ser customizado para incluir setas ou destaques)
#
# Bibliotecas:
#   - reportlab (para geração de PDF)
#   - matplotlib (para gráficos)
#
# Observação:
#   O gráfico de fluxo do cliente pode ser representado no layout ASCII,
#   destacando o caminho típico do cliente, facilitando o entendimento leigo
#   sobre o funcionamento do restaurante simulado.
#
# Autor: Christian Mulato
# Última atualização: 26/05/2025
# ===============================================


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from src.logger_config import get_logger
import os

logger = get_logger()

def _as_number(v, default=0.0):
    try:
        if v is None:
            return default
        return float(v)
    except Exception:
        return default


def _as_int(v, default=0):
    try:
        if v is None:
            return default
        return int(v)
    except Exception:
        return default

def exportar_pdf(resultado, caminho_pdf, parametros=None, layout_ascii=None):
    """
    Gera um relatório executivo em PDF no formato solicitado.
    """
    try:
        if parametros is None:
            parametros = {
                "clientes_por_minuto": resultado.get("clientes_por_minuto"),
                "tempo_medio_almoco": resultado.get("tempo_medio_almoco"),
                "numero_de_mesas": resultado.get("numero_de_mesas"),
                "cadeiras_por_mesa": resultado.get("cadeiras_por_mesa"),
            }

        # Gera nome com data e hora no formato YYYY_MM_DD_HH_MM_SS_nome.pdf
        data_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        base, ext = os.path.splitext(os.path.basename(caminho_pdf))
        novo_nome = f"{data_str}_{base}{ext}"
        novo_caminho_pdf = os.path.join(os.path.dirname(caminho_pdf), novo_nome)

        logger.info(f"Iniciando exportação do relatório PDF: {novo_caminho_pdf}")
        diretorio = os.path.dirname(novo_caminho_pdf)
        if diretorio:
            os.makedirs(diretorio, exist_ok=True)

        c = canvas.Canvas(novo_caminho_pdf, pagesize=A4)
        largura, altura = A4
        y = altura - 50

        # Título
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(largura / 2, y, "==================================================")
        y -= 18
        c.drawCentredString(largura / 2, y, "RELATÓRIO DE SIMULAÇÃO – RESTAURANTE (MODELO DES)")
        y -= 18
        c.drawCentredString(largura / 2, y, "==================================================")
        y -= 30

        # Periodo simulado
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, f"Periodo simulado: {resultado.get('tempo_total_simulacao_min', 'N/A')} minutos")
        y -= 25

        # Clientes no periodo
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Clientes no periodo:")
        y -= 18
        c.setFont("Helvetica", 11)
        clientes_gerados = _as_int(resultado.get('clientes_simulados', resultado.get('total_clientes', 0)), 0)
        clientes_atendidos = _as_int(resultado.get('clientes_processados', 0), 0)
        clientes_nao_atendidos = _as_int(resultado.get('clientes_nao_atendidos', 0), 0)
        clientes_em_sistema = _as_int(resultado.get('clientes_em_sistema', 0), 0)
        c.drawCentredString(largura / 2, y, f"- Gerados (entradas): {clientes_gerados}")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Saidas atendidas: {clientes_atendidos}")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Saidas por rejeicao/abandono: {clientes_nao_atendidos}")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- No sistema ao final da janela: {clientes_em_sistema}")
        y -= 22

        # Desempenho (KPIs de engenharia)
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Desempenho operacional (KPIs):")
        y -= 18
        c.setFont("Helvetica", 11)
        tempo_medio_espera_mesa = _as_number(resultado.get('tempo_medio_espera_fila_mesa', resultado.get('tempo_medio_espera', 0.0)), 0.0)
        kpis = resultado.get("kpis") or {}
        tempo_medio_ciclo = _as_number(kpis.get("tempo_medio_ciclo_min", resultado.get("tempo_medio_permanencia_cliente", 0.0)), 0.0)
        ocup_cadeiras = _as_number(kpis.get("ocupacao_cadeiras_percent", resultado.get("uso_medio_cadeiras_percent", resultado.get("uso_medio_mesas", 0.0))), 0.0)
        ocup_mesas = _as_number(kpis.get("ocupacao_mesas_percent", resultado.get("uso_medio_mesas_percent", 0.0)), 0.0)

        c.drawCentredString(largura / 2, y, f"- Tempo medio de espera (mesa): {tempo_medio_espera_mesa:.2f} min")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Tempo medio de ciclo (entrada->saida): {tempo_medio_ciclo:.2f} min")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Ocupacao media (cadeiras): {ocup_cadeiras:.2f}%")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Ocupacao media (mesas): {ocup_mesas:.2f}%")
        y -= 22

        # Log resumo
        tempo_medio_espera = tempo_medio_espera_mesa
        tempo_medio_refeicao = _as_number(resultado.get('tempo_medio_permanencia_cliente', resultado.get('tempo_medio_almoco_min', 0.0)), 0.0)
        logger.info(
            f"Resumo do relatório PDF: Gerados={clientes_gerados}, "
            f"Atendidos={clientes_atendidos}, Rejeitados={clientes_nao_atendidos}, "
            f"Tempo médio de espera={tempo_medio_espera}, "
            f"Tempo médio de refeição={tempo_medio_refeicao}, "
            f"Ocupacao media (cadeiras)={ocup_cadeiras}%"
        )

        # Bottleneck (gargalo) e Mass Balance
        bott = (kpis.get("bottleneck") or {}).get("principal")
        estacoes = resultado.get("estacoes") or {}
        util_bott = _as_number((estacoes.get(bott) or {}).get("utilizacao_percent", 0.0), 0.0) if bott else 0.0
        mb = resultado.get("mass_balance") or {}
        mb_ok = bool(mb.get("ok", False))

        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Bottleneck (gargalo) e conservacao:")
        y -= 18
        c.setFont("Helvetica", 11)
        c.drawCentredString(largura / 2, y, f"- Gargalo principal: {bott or 'N/A'} (utilizacao ~ {util_bott:.1f}%)")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Mass Balance (entradas = saidas + no sistema): {'OK' if mb_ok else 'FALHOU'}")
        y -= 22

        # Interpretacao
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Interpretacao tecnica:")
        y -= 18
        c.setFont("Helvetica", 11)
        interpretacao = (
            f"Durante a janela operacional, {clientes_nao_atendidos} clientes foram rejeitados/abandonaram o sistema.\n"
            f"A ocupacao media de cadeiras foi {ocup_cadeiras:.2f}%, e o tempo medio de ciclo observado foi {tempo_medio_ciclo:.2f} min.\n"
            f"O gargalo estimado foi '{bott or 'N/A'}', que tende a governar o throughput em regime de saturacao."
        )
        for linha in interpretacao.split('\n'):
            c.drawCentredString(largura / 2, y, linha)
            y -= 15
        y -= 10

        # Recomendação
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Recomendacao:")
        y -= 18
        c.setFont("Helvetica", 11)
        taxa_rejeicao = (clientes_nao_atendidos / clientes_gerados) if clientes_gerados else 0
        if taxa_rejeicao > 0.10:
            c.drawCentredString(largura / 2, y, "Se a rejeição de clientes for superior a 10%, recomendamos considerar:")
            y -= 15
            c.drawCentredString(largura / 2, y, "- A adição de 3 a 5 mesas no ambiente")
            y -= 15
            c.drawCentredString(largura / 2, y, "- Redução do tempo médio de permanência com estratégias como autosserviço ou fluxo otimizado")
            y -= 15
            c.drawCentredString(largura / 2, y, "- Avaliação do horário de pico e reserva de espaço estratégico")
            y -= 10
        else:
            c.drawCentredString(largura / 2, y, "A taxa de rejeição está dentro do esperado. Mantenha o monitoramento periódico.")
            y -= 15
        y -= 10

        # Parâmetros técnicos
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "Parametros tecnicos utilizados:")
        y -= 18
        c.setFont("Helvetica", 11)
        c.drawCentredString(largura / 2, y, f"- Clientes por minuto: {parametros.get('clientes_por_minuto', 'N/A')}")
        y -= 15
        c.drawCentredString(largura / 2, y, f"- Tempo médio de refeição: {parametros.get('tempo_medio_almoco', 'N/A')} min")
        y -= 15
        c.drawCentredString(largura / 2, y, f"- Número de mesas: {parametros.get('numero_de_mesas', 'N/A')}")
        y -= 15
        c.drawCentredString(largura / 2, y, f"- Cadeiras por mesa: {parametros.get('cadeiras_por_mesa', 'N/A')}")
        y -= 22

        logger.info(
            f"Parâmetros técnicos: Clientes por minuto={parametros.get('clientes_por_minuto', 'N/A')}, "
            f"Tempo médio de refeição={parametros.get('tempo_medio_almoco', 'N/A')}, "
            f"Número de mesas={parametros.get('numero_de_mesas', 'N/A')}, "
            f"Cadeiras por mesa={parametros.get('cadeiras_por_mesa', 'N/A')}"
        )

        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredString(largura / 2, y, "Observacao: layout fisico do restaurante disponivel ao final deste relatorio (visual ASCII).")
        y -= 30

        # Gráfico de barras
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(4, 3))
            ax.bar(['Atendidos', 'Rejeitados'], [clientes_atendidos, clientes_nao_atendidos], color=['green', 'red'])
            ax.set_ylabel('Clientes')
            ax.set_title('Atendimento de Clientes')
            plt.tight_layout()
            temp_dir = os.path.join("monitoramento", "temp")
            os.makedirs(temp_dir, exist_ok=True)
            grafico_path = os.path.join(temp_dir, "grafico_atendimento.png")
            plt.savefig(grafico_path)
            plt.close(fig)

            c.showPage()
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(largura / 2, altura - 50, "Gráfico: Atendimento de Clientes")
            largura_grafico = 300
            altura_grafico = 220
            x_grafico = (largura - largura_grafico) / 2
            y_grafico = altura / 2 - altura_grafico / 2
            c.drawImage(grafico_path, x_grafico, y_grafico, width=largura_grafico, height=altura_grafico)
        except Exception as e:
            logger.error(f"Erro ao gerar gráfico de barras: {e}")

        c.save()
        logger.info(f"Relatório PDF gerado com sucesso em: {novo_caminho_pdf}")
        return novo_caminho_pdf

    except Exception as e:
        logger.error(f"Erro ao exportar PDF: {caminho_pdf}")
        logger.error(e)
        raise
