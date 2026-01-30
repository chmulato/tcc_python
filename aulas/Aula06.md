# Aula 06 — Operando o simulador: gráficos, decisão e ROI (sem achismo)

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (fechamento da trilha) |
| **Tempo estimado** | 35–50 min |
| **Pré-requisitos** | Aula 01–05 |
| **Entrega** | mini‑relatório (10 linhas) + 2 evidências (figuras) |

> **Tese da aula:** simulação é ferramenta de engenharia quando gera **evidência**. Aqui você aprende a ler gráficos, comparar cenários e justificar uma decisão (inclui ROI simplificado).

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- ler throughput, holdup/filas e distribuição de residência como KPIs de processo;
- identificar gargalo provável com base em evidência (não opinião);
- comparar cenários “antes vs depois” e defender uma intervenção;
- estimar um ROI simplificado com base em ganho de throughput.

## Materiais (links do repositório)

- Figuras: `../docs/figuras/fig_04_throughput.png`, `fig_05_ocupacao_e_filas.png`, `fig_06_distribuicao_residencia.png`, `fig_07_antes_depois.png`
- Paper interativo (legendas): `../docs/index.html` (seção “Resultados”)
- Simulador: `python main.py` + `python scripts/gerar_figuras.py`

---

## 1) Como engenheiro lê as evidências (guia curto)

### 1.1 Throughput (saída ao longo do tempo)

**Perguntas:**

- a saída cresce de modo regular ou “em degraus”?
- há períodos longos com saída baixa? (sinal de saturação/gargalo)

### 1.2 Holdup e buffers (filas)

**Leitura:**

- holdup alto + fila crescendo → sistema perto ou acima da capacidade;
- fila que cresce e não “volta” → pressão alta (ρ próximo de 1 em algum trecho).

### 1.3 Distribuição do tempo de residência

**Leitura:**

- caudas longas indicam risco: alguns casos demoram muito;
- “média boa” pode esconder caudas ruins.

### 1.4 Antes vs Depois (intervenção)

**Leitura:**

- compare espera, utilização (se disponível) e processados;
- use isso para discutir custo/benefício (capex/opex vs ganho).

---

## 2) Desafio de simulação (reprodutível): simular e decidir

> **Objetivo:** escolher uma intervenção e defender com 2 evidências.

1) Rode o simulador com `config/parametros.yaml`.

2) Gere as figuras:

```bash
python scripts/gerar_figuras.py
```

3) Faça **uma** intervenção (mude uma variável por vez):

- **A:** aumentar `numero_caixas`
- **B:** aumentar `numero_de_mesas`
- **C:** reduzir `tempo_medio_almoco` (melhoria operacional)

4) Entrega: mini‑relatório (10 linhas)

- **Diagnóstico:** qual é o gargalo provável?
- **Intervenção escolhida:** A/B/C e por quê.
- **Evidências (mínimo 2):** cite 2 figuras pelo nome (ex.: `fig_04_throughput.png` e `fig_05_ocupacao_e_filas.png`).

---

## 3) Bônus: ROI (noção simples e honesta)

> **Importante:** aqui é um exercício didático de decisão; não substitui análise contábil real.

1) Defina um “valor por cliente atendido” (ex.: R$ 20).  
2) Calcule ganho aproximado: `Δ clientes_processados × valor`.  
3) Compare com custo estimado (caixa extra por turno, mesas, etc.).  

**Pergunta final:** o ganho justifica o custo no horizonte considerado?

---

## Pain points + mini‑FAQ

**1) Por que preciso citar duas evidências?**  
Para evitar “história boa com dado ruim”. Uma única métrica pode enganar.

**2) Qual é a diferença entre melhorar throughput e reduzir tempo no sistema?**  
Uma intervenção pode aumentar throughput e ainda assim piorar o tempo médio (trade‑off). Por isso compare métricas.

---

## Checklist de domínio

- Eu leio throughput/holdup/distribuição como KPIs.
- Eu defendo uma intervenção com evidência (mínimo 2 figuras).
- Eu escrevo uma decisão baseada em dados (não por intuição).

---

## Navegação

- **Anterior:** [Aula 05 — Ponte industrial](Aula05.md)
- **Fim da trilha:** volte ao [README da trilha](README.md)
