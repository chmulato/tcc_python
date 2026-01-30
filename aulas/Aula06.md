# Aula 06 — Operando o Simulador: leitura de gráficos, ROI e decisão baseada em dados

> **Contexto deste repositório:** aqui você usa o simulador do restaurante como um **instrumento de engenharia**
> para justificar intervenções (capacidade/layout/tempo de residência). A mesma disciplina de leitura de dados é a ponte
> para simuladores industriais.

## Guia rápido
- **Tempo estimado**: 35–50 min
- **Pré-requisitos**: Aula 01–05
- **Materiais**:
  - `index.html` (seção “Resultados”)
  - `docs/figuras/fig_04_throughput.png`, `fig_05_ocupacao_e_filas.png`, `fig_06_distribuicao_residencia.png`, `fig_07_antes_depois.png`
  - simulador (`python main.py`) + gerador de figuras (`python scripts/gerar_figuras.py`)

## Objetivo da aula
Aprender a usar o simulador como uma ferramenta de engenharia: **ler gráficos**, diagnosticar gargalos, comparar cenários (antes/depois) e justificar decisões com métricas (incluindo uma noção simples de ROI).

---

## Explicação simples (analogia do dia a dia)
Quando o restaurante fica cheio, o gestor pergunta:

- “Onde está travando?”
- “O que eu ganho se eu colocar mais um caixa?”
- “Vale a pena aumentar mesas ou reduzir tempo de permanência?”

O simulador serve para responder isso sem “chutar”.

[Imagem: painel com 3 gráficos: throughput, fila, distribuição]

Sugestão: abra `index.html` e navegue até **Resultados** para ver as Figuras 3–7 com legenda.

---

## O salto técnico (como engenheiro lê as evidências)

### 1) Throughput (vazão de saída)
Olhe `docs/figuras/fig_04_throughput.png`.

Perguntas técnicas:

- a saída cresce de forma regular ou “em degraus”?
- existem períodos longos com saída baixa? (sinal de gargalo/saturação)

### 2) Holdup e buffers (filas)
Olhe `docs/figuras/fig_05_ocupacao_e_filas.png`.

Leitura:

- holdup alto + fila crescendo → sistema perto/ acima da capacidade.
- fila que cresce “sem voltar” → \(\rho \gtrsim 1\) em algum trecho.

### 3) Distribuição do tempo de residência
Olhe `docs/figuras/fig_06_distribuicao_residencia.png`.

Leitura:

- caudas longas significam risco: algumas entidades demoram muito.
- “média boa” pode esconder caudas ruins.

### 4) Antes vs Depois (intervenção)
Olhe `docs/figuras/fig_07_antes_depois.png`.

Leitura:

- compare métricas de espera, utilização e processados.
- use como argumento para “capex vs benefício”.

---

## Desafio prático (simular e decidir)
1) Rode o simulador com `config/parametros.yaml`.
2) Gere as figuras:

```sh
python scripts/gerar_figuras.py
```

3) Faça uma intervenção e defenda uma decisão:

- Intervenção A: aumentar `numero_caixas`
- Intervenção B: aumentar `numero_de_mesas`
- Intervenção C: reduzir `tempo_medio_almoco` (melhoria operacional)

Escreva um mini relatório (10 linhas):

- **Diagnóstico**: qual é o gargalo provável?
- **Intervenção escolhida**: A/B/C e por quê.
- **Evidências**: cite pelo menos 2 gráficos/figuras.

Para citar figuras do repositório, use os arquivos em `docs/figuras/` (ex.: `fig_04_throughput.png`, `fig_07_antes_depois.png`).

### Bônus: ROI (noção simples)
Sem entrar em contabilidade real, use um ROI simplificado:

1. Defina um “valor por cliente atendido” (ex.: R$ 20).
2. Calcule o ganho: \(\Delta\)clientes_processados × valor
3. Compare com um custo estimado (ex.: caixa extra por turno, ou mais mesas).

O objetivo é treinar o raciocínio: **decisão baseada em dados**, não “achismo”.

---

## Glossário (termos-chave)
- **KPI**: indicador de desempenho (ex.: throughput, tempo de espera).
- **Evidência**: gráfico/métrica que sustenta uma conclusão.
- **Cenário**: conjunto de parâmetros (feed, capacidade, tempos) usado na simulação.
- **Intervenção**: mudança planejada (capacidade, layout, tempo de residência).
- **ROI (Return on Investment)**: retorno aproximado versus custo (simplificado aqui).

---

## Checklist (ao final desta aula, você deve conseguir…)
- interpretar, em linguagem de engenharia, os gráficos de **throughput**, **holdup/filas** e **distribuição de residência**.
- escrever um diagnóstico simples: “gargalo provável é ___ porque ___”.
- comparar cenários e defender uma intervenção usando **2 evidências** (figuras/métricas).
- fazer uma estimativa de ROI simplificada (ganho por clientes processados × custo aproximado).

---

## Navegação
- **Anterior:** [Aula 05 — Hidrometalurgia Seletiva](Aula05.md)
- **Próxima:** fim da trilha (volte ao [README da trilha](README.md))

---

## Próximos passos (ponte conceitual para indústria)
Ao migrar para um contexto industrial (ex.: ETE/Terras Raras), o modo de operar é o mesmo:

- definimos alimentação (vazão/composição),
- definimos operações unitárias (estágios/equipamentos),
- medimos throughput, holdup, residência e variabilidade,
- testamos intervenções e escolhemos a melhor relação desempenho/custo.

