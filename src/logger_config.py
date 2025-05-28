# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: logger_config.py
# Descrição:
#   Configura e retorna um logger padrão do sistema para registrar
#   eventos, erros e informações de execução em arquivo de log.
#   O log é salvo na pasta 'monitoramento' com o nome 'log_execucao.log'.
#
# Dependências Python:
#   - logging (padrão da biblioteca Python)
#   - os (padrão da biblioteca Python)
#
# Autor: Christian Mulato
# Data: 24/05/2025
# ===============================================

import logging
import os

os.makedirs("monitoramento", exist_ok=True)

def get_logger():
    logger = logging.getLogger("simulador_restaurante")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # Define encoding UTF-8 para evitar caracteres estranhos
        fh = logging.FileHandler("monitoramento/log_execucao.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger