# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: layout_parser.py
# Descrição:
#   Este módulo é responsável por ler e interpretar um arquivo
#   ASCII contendo o layout físico do restaurante. Ele converte
#   o conteúdo em uma matriz e identifica a posição dos elementos
#   relevantes como mesas, buffet, caixa e espaços livres.
#
# Objetivos:
#   - Facilitar a análise do ambiente físico na simulação
#   - Suportar múltiplos layouts para estudos comparativos
#
# Entradas esperadas:
#   - Arquivo .txt contendo layout ASCII
#
# Saídas:
#   - Matriz de caracteres representando o layout
#   - Dicionário com posições de objetos importantes (mesas, buffet, caixa, livres)
#
# Dependências Python:
#   - logging (padrão da biblioteca Python)
#   - traceback (padrão da biblioteca Python)
#
# Autor: Christian Mulato
# Data: 24/05/2025
# ===============================================

from src.logger_config import get_logger
import traceback

logger = get_logger()

def ler_layout_ascii(caminho_arquivo):
    """
    Lê um arquivo de layout ASCII e retorna uma matriz de caracteres.

    Parâmetros:
        caminho_arquivo: str - caminho para o arquivo .txt contendo o layout

    Retorna:
        matriz: list[list[str]] - matriz de caracteres representando o layout
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.read().splitlines()
        matriz = [list(linha) for linha in linhas]
        logger.info(f"Layout ASCII lido com sucesso: {caminho_arquivo}")
        return matriz
    except Exception as e:
        logger.error(f"Erro ao ler layout ASCII: {caminho_arquivo}")
        logger.error(traceback.format_exc())
        raise

def identificar_elementos(matriz):
    """
    Identifica posições de elementos relevantes no layout.

    Parâmetros:
        matriz: list[list[str]] - matriz do layout

    Retorna:
        dict - dicionário com listas de coordenadas por tipo de objeto
    """
    elementos = {
        'buffet': [],
        'mesas': [],
        'caixa': [],
        'livres': []
    }

    try:
        for y, linha in enumerate(matriz):
            for x, char in enumerate(linha):
                if char == 'B':
                    elementos['buffet'].append((x, y))
                elif char == 'M':
                    elementos['mesas'].append((x, y))
                elif char == 'C':
                    elementos['caixa'].append((x, y))
                elif char == ' ':
                    elementos['livres'].append((x, y))
        logger.info(f"Elementos identificados no layout: { {k: len(v) for k, v in elementos.items()} }")
        return elementos
    except Exception as e:
        logger.error("Erro ao identificar elementos no layout.")
        logger.error(traceback.format_exc())
        raise