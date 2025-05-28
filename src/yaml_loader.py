# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: yaml_loader.py
# Descrição:
#   Este módulo implementa a leitura e gravação de parâmetros
#   de simulação a partir de arquivos YAML (.yaml ou .yml).
#   Permite carregar os dados do sistema e também salvar
#   configurações para reutilização.
#
# Funcionalidades:
#   - Importação de parâmetros de simulação via arquivo YAML
#   - Validação dos campos obrigatórios
#   - Exportação/salvamento de parâmetros em YAML para reuso
#
# Dependências Python:
#   - yaml (PyYAML)
#   - os (padrão da biblioteca Python)
#   - traceback (padrão da biblioteca Python)
#   - src.logger_config (logger do sistema)
#
# Autor: Christian Mulato
# Data: 24/05/2025
# ===============================================

import yaml
import os
from src.logger_config import get_logger
import traceback

logger = get_logger()

def importar_dados_yaml(caminho_arquivo):
    """
    Lê os parâmetros de simulação de um arquivo YAML.

    Parâmetros:
        caminho_arquivo (str): caminho do arquivo .yaml

    Retorna:
        dict: parâmetros da simulação
    """
    try:
        logger.info(f"Iniciando importação do arquivo YAML: {caminho_arquivo}")
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = yaml.safe_load(f)

        # Validação mínima para simulação DES ideal
        campos_esperados = [
            'clientes_por_minuto',
            'tempo_medio_almoco',
            'cadeiras_por_mesa',
            'numero_de_mesas',
            'tempo_medio_atendimento',
            'tempo_medio_espera',
            'tempo_total_simulacao',
            'variabilidade_almoco',
            'variabilidade_chegada',
            'capacidade_maxima_fila',
            'modo_ocupacao',
            'numero_caixas',
            'tempo_entre_clientes'
        ]
        for campo in campos_esperados:
            if campo not in dados:
                logger.error(f"Campo obrigatório '{campo}' ausente no arquivo YAML.")
                raise ValueError(f"Campo obrigatório '{campo}' ausente no arquivo YAML.")

        logger.info(f"Parâmetros importados do YAML: {dados}")
        return dados
    except Exception as e:
        logger.error(f"Erro ao importar dados do YAML: {caminho_arquivo}")
        logger.error(traceback.format_exc())
        raise

def salvar_dados_yaml(dados, caminho_arquivo="data/config/parametros.yaml"):
    """
    Salva os parâmetros fornecidos em um arquivo YAML.

    Parâmetros:
        dados (dict): dicionário com parâmetros
        caminho_arquivo (str): caminho do arquivo de saída
    """
    try:
        logger.info(f"Salvando parâmetros no arquivo YAML: {caminho_arquivo}")
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            yaml.dump(dados, f, default_flow_style=False, allow_unicode=True)
        logger.info("Parâmetros salvos com sucesso no YAML.")
    except Exception as e:
        logger.error(f"Erro ao salvar dados no YAML: {caminho_arquivo}")
        logger.error(traceback.format_exc())
        raise