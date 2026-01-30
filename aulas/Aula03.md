# Aula 03 — Balanço (Conservação): Entrada − Saída = Acúmulo

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (já fez Aula 01–02) |
| **Tempo estimado** | 25–35 min |
| **Pré-requisitos** | Aula 01 e Aula 02 |
| **Entrega** | 1 conclusão baseada em gráficos + 1 frase de balanço |

> **Ideia central:** quando você vê fila crescer, você está vendo **acúmulo positivo**. E acúmulo positivo acontece quando, por algum período, **Entrada > Saída**.

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- aplicar o balanço simplificado: **Acúmulo = Entrada − Saída**;
- interpretar gráficos de saída (throughput) e acúmulo (holdup/filas);
- escrever uma conclusão causal, e não descritiva (“fila aumentou porque…”).

## Materiais (links do repositório)

- Figuras: `../docs/figuras/fig_04_throughput.png` e `../docs/figuras/fig_05_ocupacao_e_filas.png`
- Guia técnico: `../docs/SIMULATING.html`
- Paper interativo (legendas): `../docs/index.html`

---

## 1) Intuição: estacionamento (ou tanque)

Pense em um estacionamento:

- carros entram;
- alguns saem;
- o resto fica dentro.

Se entra mais do que sai, ele enche. Se sai mais do que entra, ele esvazia.  
No RU é igual: **chegadas** (entrada), **saídas** (clientes finalizados), **acúmulo** (fila + ocupação).

---

## 2) Forma de engenharia (sem “salto de fé”)

Em Engenharia Química, a forma geral é:

```text
Entrada − Saída + Geração − Consumo = Acúmulo
```

No RU, normalmente não há geração/consumo de “clientes” dentro do sistema (ninguém surge do nada), então:

```text
Entrada − Saída = Acúmulo
```

Tradução direta:

| Termo | No RU (simulador) |
|---|---|
| Entrada | chegadas (feed) |
| Saída | clientes que saem do sistema |
| Acúmulo | filas + ocupação (holdup/WIP) |

> **Regra de leitura:** fila crescendo é um tipo de acúmulo crescendo — logo, por um período, Entrada > Saída.

---

## 3) Desafio de simulação (reprodutível): “casar” dois gráficos

> **Objetivo:** provar a mesma história por duas evidências diferentes (saída e acúmulo).

1) Rode uma simulação (qualquer cenário base).
2) Gere as figuras:

```bash
python scripts/gerar_figuras.py
```

3) Compare:

- **Saída/throughput**: `../docs/figuras/fig_04_throughput.png`
- **Acúmulo (holdup/filas)**: `../docs/figuras/fig_05_ocupacao_e_filas.png`

4) Responda (em 3 linhas):

- Em quais momentos a saída fica “fraca” (estagna/baixa)?
- O acúmulo aumenta nesses momentos?
- Complete a frase:

> “Quando **Entrada** > **Saída**, o **Acúmulo** ____.”

---

## Pain points + mini‑FAQ

**1) “Acúmulo” é só fila?**  
Não. Acúmulo pode ser fila, ocupação ou atendimento em andamento. Depende do “recorte” do balanço.

**2) Por que preciso de dois gráficos?**  
Para evitar conclusões por um único sinal. Engenharia pede **evidências convergentes**.

---

## Checklist de domínio

- Eu uso “Entrada − Saída = Acúmulo” para explicar o que vejo (não só descrever).
- Eu consigo ligar um trecho de throughput baixo ao crescimento de holdup/filas.

---

## Navegação

- **Anterior:** [Aula 02 — Filas e Gargalos](Aula02.md)
- **Próxima:** [Aula 04 — Operações Unitárias (mesa como residência)](Aula04.md)

