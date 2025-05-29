# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: simulador_gui.py
# Descrição:
#   Interface gráfica para entrada de parâmetros,
#   execução da simulação e exibição dos resultados.
#   Permite importar dados de TXT, YAML ou Excel
#   e exportar o relatório da simulação em PDF.
#
# Autor: Christian Mulato
# Data: 27/05/2025
# ===============================================

import tkinter as tk
import os
from tkinter import ttk, messagebox, filedialog
from simulador import executar_simulacao
from pdf_exporter import exportar_pdf
from logger_config import get_logger
from yaml_loader import importar_dados_yaml
from excel_loader import importar_dados_excel
from PIL import Image, ImageTk

logger = get_logger()

def importar_dados_txt(caminho_arquivo):
    dados = {}
    try:
        with open(caminho_arquivo, 'r') as f:
            for linha in f:
                linha = linha.strip()
                if linha and not linha.startswith("#"):
                    if ":" in linha:
                        chave, valor = linha.split(":", 1)
                        chave = chave.strip()
                        valor = valor.strip()
                        if '.' in valor:
                            dados[chave] = float(valor)
                        else:
                            dados[chave] = int(valor)
        logger.info(f"Dados importados do TXT: {caminho_arquivo}")
        return dados
    except Exception as e:
        logger.error(f"Erro ao ler arquivo TXT: {e}")
        return None

class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Tempo de Almoço - Restaurante")
        self.root.geometry("600x400")

        # Parâmetros principais ajustáveis pelo operador
        self.campos = {
            "clientes_por_minuto": tk.DoubleVar(),
            "tempo_medio_almoco": tk.DoubleVar(),
            "numero_de_mesas": tk.IntVar(),
            "cadeiras_por_mesa": tk.IntVar(),
            "tempo_total_simulacao": tk.IntVar()
        }
        self.tipo_importacao_var = tk.StringVar(value="txt")  # txt, yaml ou excel

        self._criar_interface()

    def _criar_interface(self):
        frm = ttk.Frame(self.root, padding=15)
        frm.pack()

        # Adiciona logo dentro do frame com logs detalhados
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        logger.info(f"Tentando localizar o logo em: {logo_path}")
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                logger.info("Logo encontrado e carregado com sucesso.")
                img = img.resize((80, 80))
                self.logo_img = ImageTk.PhotoImage(img)
                logo_label = tk.Label(frm, image=self.logo_img)
                logo_label.grid(column=0, row=0, columnspan=2, pady=5)
                logger.info("Logo exibido no frame principal.")
                row = 1
            except Exception as e:
                logger.error(f"Erro ao carregar ou exibir o logo: {e}")
                row = 0
        else:
            logger.warning(f"Logo NÃO encontrado em: {logo_path}")
            row = 0

        # Campos de entrada
        for label, var in self.campos.items():
            label_text = label.replace("_", " ").capitalize()
            ttk.Label(frm, text=label_text).grid(column=0, row=row, sticky=tk.W, pady=2)
            ttk.Entry(frm, textvariable=var).grid(column=1, row=row, pady=2)
            row += 1

        # Opção de importação
        ttk.Label(frm, text="Importar parâmetros de:").grid(column=0, row=row, sticky=tk.W, pady=5)
        ttk.Radiobutton(frm, text="TXT", variable=self.tipo_importacao_var, value="txt").grid(column=1, row=row, sticky=tk.W)
        row += 1
        ttk.Radiobutton(frm, text="YAML", variable=self.tipo_importacao_var, value="yaml").grid(column=1, row=row, sticky=tk.W)
        row += 1
        ttk.Radiobutton(frm, text="Excel", variable=self.tipo_importacao_var, value="excel").grid(column=1, row=row, sticky=tk.W)
        row += 1

        ttk.Button(frm, text="Importar Parâmetros", command=self.importar_parametros).grid(column=0, row=row, pady=10)
        ttk.Button(frm, text="Simular", command=self.executar_simulacao).grid(column=1, row=row, pady=10)
        row += 1
        ttk.Button(frm, text="Exportar PDF", command=self.exportar_pdf).grid(column=0, columnspan=2, pady=5)
        row += 1
        ttk.Button(frm, text="Sair", command=self.root.destroy).grid(column=0, columnspan=2, pady=5)

        self.resultado_simulacao = None

    def importar_parametros(self):
        tipo = self.tipo_importacao_var.get()
        if tipo == "txt":
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not file_path:
                return
            dados = importar_dados_txt(file_path)
        elif tipo == "yaml":
            file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml;*.yml")])
            if not file_path:
                return
            try:
                dados = importar_dados_yaml(file_path)
            except Exception as e:
                logger.error(f"Erro ao importar YAML: {e}")
                messagebox.showerror("Erro", f"Erro ao importar YAML: {e}")
                return
        elif tipo == "excel":
            file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
            if not file_path:
                return
            try:
                dados = importar_dados_excel(file_path)
            except Exception as e:
                logger.error(f"Erro ao importar Excel: {e}")
                messagebox.showerror("Erro", f"Erro ao importar Excel: {e}")
                return
        else:
            messagebox.showerror("Erro", "Tipo de importação não suportado.")
            return

        if dados:
            for k, v in dados.items():
                if k in self.campos:
                    self.campos[k].set(v)
            logger.info(f"Dados importados ({tipo}) aplicados aos campos: {file_path}")
            messagebox.showinfo("Importação", "Dados importados com sucesso!")
        else:
            logger.error("Falha ao importar dados.")
            messagebox.showerror("Erro", "Falha ao importar dados.")

    def executar_simulacao(self):
        try:
            parametros = {chave: var.get() for chave, var in self.campos.items()}
            # Validação do tempo máximo de simulação (12h = 720 min)
            if parametros["tempo_total_simulacao"] > 720:
                parametros["tempo_total_simulacao"] = 720
                self.campos["tempo_total_simulacao"].set(720)
                messagebox.showwarning(
                    "Limite de tempo",
                    "O tempo máximo de simulação é 12 horas (720 minutos). O valor foi ajustado automaticamente."
                )
            logger.info(f"Executando simulação com parâmetros: {parametros}")
            layout = []  # Adapte se quiser usar um layout ASCII
            self.resultado_simulacao = executar_simulacao(parametros, layout)
            resultado_str = "\n".join(f"{k}: {v}" for k, v in self.resultado_simulacao.items())
            logger.info(f"Resultado da simulação: {self.resultado_simulacao}")
            messagebox.showinfo("Resultado da Simulação", resultado_str)
        except Exception as e:
            logger.error(f"Erro na simulação: {e}")
            messagebox.showerror("Erro", f"Erro na simulação: {e}")
            
    def exportar_pdf(self):
        if not self.resultado_simulacao:
            logger.warning("Tentativa de exportar PDF sem simulação realizada.")
            messagebox.showwarning("Exportar PDF", "Realize uma simulação antes de exportar o PDF.")
            return
        caminho_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not caminho_pdf:
            return
        try:
            exportar_pdf(self.resultado_simulacao, caminho_pdf)
            logger.info(f"Relatório PDF exportado: {caminho_pdf}")
            messagebox.showinfo("Exportar PDF", f"Relatório PDF gerado em:\n{caminho_pdf}")
        except Exception as e:
            logger.error(f"Erro ao exportar PDF: {e}")
            messagebox.showerror("Erro", f"Erro ao exportar PDF: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorGUI(root)
    root.mainloop()