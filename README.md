# Simulação de Processos Dinâmicos (DES) — Do RU à Engenharia Química

> **Proposta de valor (1 frase):** um motor de **Simulação por Eventos Discretos (DES)** que transforma um sistema real de atendimento (Restaurante Universitário) em um **laboratório reprodutível** para estudar **fluxo, gargalos, filas, throughput, holdup e tempo de residência** — com extrapolação conceitual para plantas industriais.

<p align="center">
  <img src="docs/assets/imagens/capa.png" alt="Capa do projeto" width="640"/>
</p>

---

## Contexto Acadêmico

> **Curso:** Engenharia de Processos  
> **Instituição:** Universidade Microsoft Copilot *(contexto do TCC)*  
> **Autor:** Christian Vladimir Uhdre Mulato  
> **Orientação:** Prof. Copilot, Dr. *(conforme documentação do TCC)*  
> **Ano:** 2025

**Site (GitHub Pages):** [chmulato.github.io/tcc_python](https://chmulato.github.io/tcc_python/)

**Acesso rápido (online):**

- **Paper interativo (home):** [Site / Case](https://chmulato.github.io/tcc_python/)
- **Sala Digital (portal):** [Portal](https://chmulato.github.io/tcc_python/portal.html)
- **Apostila Guia:** [Apostila](https://chmulato.github.io/tcc_python/apostila_guia.html)
- **TCC (HTML):** [Documento](https://chmulato.github.io/tcc_python/tcc.html)
- **Guia técnico (Determinística vs DES):** [Guia](https://chmulato.github.io/tcc_python/SIMULATING.html)
- **README (HTML):** [README](https://chmulato.github.io/tcc_python/README.html)

**Arquivos no repositório (pasta `/docs`):**

- **Paper interativo (site):** `docs/index.html`
- **Sala Digital (portal):** `docs/portal.html`
- **Apostila Guia:** `docs/apostila_guia.html`
- **TCC (HTML):** `docs/tcc.html`
- **Guia técnico (Determinística vs DES):** `docs/SIMULATING.html`
- **README (HTML):** `docs/README.html`

---

## Problemática e Solução (executivo)

**Problema.** Sistemas de fluxo com capacidade finita (serviços ou processos) sofrem com um custo invisível: **gargalos e variabilidade** elevam filas/buffers, degradam nível de serviço e distorcem decisões quando a operação é gerida por médias ou intuição.

**Solução.** Este TCC entrega um **motor DES em Python** que representa o sistema como uma sequência de eventos (chegada, serviço, ocupação, saída), mede métricas operacionais ao longo do tempo e exporta evidências (gráficos/relatórios). O **Restaurante Universitário** funciona como *sandbox* didático para validar, em escala humana, princípios universais de engenharia:

- **Balanço (contabilidade de entidades)**: Entrada − Saída + Geração − Consumo = Acúmulo  
- **Teoria das Filas**: saturação quando **ρ → 1** (λ/μ próximo de 1)  
- **Tempo de residência**: τ ≈ Holdup / Vazão (interpretação operacional)

> “Não gerencie por intuição; simule por precisão.”

---

## Stack Tecnológica (badges)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-0B6B4D)
![Matplotlib](https://img.shields.io/badge/Charts-matplotlib-11557C)
![ReportLab](https://img.shields.io/badge/PDF-reportlab-CC0000)
![Pillow](https://img.shields.io/badge/Images-Pillow-6E56CF)
![OpenPyXL](https://img.shields.io/badge/Excel-openpyxl-1D6F42)
![YAML](https://img.shields.io/badge/Config-YAML-CB171E)
![License: MIT](https://img.shields.io/badge/License-MIT-black)

**Dependências (arquivo base):** `requirements.txt`  

| Componente | Uso no projeto |
|---|---|
| `tkinter` | Interface gráfica (entrada e execução) |
| `pyyaml` / `openpyxl` | Importação de parâmetros (YAML/Excel) |
| `matplotlib` | Gráficos e figuras do estudo de caso |
| `reportlab` | Exportação de relatórios PDF |
| `pillow` / `imageio` | Renderização e animações (GIF/layout) |

---

## Arquitetura da Solução

**Visão arquitetural (camadas).** O projeto segue uma separação prática entre:

- **Entrada/Interface (UI)**: coleta parâmetros e aciona a simulação (`main.py`, `src/interface.py`)
- **Camada de Adaptação (I/O)**: importa parâmetros e layout (`src/yaml_loader.py`, `src/excel_loader.py`, `src/layout_parser.py`)
- **Núcleo de Simulação (engine)**: modela o sistema e calcula métricas (`src/simulador.py`)
- **Saída/Relatórios (exporters)**: PDF, layout, figuras e logs (`src/pdf_exporter.py`, `src/layout_pdf_exporter.py`, `src/logger_config.py`)

```mermaid
flowchart TD
  A[Parâmetros (YAML/Excel/Manual)] --> B[UI (Tkinter)]
  C[Layout ASCII (.txt)] --> B
  B --> D[Núcleo DES (src/simulador.py)]
  D --> E[Métricas: throughput, holdup, filas, residência]
  E --> F[Figuras (docs/figuras)]
  E --> G[PDF (reportlab)]
  E --> H[Logs (monitoramento)]
```

**Módulos principais (responsabilidades):**

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada; integra UI, loaders, engine e exportação |
| `src/simulador.py` | Núcleo DES: eventos, recursos, filas, estatística |
| `src/layout_parser.py` | Leitura e interpretação do layout ASCII |
| `src/yaml_loader.py` / `src/excel_loader.py` | Importação de parâmetros |
| `src/pdf_exporter.py` | PDF executivo (métricas + gráficos + recomendações) |
| `scripts/gerar_figuras.py` | Geração das figuras do estudo de caso para `docs/figuras/` |

---

## Guia de Instalação e Uso (Reproducible Research)

### 1) Pré-requisitos

- **Python 3.8+**
- (Linux) `tkinter`: `sudo apt-get install python3-tk`

### 2) Ambiente virtual (recomendado)

```bash
python -m venv .venv
```

- Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

- Linux/macOS:

```bash
source .venv/bin/activate
```

### 3) Instalação das dependências

```bash
pip install -r requirements.txt
```

> **Reprodutibilidade:** para uma execução totalmente determinística no nível de dependências, recomenda-se registrar um *lock* local após instalar:
>
> ```bash
> pip freeze > requirements.lock.txt
> ```
>
> (este arquivo pode ser anexado como artefato de submissão, se necessário).

### 4) Executar o simulador (GUI)

```bash
python main.py
```

Na interface, você pode:

- importar parâmetros via **YAML** (`config/parametros.yaml`) ou **Excel** (`config/parametros.xlsx`);
- escolher um **layout ASCII** (ex.: `layouts/layout_padrao.txt`);
- executar simulação e exportar relatórios.

### 5) Reproduzir as figuras do estudo de caso

As figuras usadas no site (GitHub Pages) são geradas em **`docs/figuras/`**:

```bash
python scripts/gerar_figuras.py
```

### 6) Observação sobre estocasticidade (reprodutibilidade estatística)

Este projeto realiza simulação **estocástica**. Portanto, mesmo com os mesmos parâmetros, resultados podem variar entre execuções.

Para **reproducibilidade acadêmica**, recomenda-se:

- reportar métricas como **média ± desvio padrão** em múltiplas repetições;
- registrar versão do Python e das dependências (`python --version` + `pip freeze`);
- documentar o cenário (arquivo YAML/Excel e layout ASCII) como artefatos anexos.

---

## Destaques de Implementação (desafios técnicos)

1) **Layout ASCII como “flowsheet espacial”.**  
O layout do RU é tratado como um artefato de engenharia: restrições espaciais influenciam roteamento e capacidade efetiva. Isso permite análises de intervenção (layout/capacidade) com evidência visual.

2) **Separação clara entre engine e I/O.**  
O núcleo de simulação (`src/simulador.py`) é desacoplado dos formatos de entrada (YAML/Excel/TXT) e das saídas (PDF/figuras), facilitando extensão para novos cenários (ex.: ETE / Terras Raras).

3) **Exportação de evidências para decisão.**  
Além de métricas, o projeto exporta artefatos para comunicação técnica: gráficos, figuras e PDFs executivos (importante para validação, auditoria e comunicação do TCC).

---

## Licença e Contato

- **Licença:** MIT (ver `LICENSE`)
- **Autor:** Christian Vladimir Uhdre Mulato  
- **Contato:** chmulato(at)hotmail(dot)com

