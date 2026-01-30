# Aula 04 — O Restaurante como Reator: operações unitárias (tanques, misturadores, separadores)

> **Contexto deste repositório:** “buffet”, “caixa” e “mesa” são tratados como **operações unitárias**.
> A “mesa” é um ótimo análogo de uma unidade com **tempo de residência** (holdup domina o desempenho).

## Guia rápido
- **Tempo estimado**: 30–40 min
- **Pré-requisitos**: Aula 01–03 (fluxo, filas e balanço)
- **Materiais**:
  - `docs/figuras/fig_02a_fluxo_servico.png` e `docs/figuras/fig_02b_fluxo_processo.png`
  - `docs/figuras/fig_03_layout_base.png` (planta ASCII renderizada)
  - simulador (`python main.py`) para testar mudanças em \(\tau\)

## Objetivo da aula
Entender como etapas de um serviço (buffet/caixa/mesa) podem ser modeladas como **operações unitárias** e como isso se conecta à linguagem clássica da Engenharia Química.

---

## Explicação simples (analogia do dia a dia)
Pense no restaurante como uma linha com estações:

1. Você entra (chegada).
2. Passa pelo buffet (pega comida).
3. Passa pelo caixa (paga).
4. Fica na mesa (consome / permanece).
5. Sai.

Cada estação tem duas coisas:

- **capacidade** (quantas pessoas consegue atender por vez)
- **tempo de processamento** (quanto tempo cada pessoa fica nessa etapa)

[Imagem: “estações” conectadas por setas]

Sugestões de figuras do projeto:

- `docs/figuras/fig_02a_fluxo_servico.png` (serviços)
- `docs/figuras/fig_02b_fluxo_processo.png` (processo)

---

## O salto técnico (operações unitárias)
Em plantas químicas, um processo é desenhado como um **flowsheet**:

- **Tanques** (estoques/holdup)
- **Reatores** (transformação ao longo do tempo)
- **Misturadores** (junção de correntes)
- **Separadores** (divisão de correntes)

### Analogia direta
| Restaurante | Operação unitária (processo) | Interpretação |
|---|---|---|
| Fila | Tanque/buffer | inventário em processo |
| Buffet/Caixa | Unidade de serviço | taxa de processamento \(\mu\) |
| Mesa | Tanque/reator de residência | permanência \(\tau\) domina holdup |
| Entrada/Saída | Correntes | vazões (feed/throughput) |

### Tempo de residência (\(\tau\))
Em processos contínuos, uma relação muito usada é:

\[
\tau \approx \frac{\text{Holdup}}{\text{Vazão}}
\]

No restaurante:

- holdup ≈ pessoas sentadas / em espera
- vazão ≈ pessoas que entram/saem por tempo

---

## Desafio prático (para testar no software)
Objetivo: perceber o “efeito reator” da mesa.

1) Faça duas simulações mudando apenas `tempo_medio_almoco`:

- Cenário A: 30 min
- Cenário B: 45 min

2) Compare:

- `uso_medio_mesas (%)`
- tempo médio de permanência
- crescimento de fila para mesa

Pergunta:

- Por que aumentar \(\tau\) (residência) aumenta holdup e pode reduzir throughput?

Dica: compare `docs/figuras/fig_04_throughput.png` e `docs/figuras/fig_05_ocupacao_e_filas.png` antes/depois.

---

## Glossário (termos-chave)
- **Operação unitária**: etapa padrão de processamento (reator, separador, tanque).
- **Flowsheet**: diagrama de processo (unidades + correntes).
- **Residência (\(\tau\))**: tempo médio que algo permanece em uma unidade/sistema.
- **Capacidade**: limite de atendimento/processamento.

---

## Checklist (ao final desta aula, você deve conseguir…)
- explicar o que é uma **operação unitária** usando exemplos do restaurante (buffet/caixa/mesa).
- dizer por que a **mesa** é um bom análogo de unidade com **tempo de residência \(\tau\)**.
- relacionar aumento de \(\tau\) com aumento de **holdup** e possível queda de throughput.
- identificar (em palavras) um “flowsheet” do restaurante: unidades + correntes.

---

## Navegação
- **Anterior:** [Aula 03 — Conservação de Massa](Aula03.md)
- **Próxima:** [Aula 05 — Hidrometalurgia Seletiva](Aula05.md)

