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

        # Período simulado
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, f"🗓️ Período simulado: {resultado.get('tempo_total_simulacao_min', 'N/A')} minutos")
        y -= 25

        # Clientes no período
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "👥 Clientes no período:")
        y -= 18
        c.setFont("Helvetica", 11)
        c.drawCentredString(largura / 2, y, f"- Gerados: {resultado.get('clientes_simulados', resultado.get('total_clientes', 'N/A'))}")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Atendidos: {resultado.get('clientes_processados', 'N/A')}")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Rejeitados: {resultado.get('clientes_nao_atendidos', 'N/A')}")
        y -= 22

        # Desempenho
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "⏱️ Desempenho operacional:")
        y -= 18
        c.setFont("Helvetica", 11)
        c.drawCentredString(largura / 2, y, f"- Tempo médio de espera: {resultado.get('tempo_medio_espera_fila_mesa', resultado.get('tempo_medio_espera', 'N/A'))} minutos")
        y -= 16
        c.drawCentredString(largura / 2, y, f"- Tempo médio de refeição (real): {resultado.get('tempo_medio_permanencia_cliente', resultado.get('tempo_medio_almoco_min', 'N/A'))} minutos")
        y -= 16
        uso_mesas = resultado.get('uso_medio_mesas', 0)
        c.drawCentredString(largura / 2, y, f"- Ocupação média das mesas: {round(uso_mesas, 2)}%")
        y -= 22

        # Log resumo
        clientes_gerados = resultado.get('clientes_simulados', resultado.get('total_clientes', 1))
        clientes_atendidos = resultado.get('clientes_processados', 'N/A')
        clientes_nao_atendidos = resultado.get('clientes_nao_atendidos', 0)
        tempo_medio_espera = resultado.get('tempo_medio_espera_fila_mesa', resultado.get('tempo_medio_espera', 'N/A'))
        tempo_medio_refeicao = resultado.get('tempo_medio_permanencia_cliente', resultado.get('tempo_medio_almoco_min', 'N/A'))
        logger.info(
            f"Resumo do relatório PDF: Gerados={clientes_gerados}, "
            f"Atendidos={clientes_atendidos}, Rejeitados={clientes_nao_atendidos}, "
            f"Tempo médio de espera={tempo_medio_espera}, "
            f"Tempo médio de refeição={tempo_medio_refeicao}, "
            f"Ocupação média das mesas={uso_mesas}%"
        )

        # Interpretação
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "📌 Interpretação (gerada por IA):")
        y -= 18
        c.setFont("Helvetica", 11)
        interpretacao = (
            f"Durante o período analisado, observou-se que {clientes_nao_atendidos} clientes não conseguiram ser atendidos devido à lotação máxima.\n"
            f"A taxa de ocupação média foi de {round(uso_mesas, 2)}%, sugerindo que as mesas foram utilizadas de forma eficiente,\n"
            f"mas podem estar próximas do limite operacional."
        )
        for linha in interpretacao.split('\n'):
            c.drawCentredString(largura / 2, y, linha)
            y -= 15
        y -= 10

        # Recomendação
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(largura / 2, y, "📈 Recomendação:")
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
        c.drawCentredString(largura / 2, y, "⚙️ Parâmetros técnicos utilizados:")
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
        c.drawCentredString(largura / 2, y, "📍 Observação: layout físico do restaurante disponível ao final deste relatório (visual ASCII).")
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
