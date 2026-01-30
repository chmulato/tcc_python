# Aula 02 — A Matemática das Filas: por que as coisas acumulam (gargalos)

> **Contexto deste repositório:** aqui, “fila” é o mesmo que **buffer/inventário** em um processo industrial.
> Você vai usar o simulador do restaurante para visualizar quando \(\lambda\) supera a capacidade \(\mu\).

## Guia rápido
- **Tempo estimado**: 25–35 min
- **Pré-requisitos**: Aula 01 (conceito de sistema e fluxo)
- **Materiais**:
  - `SIMULATING.md` (interpretação de \(\lambda\), \(\mu\), \(\rho\) e variabilidade)
  - `docs/figuras/fig_05_ocupacao_e_filas.png` e `docs/figuras/fig_04_throughput.png`
  - simulador (`python main.py`)

## Objetivo da aula
Entender, com matemática simples, por que filas surgem e como identificar **gargalos** a partir de taxas, variabilidade e capacidade.

---

## Explicação simples (analogia do dia a dia)
Você já viu a fila “andar e parar”:

- A fila cresce quando chegam pessoas **mais rápido** do que o atendimento acontece.
- A fila diminui quando o atendimento consegue “queimar estoque” de pessoas esperando.

[Imagem: fila aumentando (entrada > saída) e diminuindo (entrada < saída)]

Sugestão de figura do projeto: `docs/figuras/fig_05_ocupacao_e_filas.png` (buffers/holdup no tempo).

Uma regra intuitiva:

- Se você tem **1 caixa** atendendo em média 1 pessoa por minuto, mas chegam 2 pessoas por minuto, a fila cresce.
- Se você abre mais um caixa e passa a atender 2 por minuto, a fila para de crescer (em média).

---

## O salto técnico (termos de Engenharia de Processos)
Em teoria das filas, duas quantidades são essenciais:

- \(\lambda\) = **taxa média de chegada** (feed rate)
- \(\mu\) = **taxa média de atendimento** (capacidade de serviço)

A “pressão” sobre o sistema é a **utilização**:

\[
\rho = \frac{\lambda}{\mu}
\]

Interpretação (bem prática):

- Se \(\rho < 1\): o sistema “dá conta” em média (fila tende a estabilizar).
- Se \(\rho \approx 1\): o sistema vira “sensível” a qualquer variação (filas explodem em horários de pico).
- Se \(\rho > 1\): fila cresce sem parar (até atingir um limite físico ou regra de rejeição).

### Por que a variabilidade importa?
Mesmo com \(\rho < 1\), filas aparecem porque o mundo real não é constante:

- chegadas variam
- tempos de serviço variam

No simulador, isso é controlado por:

- `variabilidade_chegada`
- `variabilidade_almoco`

Veja `SIMULATING.md` para a interpretação completa.

> Dica importante: mantenha `tempo_entre_clientes ≈ 1/clientes_por_minuto` (veja “Configuração recomendada” em `SIMULATING.md`)
> para evitar um cenário com alimentação inconsistente.

---

## Desafio prático (para testar no software)
Objetivo: **criar e eliminar um gargalo**.

1) Rode duas simulações mudando só `numero_caixas`:

- Cenário A: `numero_caixas: 1`
- Cenário B: `numero_caixas: 2`

2) Compare:

- tempo médio de espera (fila)
- clientes processados
- sinais de fila crescente

Dica: gere as figuras e compare:

- `docs/figuras/fig_05_ocupacao_e_filas.png` (buffers/filas)
- `docs/figuras/fig_04_throughput.png` (saída)

---

## Glossário (termos-chave)
- **Fila (queue)**: acúmulo de entidades esperando por capacidade.
- **Gargalo (bottleneck)**: etapa que limita o throughput global.
- **\(\lambda\)**: taxa de chegada (alimentação).
- **\(\mu\)**: taxa de serviço (capacidade).
- **\(\rho\)**: utilização (quão “perto do limite” o sistema opera).
- **Variabilidade**: dispersão nos tempos (chegadas/serviço/residência).

---

## Checklist (ao final desta aula, você deve conseguir…)
- explicar por que uma fila cresce quando **\(\lambda > \mu\)** (em média).
- usar \(\rho = \lambda/\mu\) para dizer se o sistema está **longe** ou **perto** da saturação.
- dar um exemplo prático de **gargalo** no restaurante (ex.: caixa) e como mitigá-lo.
- explicar por que **variabilidade** cria filas mesmo quando \(\rho < 1\).

---

## Navegação
- **Anterior:** [Aula 01 — O Mundo em Fluxo](Aula01.md)
- **Próxima:** [Aula 03 — Conservação de Massa](Aula03.md)

