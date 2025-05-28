# ===============================================
# Copyright (c) 2025 Christian Vladimir Uhdre Mulato
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# ===============================================
# Projeto: Simulador de Tempo de Permanência em Restaurantes
# Módulo: interface.py
# Descrição:
#   Este módulo implementa a interface gráfica da aplicação
#   utilizando Tkinter. Permite entrada de dados manuais ou
#   importação de arquivos para simulação.
#
# Funcionalidades:
#   - Campos para entrada de parâmetros
#   - Botão de importação de configuração YAML ou Excel
#   - Botão de importação de layout ASCII
#   - Execução da simulação e geração de relatório PDF
#   - Exportação de resultado
#
# Dependências Python:
#   - tkinter (padrão da biblioteca Python)
#   - os (padrão da biblioteca Python)
#   - src.simulador (lógica da simulação)
#   - src.layout_parser (leitura do layout)
#   - src.logger_config (logger do sistema)
#   - src.yaml_loader (importação de YAML)
#   - src.excel_loader (importação de Excel)
#   - src.pdf_exporter (geração de PDF)
#   - src.layout_pdf_exporter (geração de PDF do layout ASCII)
#
# Autor: Christian Mulato
# Data: 27/05/2025
# ===============================================

import tkinter as tk
from tkinter import filedialog, messagebox
from src.simulador import executar_simulacao
from src.layout_parser import ler_layout_ascii, identificar_elementos
from src.logger_config import get_logger
from src.yaml_loader import importar_dados_yaml
from src.excel_loader import importar_dados_excel
from src.pdf_exporter import exportar_pdf
from src.layout_pdf_exporter import exportar_layout_ascii_para_pdf
import os

logger = get_logger()

class AplicacaoSimulador:
    def __init__(self, root, callbacks=None):
        self.root = root
        self.root.configure(bg="#f9f9f9")
        self.layout = None
        self.parametros = {}
        self.callbacks = callbacks or {}

        # Variáveis de interface
        self.qtd_pessoas_var = tk.StringVar()
        self.tempo_medio_refeicao_var = tk.StringVar()
        self.cadeiras_por_mesa_var = tk.StringVar()
        self.numero_de_mesas_var = tk.StringVar()
        self.tempo_total_simulacao_var = tk.StringVar()
        self.numero_caixas_var = tk.StringVar()  # Prioriza layout

        # Novo: variável para escolha do tipo de importação
        self.tipo_importacao_var = tk.StringVar(value="yaml")

        logger.info("Interface gráfica inicializada.")
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.root, text="Simulador de Permanência", font=("Helvetica", 16, "bold"), bg="#f9f9f9").pack(pady=10)

        entrada_frame = tk.Frame(self.root, bg="#f9f9f9")
        entrada_frame.pack(pady=10)

        tk.Label(entrada_frame, text="Clientes por minuto:", bg="#f9f9f9").grid(row=0, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.qtd_pessoas_var).grid(row=0, column=1)

        tk.Label(entrada_frame, text="Tempo médio de almoço (min):", bg="#f9f9f9").grid(row=1, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.tempo_medio_refeicao_var).grid(row=1, column=1)

        tk.Label(entrada_frame, text="Número de mesas:", bg="#f9f9f9").grid(row=2, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.numero_de_mesas_var).grid(row=2, column=1)

        tk.Label(entrada_frame, text="Cadeiras por mesa:", bg="#f9f9f9").grid(row=3, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.cadeiras_por_mesa_var).grid(row=3, column=1)

        tk.Label(entrada_frame, text="Tempo total da simulação (min):", bg="#f9f9f9").grid(row=4, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.tempo_total_simulacao_var).grid(row=4, column=1)

        tk.Label(entrada_frame, text="Número de caixas:", bg="#f9f9f9").grid(row=5, column=0, sticky="e")
        tk.Entry(entrada_frame, textvariable=self.numero_caixas_var, state="readonly").grid(row=5, column=1)

        # Novo: Frame para escolha do tipo de importação
        tipo_frame = tk.Frame(self.root, bg="#f9f9f9")
        tipo_frame.pack(pady=5)
        tk.Label(tipo_frame, text="Importar parâmetros de:", bg="#f9f9f9").pack(side=tk.LEFT)
        tk.Radiobutton(tipo_frame, text="YAML", variable=self.tipo_importacao_var, value="yaml", bg="#f9f9f9").pack(side=tk.LEFT)
        tk.Radiobutton(tipo_frame, text="Excel", variable=self.tipo_importacao_var, value="excel", bg="#f9f9f9").pack(side=tk.LEFT)

        # Botões de ação
        botoes_frame = tk.Frame(self.root, bg="#f9f9f9")
        botoes_frame.pack(pady=10)

        btn_importar_param = tk.Button(botoes_frame, text="Importar Parâmetros", command=self.importar_parametros)
        btn_importar_param.grid(row=0, column=0, padx=5)

        btn_importar_layout = tk.Button(botoes_frame, text="Importar Layout", command=self.importar_layout)
        btn_importar_layout.grid(row=0, column=1, padx=5)

        self.btn_simular = tk.Button(botoes_frame, text="Simular", command=self.simular, state=tk.DISABLED)
        self.btn_simular.grid(row=0, column=2, padx=5)

        # Entradas para uso externo (main.py)
        self.entradas = {
            "Clientes por minuto:": self.qtd_pessoas_var,
            "Tempo médio de almoço (min):": self.tempo_medio_refeicao_var,
            "Número de mesas:": self.numero_de_mesas_var,
            "Cadeiras por mesa:": self.cadeiras_por_mesa_var,
            "Tempo total da simulação (min):": self.tempo_total_simulacao_var,
            "Número de caixas:": self.numero_caixas_var
        }

    def importar_parametros(self):
        tipo = self.tipo_importacao_var.get()
        if tipo == "yaml":
            caminho = filedialog.askopenfilename(filetypes=[("Arquivos YAML", "*.yaml;*.yml")])
            if caminho:
                try:
                    logger.info(f"Iniciando importação do YAML: {caminho}")
                    self.parametros = importar_dados_yaml(caminho)
                    messagebox.showinfo("Importação", "Dados importados com sucesso!")
                    self.qtd_pessoas_var.set(str(self.parametros.get("clientes_por_minuto", "")))
                    self.tempo_medio_refeicao_var.set(str(self.parametros.get("tempo_medio_almoco", "")))
                    self.cadeiras_por_mesa_var.set(str(self.parametros.get("cadeiras_por_mesa", "")))
                    self.numero_de_mesas_var.set(str(self.parametros.get("numero_de_mesas", "")))
                    self.tempo_total_simulacao_var.set(str(self.parametros.get("tempo_total_simulacao", "")))
                    logger.info(f"Parâmetros importados do YAML: {self.parametros}")
                    logger.info("Ao importar o layout, o número de caixas será priorizado em relação ao YAML ou campos manuais.")
                    self._ativar_simular_se_pronto()
                except Exception as e:
                    logger.error(f"Falha ao importar YAML: {e}")
                    messagebox.showerror("Erro", f"Falha ao importar YAML:\n{e}")
        elif tipo == "excel":
            caminho = filedialog.askopenfilename(filetypes=[("Planilhas Excel", "*.xlsx;*.xls")])
            if caminho:
                try:
                    logger.info(f"Iniciando importação do Excel: {caminho}")
                    self.parametros = importar_dados_excel(caminho)
                    messagebox.showinfo("Importação", "Dados importados com sucesso!")
                    self.qtd_pessoas_var.set(str(self.parametros.get("clientes_por_minuto", "")))
                    self.tempo_medio_refeicao_var.set(str(self.parametros.get("tempo_medio_almoco", "")))
                    self.cadeiras_por_mesa_var.set(str(self.parametros.get("cadeiras_por_mesa", "")))
                    self.numero_de_mesas_var.set(str(self.parametros.get("numero_de_mesas", "")))
                    self.tempo_total_simulacao_var.set(str(self.parametros.get("tempo_total_simulacao", "")))
                    logger.info(f"Parâmetros importados do Excel: {self.parametros}")
                    logger.info("Ao importar o layout, o número de caixas será priorizado em relação ao Excel ou campos manuais.")
                    self._ativar_simular_se_pronto()
                except Exception as e:
                    logger.error(f"Falha ao importar Excel: {e}")
                    messagebox.showerror("Erro", f"Falha ao importar Excel:\n{e}")

    def importar_layout(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos TXT", "*.txt")])
        if caminho:
            try:
                logger.info(f"Iniciando importação do layout: {caminho}")
                self.layout = ler_layout_ascii(caminho)
                elementos = identificar_elementos(self.layout)
                n_caixas = len(elementos.get('caixa', []))
                n_mesas = len(elementos.get('mesas', []))
                n_buffets = len(elementos.get('buffet', []))

                # Validação mínima: pelo menos 1 caixa, 1 mesa, 1 buffet e 1 cadeira
                cadeiras_por_mesa = int(self.cadeiras_por_mesa_var.get() or 0)
                total_cadeiras = n_mesas * cadeiras_por_mesa

                if n_caixas < 1 or n_mesas < 1 or n_buffets < 1 or total_cadeiras < 1:
                    msg = (
                        "O layout deve conter pelo menos:\n"
                        "- 1 caixa (C)\n"
                        "- 1 mesa (M)\n"
                        "- 1 buffet (B)\n"
                        "- 1 cadeira (total de cadeiras > 0)\n"
                        f"Encontrado: Caixas={n_caixas}, Mesas={n_mesas}, Buffets={n_buffets}, Cadeiras={total_cadeiras}"
                    )
                    logger.error(msg)
                    messagebox.showerror("Layout inválido", msg)
                    return

                # Atualiza os campos da interface com base no layout
                self.numero_caixas_var.set(str(n_caixas))
                self.numero_de_mesas_var.set(str(n_mesas))
                logger.info(f"Número de caixas definido pelo layout: {n_caixas} (prioridade sobre YAML ou manual)")
                logger.info(f"Layout importado com sucesso. Mesas: {n_mesas}, Caixas: {n_caixas}, Buffets: {n_buffets}, Cadeiras: {total_cadeiras}")
                messagebox.showinfo(
                    "Layout",
                    f"Layout importado com sucesso!\nMesas: {n_mesas}\nCaixas: {n_caixas}\nBuffets: {n_buffets}\nCadeiras: {total_cadeiras}"
                )
                self._ativar_simular_se_pronto()
            except Exception as e:
                logger.error(f"Falha ao importar layout: {e}")
                messagebox.showerror("Erro", f"Falha ao importar layout:\n{e}")

    def _ativar_simular_se_pronto(self):
        # Ativa o botão Simular se todos os dados estiverem carregados
        if self.qtd_pessoas_var.get() and self.tempo_medio_refeicao_var.get() and \
           self.cadeiras_por_mesa_var.get() and self.numero_de_mesas_var.get() and \
           self.tempo_total_simulacao_var.get() and self.numero_caixas_var.get() and self.layout:
            self.btn_simular.config(state=tk.NORMAL)

    def simular(self):
        try:
            clientes_por_minuto = float(self.qtd_pessoas_var.get())
            tempo_medio_almoco = float(self.tempo_medio_refeicao_var.get())
            numero_de_mesas = int(self.numero_de_mesas_var.get())
            cadeiras_por_mesa = int(self.cadeiras_por_mesa_var.get())
            tempo_total_simulacao = int(self.tempo_total_simulacao_var.get())
            numero_caixas = int(self.numero_caixas_var.get())
            if not self.layout:
                logger.warning("Tentativa de simulação sem layout carregado.")
                raise ValueError("Layout não carregado.")

            parametros = {
                'clientes_por_minuto': clientes_por_minuto,
                'tempo_medio_almoco': tempo_medio_almoco,
                'numero_de_mesas': numero_de_mesas,
                'cadeiras_por_mesa': cadeiras_por_mesa,
                'tempo_total_simulacao': tempo_total_simulacao,
                'numero_caixas': numero_caixas
            }
            logger.info(f"Parâmetro 'numero_caixas' priorizado do layout: {numero_caixas}")
            logger.info(f"Executando simulação com parâmetros: {parametros}")
            resultado = executar_simulacao(parametros, self.layout)
            logger.info(f"Resultado da simulação: {resultado}")

            caminho_pdf = "resultados/relatorios/resultado_simulacao.pdf"
            os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
            exportar_pdf(resultado, caminho_pdf, layout_ascii=self.layout)
            logger.info(f"Relatório PDF gerado em: {caminho_pdf}")

            # Exporta o layout ASCII em PDF separado, com logs detalhados
            caminho_layout_pdf = "resultados/relatorios/layout_da_simulacao.pdf"
            os.makedirs(os.path.dirname(caminho_layout_pdf), exist_ok=True)
            logger.info(f"Iniciando exportação do layout ASCII em PDF separado: {caminho_layout_pdf}")
            try:
                exportar_layout_ascii_para_pdf(self.layout, caminho_layout_pdf)
                logger.info(f"Layout ASCII exportado em PDF separado com sucesso: {caminho_layout_pdf}")
            except Exception as e:
                logger.error(f"Erro ao exportar layout ASCII em PDF separado: {e}")

            messagebox.showinfo(
                "Simulação concluída",
                f"Relatório gerado com sucesso!\n\n{caminho_pdf}\n\nLayout ASCII exportado em:\n{caminho_layout_pdf}"
            )
        except Exception as e:
            logger.error(f"Erro na simulação: {e}")
            messagebox.showerror("Erro na Simulação", f"{e}")

def criar_janela_interface(root, callbacks=None):
    """
    Função de fábrica para criar a interface gráfica usando a classe AplicacaoSimulador.
    Retorna o dicionário de entradas e o botão Simular para controle externo.
    """
    app = AplicacaoSimulador(root, callbacks)
    return app.entradas, app.btn_simular

# Para rodar a interface diretamente (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoSimulador(root)
    root.mainloop()