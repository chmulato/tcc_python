# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: layout_pdf_exporter.py
# Descrição:
#   Gera um PDF a partir de um layout ASCII (arquivo ou lista de strings),
#   imprimindo o conteúdo do layout como texto, com legenda e totais de cada elemento.
#
#   O PDF gerado será salvo em:
#     resultados/relatorios/layout_da_simulacao.pdf
#
# Autor: Christian Mulato
# Data: 24/05/2025
#
# Dependências:
#   - Python >= 3.8
#   - reportlab (pip install reportlab)
#   - src.logger_config (logger do sistema, para logs)
# ===============================================

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from src.logger_config import get_logger

logger = get_logger()

def exportar_layout_ascii_para_pdf(layout_ascii, caminho_pdf, cadeiras_por_mesa=4):
    """
    Exporta um layout ASCII (arquivo ou lista de strings) para PDF.

    Parâmetros:
        layout_ascii (str ou list): caminho do arquivo de layout ou lista de linhas (strings)
        caminho_pdf (str): caminho do PDF de saída
        cadeiras_por_mesa (int): quantidade de cadeiras por mesa (para legenda)
    """
    try:
        # Gera nome com data e hora no formato YYYY_MM_DD_HH_MM_SS_nome.pdf
        data_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        base, ext = os.path.splitext(os.path.basename(caminho_pdf))
        novo_nome = f"{data_str}_{base}{ext}"
        novo_caminho_pdf = os.path.join(os.path.dirname(caminho_pdf), novo_nome)

        # Detecta se é caminho de arquivo ou lista de linhas
        if isinstance(layout_ascii, str) and os.path.isfile(layout_ascii):
            logger.info(f"Iniciando exportação do layout ASCII para PDF: {layout_ascii} -> {novo_caminho_pdf}")
            with open(layout_ascii, "r", encoding="utf-8") as f:
                linhas = [linha.rstrip('\n') for linha in f]
        elif isinstance(layout_ascii, list):
            logger.info(f"Iniciando exportação do layout ASCII (lista) para PDF: {novo_caminho_pdf}")
            linhas = [linha.rstrip('\n') if isinstance(linha, str) else "".join(linha) for linha in layout_ascii]
        else:
            raise ValueError("layout_ascii deve ser caminho de arquivo ou lista de strings.")

        logger.info("Layout lido com sucesso para exportação.")

        # Conta os elementos
        total_mesas = sum(linha.count('M') for linha in linhas)
        total_buffets = sum(linha.count('B') for linha in linhas)
        total_caixas = sum(linha.count('C') for linha in linhas)
        total_cadeiras = total_mesas * cadeiras_por_mesa

        c = canvas.Canvas(novo_caminho_pdf, pagesize=A4)
        largura, altura = A4

        # Centraliza o título no topo
        c.setFont("Helvetica-Bold", 16)
        titulo = "Layout do Restaurante (ASCII)"
        largura_titulo = c.stringWidth(titulo, "Helvetica-Bold", 16)
        c.drawString((largura - largura_titulo) / 2, altura - 50, titulo)

        # Centraliza o layout na página
        c.setFont("Courier", 12)
        altura_layout = len(linhas) * 16
        y_inicio = (altura + altura_layout) // 2 - 16  # Centralizado verticalmente

        largura_max_linha = max([c.stringWidth(linha, "Courier", 12) for linha in linhas]) if linhas else 0
        x_inicio = (largura - largura_max_linha) / 2

        # --- Desenha borda vermelha ao redor do layout ---
        padding = 10
        box_width = largura_max_linha + 2 * padding
        box_height = altura_layout + 2 * padding
        box_x = x_inicio - padding
        box_y = y_inicio - altura_layout - padding + 16  # Ajuste para alinhar topo

        c.setStrokeColorRGB(1, 0, 0)  # Vermelho
        c.setLineWidth(2)
        c.rect(box_x, box_y, box_width, box_height, stroke=1, fill=0)
        # --- Fim da borda ---

        y = y_inicio
        for linha in linhas:
            c.drawString(x_inicio, y, linha)
            y -= 16
            if y < 80:  # Reservar espaço para a legenda e totais
                c.showPage()
                c.setFont("Courier", 12)
                y = altura - 50

        # Legenda e totais no rodapé
        c.setFont("Helvetica", 10)
        legenda = (
            "Legenda: M = Mesa   B = Buffet   C = Caixa de Pagamento   "
            f"Cadeiras por mesa: {cadeiras_por_mesa}   Total de cadeiras: {total_cadeiras}"
        )
        totais = (
            f"Total: Mesas (M): {total_mesas}   Buffets (B): {total_buffets}   Caixas (C): {total_caixas}"
        )
        c.drawString(50, 45, legenda)
        c.drawString(50, 30, totais)

        c.save()
        logger.info(f"PDF do layout gerado com sucesso em: {novo_caminho_pdf}")
        print(f"PDF gerado em: {novo_caminho_pdf}")

    except Exception as e:
        logger.error(f"Erro ao exportar layout para PDF: {e}")
        raise
    
if __name__ == "__main__":
    caminho_layout = os.path.join("layouts", "layout_padrao.txt")
    caminho_pdf = os.path.join("resultados", "relatorios", "layout_da_simulacao.pdf")
    os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
    logger.info(f"Iniciando exportação do layout ASCII em PDF separado: {caminho_pdf}")
    try:
        # Altere o valor de cadeiras_por_mesa conforme sua configuração
        exportar_layout_ascii_para_pdf(caminho_layout, caminho_pdf, cadeiras_por_mesa=4)
    except Exception as e:
        logger.error(f"Falha ao exportar o layout ASCII em PDF separado: {e}")
        print(f"Erro ao exportar o layout ASCII em PDF separado: {e}")