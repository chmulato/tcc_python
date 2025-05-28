# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: excel_loader.py
# Descrição:
#   Este módulo implementa a importação de parâmetros de simulação
#   a partir de uma planilha Excel (.xlsx), permitindo alternativa
#   ao uso de arquivos YAML.
#
# Função principal:
#   - importar_dados_excel: lê parâmetros de uma planilha e retorna
#     um dicionário compatível com o simulador.
#
# Autor: Christian Mulato
# Data: 27/05/2025
# ===============================================

import openpyxl
from src.logger_config import get_logger

logger = get_logger()

def importar_dados_excel(caminho_arquivo):
    """
    Lê uma planilha Excel (.xlsx) e retorna um dicionário de parâmetros
    compatível com o simulador. Espera-se que a planilha tenha duas colunas:
    'parametro' e 'valor', com os mesmos nomes usados no parametros.yaml.
    """
    logger.info(f"Iniciando importação da planilha Excel: {caminho_arquivo}")
    try:
        wb = openpyxl.load_workbook(caminho_arquivo, data_only=True)
        ws = wb.active
        logger.info("Planilha carregada com sucesso.")

        parametros = {}
        for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):  # Pula o cabeçalho
            if not row or not row[0]:
                logger.debug(f"Linha {idx} ignorada (vazia ou sem parâmetro).")
                continue
            chave = str(row[0]).strip()
            valor = row[1]
            # Tenta converter valores numéricos
            try:
                if isinstance(valor, str):
                    valor = valor.replace(",", ".")
                    if valor.isdigit():
                        valor = int(valor)
                    else:
                        valor = float(valor)
                elif isinstance(valor, (int, float)):
                    pass
            except Exception as e:
                logger.warning(f"Falha ao converter valor '{valor}' para o parâmetro '{chave}' na linha {idx}: {e}")
            parametros[chave] = valor
            logger.debug(f"Parâmetro importado: {chave} = {valor}")
        logger.info(f"Importação concluída. Parâmetros carregados: {list(parametros.keys())}")
        return parametros
    except Exception as e:
        logger.error(f"Erro ao importar dados da planilha Excel: {e}")
        return None