# 🍽️ Simulador de Tempo de Permanência em Restaurantes

Este sistema permite simular, de forma visual e estatística, o tempo de permanência dos clientes em um restaurante. O simulador considera o fluxo de clientes desde a chegada, passando por filas, ocupação de mesas, uso de buffets e caixas, até a saída. Com base em parâmetros configuráveis e no layout físico do restaurante, o sistema calcula tempos médios, gargalos e estatísticas de atendimento, gerando relatórios completos em PDF e animações do funcionamento do restaurante.

---

## 📌 Funcionalidades

- Simulação completa do fluxo de clientes: chegada, filas, ocupação de mesas, uso de buffets, caixas e saída
- Entrada de parâmetros via planilha Excel (.xlsx), arquivo YAML (.yaml/.yml), arquivo texto (.txt) ou manualmente pela interface
- Leitura e interpretação do layout do restaurante em formato ASCII (.txt)
- Configuração de variáveis como número de clientes por minuto, tempo médio de refeição, capacidade de mesas/cadeiras e layout físico
- Geração automática de relatórios finais em PDF com estatísticas, gráficos e visualização do layout
- Criação de animações (GIF) do funcionamento do restaurante durante a simulação
- Interface gráfica intuitiva e fácil de usar (Tkinter)
- Exportação de logs detalhados de execução e erros para acompanhamento e auditoria

---

## ⚙️ Requisitos do Sistema

- Python 3.8 ou superior instalado
- Sistema operacional Windows (recomendado), mas compatível com Linux e MacOS
- Bibliotecas Python necessárias:
  - `reportlab` (geração de PDFs)
  - `matplotlib` (gráficos)
  - `pillow` (imagens/GIF)
  - `openpyxl` (planilhas Excel)
  - `pyyaml` (YAML)
  - `graphviz` (opcional, para diagramas)
- Tkinter (interface gráfica):
  - Já incluso no Python para Windows/Mac
  - No Linux, instale com: `sudo apt-get install python3-tk`
- Recomendado: ambiente virtual Python para isolar dependências

---

## 🛠️ Instalação

1. Instale o Python: https://www.python.org/downloads/
2. Instale as dependências no terminal:
   ```sh
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuração Inicial

Você pode definir os parâmetros da simulação utilizando um dos formatos abaixo:

- **Arquivo YAML** (exemplo: `config/parametros.yaml`)
- **Planilha Excel (.xlsx)** com colunas `parametro` e `valor`
- **Arquivo texto (.txt)** no formato `parametro: valor` por linha
- **Entrada manual** pela interface gráfica

**Exemplo de planilha Excel:**

| parametro               | valor   |
|-------------------------|---------|
| clientes_por_minuto     | 12      |
| tempo_medio_almoco      | 30      |
| cadeiras_por_mesa       | 4       |

**Exemplo de arquivo TXT:**
clientes_por_minuto: 12  
tempo_medio_almoco: 30  
cadeiras_por_mesa: 4

- Edite ou escolha um layout ASCII em `layouts/layout_padrao.txt` para definir a disposição física do restaurante.

---

## 🗺️ Layout do Restaurante e Variáveis

O layout do restaurante é definido por um arquivo ASCII (texto simples), onde cada caractere representa um elemento físico do ambiente, como mesas, cadeiras, buffets, caixas, paredes e corredores. Esse layout é fundamental para a simulação, pois determina o fluxo dos clientes e a disposição dos recursos.

### Exemplo de layout ASCII (`layouts/layout_padrao.txt`):

```
###########
# M M B C #
# M M B C #
#         #
###########
```
Legenda dos símbolos:
- `#` : Parede
- `M` : Mesa
- `B` : Buffet
- `C` : Caixa
- Espaço em branco: Corredor/caminho livre

### Variáveis do Layout

As principais variáveis relacionadas ao layout e à simulação são:

- **clientes_por_minuto**: Quantidade média de clientes que chegam ao restaurante por minuto.
- **tempo_medio_almoco**: Tempo médio (em minutos) que cada cliente permanece no restaurante.
- **cadeiras_por_mesa**: Número de cadeiras disponíveis em cada mesa.
- **quantidade_de_mesas**: Número total de mesas no layout.
- **quantidade_de_buffets**: Número de buffets disponíveis.
- **quantidade_de_caixas**: Número de caixas para pagamento.
- **capacidade_buffet**: Quantidade máxima de clientes que podem se servir simultaneamente no buffet.
- **capacidade_caixa**: Quantidade máxima de clientes atendidos simultaneamente no caixa.
- **layout_fisico**: Arquivo ASCII que representa a disposição dos elementos do restaurante.

Essas variáveis podem ser ajustadas nos arquivos de configuração (YAML, Excel, TXT) ou diretamente pela interface gráfica, permitindo simular diferentes cenários e layouts para análise de desempenho e identificação de gargalos.

---

## ▶️ Como Executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando abaixo para iniciar o simulador:
   ```sh
   python main.py
   ```
3. Na interface gráfica, você poderá:
   - Importar os parâmetros de simulação (YAML, Excel, TXT ou manual)
   - Importar ou editar o layout do restaurante
   - Executar a simulação
   - Visualizar os resultados e estatísticas
   - Exportar o relatório PDF e o GIF animado

4. Os arquivos gerados (relatórios e animações) serão salvos automaticamente em:
   `resultados/relatorios/`

---

## 📁 Estrutura de Pastas

```
simulador_restaurante/
│
├── main.py                # Ponto de entrada da aplicação
├── config/                # Parâmetros de simulação
│   └── parametros.yaml
├── layouts/               # Layouts ASCII do restaurante
│   └── layout_padrao.txt
├── monitoramento/         # Logs de execução e erros
│   └── log_execucao.log
├── resultados/            # Relatórios e animações gerados
│   └── relatorios/
│       ├── YYYY_MM_DD_HH_MM_SS_resultado_simulacao.pdf    # Relatório PDF gerado pela simulação
│       ├── YYYY_MM_DD_HH_MM_SS_layout_da_simulacao.pdf    # PDF do layout ASCII do restaurante
│       └── YYYY_MM_DD_HH_MM_SS_layout_animacao.gif        # GIF animado do layout do restaurante
├── src/
│   ├── interface.py               # Interface gráfica principal (Tkinter)
│   ├── simulador.py               # Lógica central da simulação
│   ├── visualizador_layout.py     # Geração dos frames e GIF animado do layout
│   ├── yaml_loader.py             # Leitura de parâmetros YAML
│   ├── excel_loader.py            # Leitura de parâmetros Excel
│   ├── layout_parser.py           # Leitura/análise do layout ASCII
│   ├── pdf_exporter.py            # Geração de relatórios PDF
│   ├── layout_pdf_exporter.py     # Exportação do layout ASCII em PDF separado
│   ├── logger_config.py           # Configuração do sistema de logging
│   └── logo.png                   # Imagem da logo exibida na interface gráfica
├── requirements.txt               # Lista de dependências Python
└── README.md                      # Este arquivo de documentação

---

## 📚 Descrição dos Arquivos Principais

- **main.py**: Ponto de entrada da aplicação. Integra interface gráfica, simulação, importação de dados e exportação de relatórios.
- **src/interface.py**: Interface gráfica (Tkinter) para entrada de dados e interação do usuário.
- **src/simulador.py**: Lógica central da simulação por eventos discretos. Calcula estatísticas e resultados.
- **src/visualizador_layout.py**: Responsável pela geração das imagens dos frames e do GIF animado do layout do restaurante durante a simulação.
- **src/yaml_loader.py**: Importação dos parâmetros de simulação a partir de arquivos YAML.
- **src/excel_loader.py**: Importação dos parâmetros de simulação a partir de planilhas Excel.
- **src/layout_parser.py**: Leitura e análise do layout ASCII do restaurante (mesas, caixas, buffets).
- **src/pdf_exporter.py**: Geração do relatório PDF com gráficos, layout, parâmetros, resultados e recomendações.
- **src/layout_pdf_exporter.py**: Exportação do layout ASCII em PDF separado.
- **src/logger_config.py**: Configuração do sistema de logging (logs de execução e erros).
- **src/logo.png**: Imagem da logo exibida na interface gráfica.
- **monitoramento/log_execucao.log**: Arquivo de log das execuções.
- **resultados/relatorios/resultado_simulacao.pdf**: Relatório PDF gerado pela simulação.
- **resultados/relatorios/layout_animacao.gif**: GIF animado gerado durante a simulação, mostrando o funcionamento do restaurante ao longo do tempo.
- **layouts/layout_padrao.txt**: Exemplo de layout ASCII do restaurante.

---

## 📊 Estatística e Análise

O simulador gera estatísticas detalhadas sobre o funcionamento do restaurante, permitindo identificar gargalos, otimizar recursos e melhorar o atendimento. Entre as principais análises disponíveis estão:

- **Tempo médio de permanência dos clientes**: Mede quanto tempo, em média, cada cliente permanece no restaurante do momento da chegada até a saída.
- **Taxa de ocupação das mesas**: Indica o percentual de utilização das mesas ao longo da simulação.
- **Tempo médio em filas**: Mostra quanto tempo os clientes aguardam em filas para buffet, mesas e caixas.
- **Capacidade e utilização dos buffets e caixas**: Analisa se há sobrecarga ou ociosidade nesses pontos do restaurante.
- **Distribuição do fluxo de clientes**: Permite visualizar horários de pico e períodos de menor movimento.
- **Identificação de gargalos**: Aponta etapas do processo onde ocorrem maiores atrasos ou acúmulo de clientes.

Os resultados são apresentados em relatórios PDF com gráficos, tabelas e visualizações do layout, facilitando a tomada de decisão e o planejamento de melhorias no restaurante.

---

## 📊 Gráficos e Visualizações

Durante e após a simulação, o sistema gera diversos gráficos e visualizações para facilitar a análise dos resultados e o entendimento do funcionamento do restaurante. Entre os principais recursos estão:

- **Gráficos de atendimento**: Mostram o número de clientes atendidos ao longo do tempo, permitindo identificar horários de pico e períodos de menor movimento.
- **Gráficos de ocupação**: Exibem a taxa de ocupação das mesas, buffets e caixas durante a simulação.
- **Gráficos de tempo em filas**: Apresentam o tempo médio de espera dos clientes em cada etapa do processo (buffet, mesas, caixas).
- **Visualização do layout**: O layout ASCII do restaurante é apresentado em PDF e animado em GIF, ilustrando a movimentação dos clientes e a utilização dos recursos ao longo do tempo.
- **Animação (GIF)**: Demonstra visualmente o fluxo dos clientes no restaurante, facilitando a identificação de gargalos e o entendimento do comportamento do sistema.

Essas visualizações são incluídas automaticamente nos relatórios PDF e nos arquivos GIF gerados, tornando a análise mais intuitiva e completa.

---

## 📈 Resultados e Relatórios

- O relatório PDF será salvo em `resultados/relatorios/`.
- O relatório inclui:
    - Resumo dos parâmetros e resultados
    - Gráficos de atendimento
    - Visualização do layout do restaurante
    - Legenda dos símbolos do layout

---

## 🔄 Diagrama de Sequência (Resumo)

Usuário
  |
  v
[main.py]                # Inicia a aplicação
  |
  v
[interface.py]           # Interface gráfica (Tkinter)
  |        (importa parâmetros)
  |-----> [yaml_loader.py] / [excel_loader.py] / importar_dados_txt
  |<----- parâmetros
  |
  |        (importa layout ASCII)
  |-----> [layout_parser.py]
  |<----- layout
  |
  |        (executa simulação)
  |-----> [simulador.py]
  |           |
  |           |---> [logger_config.py]           # Logging de execução/erros
  |           |---> [pdf_exporter.py]            # Geração do relatório PDF
  |           |         |
  |           |         |---> [layout_pdf_exporter.py]   # Exporta layout em PDF
  |           |         |---> [logger_config.py]         # Logging do PDF
  |           |<--------|
  |           |
  |<---------- resultado
  |
  v
Relatórios e animações gerados em resultados/relatorios/

---

## 📄 Licença

Este software é distribuído sob a Licença MIT.

Você pode usar, modificar, integrar, distribuir e comercializar este sistema livremente, desde que mantenha os créditos originais ao(s) autor(es) conforme especificado na licença.

---

## 📚 Referências Bibliográficas

- BALLOU, Ronald H. Logística empresarial: transportes, administração de materiais e distribuição física. 1. ed. São Paulo: Atlas, 2006.
- BANKS, Jerry et al. Discrete-event system simulation. 5. ed. Upper Saddle River: Pearson, 2010.
- LAURINDO, Fernando José Barbin; CARVALHO, Marly Monteiro de. Sistemas de informação: planejamento e alinhamento estratégico nas organizações. São Paulo: Atlas, 2012.
- LAW, Averill M.; KELTON, W. David. Simulation modeling and analysis. 5. ed. New York: McGraw-Hill, 2015.
- PIDD, Michael. Computer simulation in management science. 5. ed. Chichester: Wiley, 2004.
- SILVA, José Carlos de Souza; OLIVEIRA, Flávio Soares Corrêa da. Teoria das filas: fundamentos e aplicações. 2. ed. Rio de Janeiro: Elsevier, 2006.
- SOUZA, César Alexandre de; CUNHA, Cláudio Barbosa da. Gestão de operações em serviços. São Paulo: Atlas, 2012.
- SOUZA, Ricardo de. Python para desenvolvedores. 3. ed. Rio de Janeiro: Novatec, 2019.

---

## 💡 Dicas e Suporte

- Para alterar o fluxo do cliente, edite o layout ASCII.
- Para dúvidas ou problemas, consulte o log em `monitoramento/log_execucao.log`.
- Para suporte, contate o autor ou consulte a documentação interna.
---

## 📞 Contato

**Autor:** Christian Vladimir Uhdre Mulato  
**E-mail:** chmulato(at)hotmail(dot)com
**Última atualização:** 28/05/2025

---
