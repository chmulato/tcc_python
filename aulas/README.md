# Trilha de Aulas — Do RU à Engenharia Química (Simulação DES)

> Esta trilha foi escrita para **aprendizagem de adultos** (andragogia): cada aula entrega uma ideia central + uma atividade curta + um desafio reprodutível no simulador.

## Onde está o “portal” publicado (GitHub Pages)

O GitHub Pages deste repositório é servido a partir de `/docs`. Os principais artefatos em HTML ficam em:

- **Paper interativo (home):** `../docs/index.html`
- **Sala Digital (portal):** `../docs/portal.html`
- **TCC (HTML):** `../docs/tcc.html`
- **Guia técnico (Determinística vs DES):** `../docs/SIMULATING.html`
- **README em HTML (site):** `../docs/README.html`

## Como usar (fluxo recomendado)

1) **Leia as aulas em ordem** (Aula 01 → 06).  
2) **Em cada aula**, faça:
   - **Atividade (em sala)**: 10–15 min (tabela/frase curta).
   - **Desafio de simulação**: 15–30 min (mudar 1 variável, medir 2–3 métricas, escrever conclusão).
3) Para evidências visuais (figuras do case), gere:

```bash
python scripts/gerar_figuras.py
```

As saídas ficam em `../docs/figuras/`.

> **Regra de ouro (reprodutibilidade):** anote sempre **(a)** qual arquivo de parâmetros você usou (`config/parametros.yaml`, Excel, etc.), **(b)** qual layout (`layouts/*.txt`) e **(c)** quais valores você alterou.

## Aulas (progressão do simples ao complexo)

| Aula | Tema | Resultado de aprendizagem (1 linha) |
|---:|---|---|
| 01 | Sistemas e fluxo | separar **entrada → processo → saída** e reconhecer acúmulo (fila/ocupação) |
| 02 | Filas e gargalos | entender por que acumula quando **λ** supera **μ** e quando a variabilidade “explode” filas |
| 03 | Conservação (balanço) | usar **Entrada − Saída = Acúmulo** para interpretar gráficos do simulador |
| 04 | Operações unitárias | mapear etapas do restaurante para **unidades** (capacidade, tempo de serviço, residência) |
| 05 | Ponte industrial (ETE/Terras Raras) | traduzir “pessoas ↔ íons” sem perder o rigor conceitual |
| 06 | Decisão baseada em dados | ler gráficos, comparar cenários e justificar intervenção (inclui ROI simples) |

## Leituras de apoio

- **Para ver o case completo e as figuras:** `../docs/index.html`
- **Para navegar como aprendiz (trilha):** `../docs/portal.html`
- **Para entendimento técnico da simulação:** `../docs/SIMULATING.html`

