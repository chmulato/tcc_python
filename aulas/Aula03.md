# Aula 03 — Conservação de Massa: o que entra tem que sair (ou acumular)

> **Contexto deste repositório:** esta aula é o “coração” do reenquadramento.
> No restaurante, o balanço é de **pessoas**; na indústria, é de **massa/energia/espécies químicas**.

## Guia rápido
- **Tempo estimado**: 25–35 min
- **Pré-requisitos**: Aula 01 e Aula 02
- **Materiais**:
  - `docs/figuras/fig_04_throughput.png` (saída/throughput)
  - `docs/figuras/fig_05_ocupacao_e_filas.png` (acúmulo/holdup)
  - `SIMULATING.md` (métricas e parâmetros)

## Objetivo da aula
Entender a lógica de **balanço** (conservação) de forma intuitiva e aplicá-la para interpretar filas, ocupação e throughput no simulador.

---

## Explicação simples (analogia do dia a dia)
Pense em um estacionamento:

- carros **entram**;
- alguns **saem**;
- o resto **fica dentro**.

Se entram mais carros do que saem, o estacionamento **enche**. Se saem mais do que entram, ele **esvazia**.

No restaurante, é igual:

- entram clientes (chegadas),
- saem clientes (atendidos/saídas),
- o resto fica acumulado (filas + mesas ocupadas).

[Imagem: tanque enchendo e esvaziando, comparando com fila]

Sugestões de figuras do projeto:

- `docs/figuras/fig_04_throughput.png` (saída)
- `docs/figuras/fig_05_ocupacao_e_filas.png` (acúmulo)

---

## O salto técnico (Balanço de Massa)
Em Engenharia Química, a forma geral do balanço é:

\[
\text{Entrada} - \text{Saída} + \text{Geração} - \text{Consumo} = \text{Acúmulo}
\]

No restaurante (serviços), normalmente não há “reação química”, então:

- **Geração/Consumo ≈ 0**

Fica:

\[
\text{Entrada} - \text{Saída} = \text{Acúmulo}
\]

### Tradução direta
| Termo do balanço | No simulador |
|---|---|
| Entrada | chegadas (feed) |
| Saída | clientes que saem do sistema |
| Acúmulo | filas + ocupação (holdup/WIP) |

Se a fila cresce, é porque, por algum período, **Entrada > Saída**.

---

## Desafio prático (para testar no software)
1) Rode uma simulação e observe `docs/figuras/fig_04_throughput.png` (saída no tempo).
2) Em seguida, observe `docs/figuras/fig_05_ocupacao_e_filas.png` (holdup e buffers).

Pergunta:

- Em quais intervalos a **saída acumulada “fica plana”** (throughput estagnado)?
- O que acontece com o **acúmulo (fila)** nesses mesmos intervalos?

Escreva sua conclusão em uma frase usando o balanço:

> “Quando _____ > _____, o acúmulo _____.”

---

## Glossário (termos-chave)
- **Balanço de massa**: contabilidade de entradas, saídas e acúmulo.
- **Acúmulo (accumulation)**: aumento de “inventário” no sistema (fila/ocupação).
- **Holdup / WIP**: material/pessoas dentro do sistema.
- **Throughput**: taxa de saída.

---

## Checklist (ao final desta aula, você deve conseguir…)
- recitar a ideia “**entrada − saída = acúmulo**” com suas palavras.
- explicar por que **fila crescente** é um sinal de acúmulo positivo.
- relacionar um trecho de throughput baixo (Figura 4) com aumento de holdup/filas (Figura 5).
- dar um exemplo de “acúmulo” no restaurante e um exemplo de acúmulo em um processo industrial.

---

## Navegação
- **Anterior:** [Aula 02 — A Matemática das Filas](Aula02.md)
- **Próxima:** [Aula 04 — O Restaurante como Reator](Aula04.md)

