<p align="center">
  <img src="assets/imagens/capa.png" alt="Capa do Livro" width="510"/>
</p>

## Simulação Estocástica de Processos de Fluxo (DES) — Case de Engenharia de Processos Aplicada

Este repositório apresenta um **motor de Simulação por Eventos Discretos (Discrete-Event Simulation — DES)** para sistemas de fluxo com capacidade finita, filas e ocupação. O “restaurante” é usado como **ambiente análogo** para um problema de Engenharia de Processos: maximizar **throughput** (vazão de saída) sob restrições de recursos, minimizando **holdup** (acúmulo/inventário em processo) e tempos de ciclo.

## Introdução — Simulação Estocástica de Processos de Fluxo

O objeto aqui não é o comércio, e sim o **processo**: um conjunto de operações conectadas por transferências, com alimentação variável e capacidades limitantes. A simulação DES permite observar comportamento transiente, saturação, formação de filas e regimes de pico — fenômenos que, em plantas industriais, determinam estabilidade operacional e eficiência.

### Reenquadramento do objeto (The Process Thinking)

- **Fluxo de Clientes = Vazão de Alimentação (Feed Rate)**: taxa de chegada \(\lambda\) e sua variabilidade representam a alimentação do sistema.
- **Buffets e Caixas = Operações Unitárias / Reatores (Unit Operations)**: recursos com tempos de serviço e capacidades finitas, análogos a etapas de processamento.
- **Tempo de Refeição = Tempo de Residência (Residence Time)**: permanência no “volume de processo” (mesas) análoga à residência em equipamentos contínuos.
- **Gargalos de Fila = Limitações de Transferência de Massa/Momento**: filas emergem quando a “capacidade de transferência” entre etapas é inferior à alimentação; o gargalo passa a governar o throughput global.

### Destaque do fundo de Engenharia Química

O software explora a mesma lógica aplicada em **dimensionamento e melhoria de plantas**:

- **Maximização de throughput** via avaliação de cenários de capacidade e restrições.
- **Minimização de holdup/WIP** (acúmulo de pessoas/material) reduzindo filas e tempos totais de ciclo.
- **Distribuições estocásticas** para prever dispersão e risco (caudas), pilar do controle estatístico e da análise de variabilidade em processos.

## Metodologia — filas e ocupação como balanços de inventário

Em Python, o sistema é modelado por eventos (chegada, entrada/saída de fila, início/fim de serviço, alocação/liberação de recurso). As filas funcionam como **inventários intermediários** (buffers), e o layout ASCII funciona como uma “planta” espacial que influencia roteamento e restrições.

Para uma comparação direta entre **simulação determinística** e **DES estocástico**, veja `SIMULATING.md`.

## Resultados — identificação de gargalos e otimização de layout industrial

As saídas (tempo em fila, ocupação, utilização de recursos, gargalos) permitem:

- identificar a operação limitante do throughput;
- quantificar holdup máximo e médio;
- comparar rearranjos de layout e paralelização de recursos;
- justificar mudanças de capacidade com evidência (relatórios e gráficos).

## Evolução Tecnológica

Este TCC foi utilizado como **Prova de Conceito (PoC)** para simuladores mais complexos (ex.: **Hidrometalurgia Seletiva — Projeto ETE / Terras Raras**), demonstrando que a lógica de **Balanço de Massa e Tempo** é universal: entidades atravessam operações unitárias, acumulam em buffers e são governadas por gargalos e variabilidade.

---

## Capacidades do motor (funcionalidades)

- Simulação completa do **fluxo de entidades** (clientes) em DES: chegada, filas (buffers), ocupação (residência), operações unitárias (buffet/caixa) e saída
- Entrada de parâmetros via planilha Excel (.xlsx), arquivo YAML (.yaml/.yml), arquivo texto (.txt) ou manualmente pela interface
- Leitura e interpretação de **layout em ASCII** (.txt) como “planta”/arranjo físico do processo
- Configuração de variáveis como feed rate (clientes/min), tempos médios e variabilidade, capacidades e layout físico
- Geração automática de relatórios finais em PDF com estatísticas, gráficos e visualização do layout
- Criação de animações (GIF) do comportamento do sistema ao longo do tempo
- Interface gráfica intuitiva e fácil de usar (Tkinter)
- Exportação de logs detalhados de execução e erros para acompanhamento e auditoria

---

## Requisitos do sistema

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

## Instalação

1. Instale o Python: [python.org/downloads](https://www.python.org/downloads/)
2. Instale as dependências no terminal:
   ```sh
   pip install -r requirements.txt
   ```

---

## Configuração inicial

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

- Edite ou escolha um layout ASCII em `layouts/layout_padrao.txt` para definir a disposição física do sistema (operações unitárias, áreas de residência e caminhos).

---

## Layout (planta ASCII) e variáveis de processo

O layout é definido por um arquivo ASCII (texto simples), onde cada caractere representa um elemento físico do ambiente (operações unitárias, áreas de residência, barreiras e corredores). Esse layout é determinante para a simulação, pois condiciona o roteamento e a disponibilidade de recursos.

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

### Variáveis (parâmetros de processo)

As principais variáveis relacionadas ao layout e à simulação são:

- **clientes_por_minuto**: vazão de alimentação (feed rate) do sistema.
- **tempo_medio_almoco**: tempo de residência médio.
- **variabilidade_chegada / variabilidade_almoco**: dispersão estocástica associada aos tempos.
- **cadeiras_por_mesa / numero_de_mesas**: capacidade da área de residência (holdup “físico”).
- **numero_caixas / tempo_medio_atendimento**: capacidade e tempo de serviço de uma operação unitária crítica (quando configurado).
- **capacidade_maxima_fila**: limite de buffer/inventário intermediário.
- **layout_fisico**: arquivo ASCII que representa a disposição de operações e caminhos.

Essas variáveis podem ser ajustadas nos arquivos de configuração (YAML, Excel, TXT) ou diretamente pela interface gráfica, permitindo simular diferentes cenários e layouts para análise de desempenho e identificação de gargalos.

---

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando abaixo para iniciar o simulador:
   ```sh
   python main.py
   ```
3. Na interface gráfica, você poderá:
   - Importar os parâmetros de simulação (YAML, Excel, TXT ou manual)
  - Importar ou editar o layout do sistema
   - Executar a simulação
   - Visualizar os resultados e estatísticas
   - Exportar o relatório PDF e o GIF animado

4. Os arquivos gerados (relatórios e animações) serão salvos automaticamente em:
   `resultados/relatorios/`

---

## Estrutura de pastas

```plaintext
tcc_python/
│
├── main.py                # Ponto de entrada da aplicação
├── config/                # Parâmetros de simulação
│   └── parametros.yaml
├── layouts/               # Layouts ASCII do sistema
│   └── layout_padrao.txt
├── monitoramento/         # Logs de execução e erros
│   └── log_execucao.log
├── resultados/            # Relatórios e animações gerados
│   └── relatorios/
│       ├── YYYY_MM_DD_HH_MM_SS_resultado_simulacao.pdf    # Relatório PDF gerado pela simulação
│       ├── YYYY_MM_DD_HH_MM_SS_layout_da_simulacao.pdf    # PDF do layout ASCII do sistema
│       └── YYYY_MM_DD_HH_MM_SS_layout_animacao.gif        # GIF animado do layout do sistema
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
```

---

## Descrição dos arquivos principais

- **main.py**: Ponto de entrada da aplicação. Integra interface gráfica, simulação, importação de dados e exportação de relatórios.
- **src/interface.py**: Interface gráfica (Tkinter) para entrada de dados e interação do usuário.
- **src/simulador.py**: Lógica central da simulação por eventos discretos. Calcula estatísticas e resultados.
- **src/visualizador_layout.py**: Geração das imagens (frames) e do GIF do layout do sistema durante a simulação.
- **src/yaml_loader.py**: Importação dos parâmetros de simulação a partir de arquivos YAML.
- **src/excel_loader.py**: Importação dos parâmetros de simulação a partir de planilhas Excel.
- **src/layout_parser.py**: Leitura e análise do layout ASCII (operações unitárias, áreas de residência e caminhos).
- **src/pdf_exporter.py**: Geração do relatório PDF com gráficos, layout, parâmetros, resultados e recomendações.
- **src/layout_pdf_exporter.py**: Exportação do layout ASCII em PDF separado.
- **src/logger_config.py**: Configuração do sistema de logging (logs de execução e erros).
- **src/logo.png**: Imagem da logo exibida na interface gráfica.
- **monitoramento/log_execucao.log**: Arquivo de log das execuções.
- **resultados/relatorios/resultado_simulacao.pdf**: Relatório PDF gerado pela simulação.
- **resultados/relatorios/layout_animacao.gif**: GIF gerado durante a simulação, mostrando o comportamento do sistema ao longo do tempo.
- **layouts/layout_padrao.txt**: Exemplo de layout ASCII do sistema.

---

## Estatística e análise (métricas de processo)

O simulador gera estatísticas operacionais para identificar gargalos, dimensionar recursos e comparar cenários de layout/capacidade. Entre as principais análises estão:

- **Tempo de residência**: tempo médio no sistema (do feed à saída).
- **Utilização de recursos**: ocupação de operações unitárias e áreas de residência.
- **Tempo em filas (buffers)**: espera por capacidade em etapas críticas.
- **Perfil temporal de alimentação/saída**: regimes de pico, transientes e saturação.
- **Identificação de gargalos**: etapas onde ocorrem maiores atrasos/holdup e que dominam o throughput global.

Os resultados são apresentados em relatórios PDF com gráficos, tabelas e visualizações do layout, facilitando a tomada de decisão e o planejamento de melhorias no processo.

---

## Gráficos e visualizações

Durante e após a simulação, o sistema gera gráficos e visualizações para facilitar a leitura do comportamento do processo. Entre os principais recursos estão:

- **Gráficos de throughput**: saída ao longo do tempo, evidenciando regimes de pico e saturação.
- **Gráficos de ocupação/utilização**: taxa de ocupação de recursos ao longo da simulação.
- **Gráficos de tempos de fila**: espera média por etapa (buffers).
- **Visualização do layout**: o layout ASCII é exportado em PDF e animado em GIF, ilustrando movimentação e utilização ao longo do tempo.

Essas visualizações são incluídas automaticamente nos relatórios PDF e nos arquivos GIF gerados, tornando a análise mais intuitiva e completa.

---

## Resultados e relatórios

- O relatório PDF será salvo em `resultados/relatorios/`.
- O relatório inclui:
    - Resumo dos parâmetros e resultados
    - Gráficos de throughput/ocupação/filas (conforme cenário)
    - Visualização do layout do sistema
    - Legenda dos símbolos do layout

---

## Diagrama de sequência (resumo)

```plaintext
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
```

---

## Licença

Este software é distribuído sob a Licença MIT.

Você pode usar, modificar, integrar, distribuir e comercializar este sistema livremente, desde que mantenha os créditos originais ao(s) autor(es) conforme especificado na licença.

---

## Referências bibliográficas

- BALLOU, Ronald H. Logística empresarial: transportes, administração de materiais e distribuição física. 1. ed. São Paulo: Atlas, 2006.
- BANKS, Jerry et al. Discrete-event system simulation. 5. ed. Upper Saddle River: Pearson, 2010.
- LAURINDO, Fernando José Barbin; CARVALHO, Marly Monteiro de. Sistemas de informação: planejamento e alinhamento estratégico nas organizações. São Paulo: Atlas, 2012.
- LAW, Averill M.; KELTON, W. David. Simulation modeling and analysis. 5. ed. New York: McGraw-Hill, 2015.
- PIDD, Michael. Computer simulation in management science. 5. ed. Chichester: Wiley, 2004.
- SILVA, José Carlos de Souza; OLIVEIRA, Flávio Soares Corrêa da. Teoria das filas: fundamentos e aplicações. 2. ed. Rio de Janeiro: Elsevier, 2006.
- SOUZA, César Alexandre de; CUNHA, Cláudio Barbosa da. Gestão de operações em serviços. São Paulo: Atlas, 2012.
- SOUZA, Ricardo de. Python para desenvolvedores. 3. ed. Rio de Janeiro: Novatec, 2019.

---

## Dicas e suporte

- Para alterar roteamento e restrições espaciais, edite o layout ASCII.
- Para dúvidas ou problemas, consulte o log em `monitoramento/log_execucao.log`.
- Para suporte, contate o autor ou consulte a documentação interna.
---

## Contato

**Autor:** Christian Vladimir Uhdre Mulato  
**E-mail:** chmulato(at)hotmail(dot)com
**Última atualização:** 28/05/2025

---
