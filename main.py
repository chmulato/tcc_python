# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Arquivo: main.py
# Descrição:
#   Ponto de entrada principal da aplicação.
#   Inicializa a interface gráfica, gerencia a importação de dados
#   (YAML e layout ASCII), executa a simulação e exporta relatórios.
#
# Dependências Python:
#   - tkinter (padrão da biblioteca Python)
#   - src.interface (interface gráfica)
#   - src.simulador (lógica da simulação)
#   - src.yaml_loader (importação de parâmetros YAML)
#   - src.layout_parser (leitura do layout ASCII)
#   - src.pdf_exporter (geração de PDF)
#   - src.logger_config (logger do sistema)
#   - traceback (padrão da biblioteca Python)
#   - os (padrão da biblioteca Python)
#
# Autor: Christian Mulato
# Data: 24/05/2025
# ===============================================

import tkinter as tk
from tkinter import filedialog, messagebox
from src.interface import criar_janela_interface
from src.simulador import rodar_simulacao
from src.yaml_loader import importar_dados_yaml
from src.layout_parser import ler_layout_ascii
from src.layout_pdf_exporter import exportar_layout_ascii_para_pdf
from src.pdf_exporter import exportar_pdf
from src.logger_config import get_logger
import traceback
import os

logger = get_logger()

dados_simulacao = {
    'parametros': None,
    'layout': None,
    'resultado': None
}

def ativar_simular_se_pronto(btn_simular):
    if dados_simulacao['parametros'] and dados_simulacao['layout']:
        btn_simular.config(state=tk.NORMAL)

def iniciar_simulador():
    try:
        logger.info("Iniciando a aplicação.")
        root = tk.Tk()
        root.title("Simulador de Permanência no Restaurante")
        global entradas_globais
        global btn_simular_global
        entradas, btn_simular = criar_janela_interface(root, callbacks={
            'importar_yaml': lambda: callback_importar_yaml(btn_simular, entradas),
            'importar_layout': lambda: callback_importar_layout(btn_simular),
            'simular': lambda: callback_simular(entradas),
            'exportar_pdf': callback_exportar_pdf
        })
        entradas_globais = entradas
        btn_simular_global = btn_simular
        root.mainloop()
    except Exception as e:
        logger.error("Falha ao iniciar a interface.")
        logger.error(traceback.format_exc())
        raise

def callback_importar_yaml(btn_simular, entradas):
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos YAML", "*.yaml;*.yml")])
    if caminho:
        try:
            logger.info(f"Importando dados do YAML: {caminho}")
            parametros = importar_dados_yaml(caminho)
            dados_simulacao['parametros'] = parametros
            # Atualiza os campos da interface
            entradas["Clientes por minuto:"].set(str(parametros.get("clientes_por_minuto", "")))
            entradas["Tempo médio de almoço (min):"].set(str(parametros.get("tempo_medio_almoco", "")))
            entradas["Cadeiras por mesa:"].set(str(parametros.get("cadeiras_por_mesa", "")))
            entradas["Número de mesas:"].set(str(parametros.get("numero_de_mesas", "")))
            entradas["Tempo total da simulação (min):"].set(str(parametros.get("tempo_total_simulacao", "")))
            messagebox.showinfo(
                "Importação",
                "Dados importados do arquivo YAML e atualizados na tela.\n"
                "Esses dados serão usados na próxima simulação, a menos que você altere manualmente os campos."
            )
            ativar_simular_se_pronto(btn_simular)
        except Exception as e:
            logger.error("Erro ao importar YAML.")
            logger.error(traceback.format_exc())
            messagebox.showerror("Erro", str(e))

def callback_importar_layout(btn_simular):
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos ASCII", "*.txt")])
    if caminho:
        try:
            logger.info(f"Importando layout: {caminho}")
            layout = ler_layout_ascii(caminho)
            dados_simulacao['layout'] = layout
            messagebox.showinfo("Layout", "Layout importado com sucesso.")
            ativar_simular_se_pronto(btn_simular)
        except Exception as e:
            logger.error("Erro ao importar layout.")
            logger.error(traceback.format_exc())
            messagebox.showerror("Erro", str(e))

def callback_simular(entradas):
    try:
        logger.info("Iniciando simulação...")
        parametros = dados_simulacao['parametros']
        if parametros:
            origem = "Os dados do arquivo YAML estão sendo usados para esta simulação."
        else:
            origem = "Os dados digitados nos campos da tela estão sendo usados para esta simulação."
            parametros = {
                'clientes_por_minuto': float(entradas["Clientes por minuto:"].get()),
                'tempo_medio_almoco': float(entradas["Tempo médio de almoço (min):"].get()),
                'cadeiras_por_mesa': int(entradas["Cadeiras por mesa:"].get()),
                'numero_de_mesas': int(entradas["Número de mesas:"].get()),
                'tempo_total_simulacao': int(entradas["Tempo total da simulação (min):"].get())
            }
        messagebox.showinfo("Fonte dos Dados", origem)
        logger.info(origem)

        layout = dados_simulacao['layout']
        if not layout:
            raise ValueError("Layout ainda não carregado.")
        resultado = rodar_simulacao(parametros, layout, exportar_pdf_automatico=True)

        # Inclui os parâmetros de entrada no resultado para o relatório PDF
        resultado.update({
            'clientes_por_minuto': parametros.get('clientes_por_minuto'),
            'tempo_medio_almoco': parametros.get('tempo_medio_almoco'),
            'numero_de_mesas': parametros.get('numero_de_mesas'),
            'cadeiras_por_mesa': parametros.get('cadeiras_por_mesa'),
            'numero_caixas': parametros.get('numero_caixas', 1),  # Ajuste se necessário
            'tempo_total_simulacao_min': parametros.get('tempo_total_simulacao'),
            'capacidade_maxima_fila': parametros.get('capacidade_maxima_fila', 'N/A'),
            'variabilidade_almoco': parametros.get('variabilidade_almoco', 0),
            'variabilidade_chegada': parametros.get('variabilidade_chegada', 0),
        })

        dados_simulacao['resultado'] = resultado
        logger.info("Simulação executada com sucesso.")

        # Exporta o layout ASCII em PDF separado
        caminho_layout_pdf = "resultados/relatorios/layout_simulacao.pdf"
        os.makedirs(os.path.dirname(caminho_layout_pdf), exist_ok=True)
        logger.info(f"Iniciando exportação do layout ASCII em PDF separado: {caminho_layout_pdf}")
        try:
            exportar_layout_ascii_para_pdf("layouts/layout_padrao.txt", caminho_layout_pdf)
            logger.info(f"Layout ASCII exportado em PDF separado com sucesso: {caminho_layout_pdf}")
        except Exception as e:
            logger.error(f"Erro ao exportar layout ASCII em PDF separado: {e}")

        messagebox.showinfo("Simulação", "Simulação concluída com sucesso.\n\n"
                                         f"Relatório: resultados/relatorios/resultado_simulacao.pdf\n"
                                         f"Layout ASCII: {caminho_layout_pdf}")
    except Exception as e:
        logger.error("Erro durante a simulação.")
        logger.error(traceback.format_exc())
        messagebox.showerror("Erro na Simulação", str(e))

def callback_exportar_pdf():
    try:
        logger.info("Exportando relatório PDF...")
        resultado = dados_simulacao['resultado']
        parametros = dados_simulacao['parametros']
        layout = dados_simulacao['layout']
        if not resultado:
            raise ValueError("Simulação ainda não foi executada.")
        caminho = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")],
            title="Salvar Relatório"
        )
        logger.info(f"Parâmetros enviados para o PDF: {parametros}")
        if caminho:
            exportar_pdf(
                resultado,
                caminho,
                parametros=parametros,
                layout_ascii=layout
            )
            logger.info(f"PDF exportado com sucesso: {caminho}")
            messagebox.showinfo("Exportação", "Relatório PDF exportado com sucesso.")
    except Exception as e:
        logger.error("Erro ao exportar PDF.")
        logger.error(traceback.format_exc())
        messagebox.showerror("Erro ao Exportar", str(e))

if __name__ == "__main__":
    iniciar_simulador()