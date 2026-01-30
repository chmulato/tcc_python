# Aula 02 — Filas e Gargalos: por que as coisas acumulam?

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (já fez a Aula 01) |
| **Tempo estimado** | 25–35 min |
| **Pré-requisitos** | Aula 01 |
| **Entrega** | 1 comparação (2 cenários) + 1 conclusão (2 frases) |

> **Tese da aula:** fila é **acúmulo** (buffer/holdup). Ela cresce quando a **taxa de chegada (λ)** supera a **capacidade (μ)** — e cresce também quando a variabilidade é alta, mesmo com médias “boas”.

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- explicar por que fila cresce quando **λ > μ** (em média);
- usar **ρ = λ/μ** para interpretar “perto do limite”;
- diferenciar **problema de média** vs **problema de variabilidade**;
- apontar um gargalo provável no RU e propor uma intervenção simples.

## Materiais (links do repositório)

- Guia técnico: `../docs/SIMULATING.html`
- Figuras (se já tiver gerado): `../docs/figuras/fig_04_throughput.png` e `../docs/figuras/fig_05_ocupacao_e_filas.png`
- Simulador: `python main.py`

---

## 1) Intuição: “andar e parar”

Você já viu a fila “andar e parar”:

- fila cresce quando chegam pessoas **mais rápido** do que o atendimento acontece;
- fila diminui quando o atendimento consegue “queimar” o acúmulo.

> **Imagem recomendada:** `../docs/figuras/fig_05_ocupacao_e_filas.png` (filas/holdup no tempo).

---

## 2) Termos técnicos (com matemática mínima)

Definições:

- **λ (lambda)** = taxa média de chegada (clientes/min)
- **μ (mu)** = taxa média de atendimento de uma etapa (clientes/min)
- **ρ (rho)** = utilização (pressão do sistema): `ρ = λ/μ`

Interpretação prática:

- se **ρ < 1**: em média dá para atender, mas pode haver fila por variabilidade;
- se **ρ ≈ 1**: o sistema fica sensível; qualquer oscilação vira fila grande;
- se **ρ > 1**: a fila cresce até bater um limite (capacidade física ou regra).

### Onde os alunos se perdem (e o ajuste)

> **Pain point clássico:** “Se ρ < 1, então não deveria existir fila.”

Correção: o mundo real tem dispersão (chegadas/serviço). Mesmo com ρ < 1, podem existir **rajadas** de chegada ou tempos longos de atendimento, gerando fila temporária.

No simulador, isso é representado por parâmetros de variabilidade (ex.: `variabilidade_chegada`, `variabilidade_almoco`).  
Veja `../docs/SIMULATING.html` para a interpretação.

---

## 3) Desafio de simulação (reprodutível): criar e remover gargalo

> **Objetivo:** rodar 2 cenários mudando **uma variável por vez** e comparar métricas.

1) Execute o simulador (`python main.py`).

2) Rode dois cenários mudando apenas `numero_caixas`:

- **Cenário A:** `numero_caixas: 1`
- **Cenário B:** `numero_caixas: 2`

3) Compare e anote:

- throughput (clientes processados / taxa de saída)
- tempo médio de espera (fila)
- sinais de fila persistente (cresce e não volta)

4) Escreva a conclusão (2 frases):

> “Ao aumentar μ (capacidade do caixa), a fila ____ porque ____.”  
> “O gargalo provável era ____ pois ____.”

---

## Mini‑FAQ (dúvidas comuns)

**1) “Gargalo” é sempre o caixa?**  
Não. Pode ser buffet, caixas ou mesas (capacidade de residência). Depende do cenário (λ, variabilidade e capacidades).

**2) O que eu mudo primeiro: λ ou μ?**  
Para diagnóstico, normalmente você testa **μ** (capacidade), pois é uma intervenção direta (ex.: mais caixas). Para política operacional, você também pode atuar em **λ** (escalonar chegadas).

---

## Checklist de domínio (autoavaliação)

- Eu explico fila como acúmulo (buffer).
- Eu sei interpretar `ρ = λ/μ` sem “misturar termos”.
- Eu sei dizer por que variabilidade cria fila mesmo quando ρ < 1.

---

## Navegação

- **Anterior:** [Aula 01 — Sistemas e Fluxo](Aula01.md)
- **Próxima:** [Aula 03 — Balanço (Entrada − Saída = Acúmulo)](Aula03.md)
