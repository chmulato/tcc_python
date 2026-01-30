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

        if not isinstance(dados, dict):
            raise ValueError("Arquivo YAML inválido: esperado um dicionário de parâmetros no topo do arquivo.")

        # Validação mínima (robusta): apenas o necessário para rodar com defaults seguros.
        # Demais campos são opcionais e podem ser calibrados conforme o contexto.
        campos_obrigatorios = [
            "clientes_por_minuto",
            "tempo_medio_almoco",
            "cadeiras_por_mesa",
            "numero_de_mesas",
            "tempo_total_simulacao",
        ]
        ausentes = [c for c in campos_obrigatorios if c not in dados]
        if ausentes:
            msg = f"Campos obrigatórios ausentes no YAML: {', '.join(ausentes)}"
            logger.error(msg)
            raise ValueError(msg)

        # Campos esperados (opcionais). Se ausentes, apenas registra (o núcleo aplica defaults).
        campos_opcionais = [
            "tempo_medio_atendimento",
            "tempo_medio_espera",
            "variabilidade_almoco",
            "variabilidade_chegada",
            "capacidade_maxima_fila",
            "tempo_max_espera_fila",
            "modo_ocupacao",
            "numero_caixas",
            "numero_buffets",
            "tempo_entre_clientes",
            "processar_pos_fechamento",
            "tempo_buffet",
            "tempo_balcao",
            "coletar_series",
        ]
        for campo in campos_opcionais:
            if campo not in dados:
                logger.debug(f"Campo opcional '{campo}' ausente no YAML (default será aplicado pelo simulador).")

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