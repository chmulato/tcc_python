# Aula 03 — Balanço de Massa no Buffet: “Nada se perde, tudo sai ou acumula”

| Campo | Valor |
|---|---|
| **Público-alvo** | Ensino médio / técnico (transição para nível universitário) |
| **Tempo sugerido** | 70 min |
| **Pré-requisitos** | Aula 01–02 |
| **Ferramentas** | Simulador + leitura de gráficos (throughput e ocupação/filas) |
| **Entrega** | 3 balanços escritos + 1 interpretação curta baseada em gráfico |

## Visão geral
Você vai transformar a frase “a fila cresceu” numa equação que serve para restaurante e para planta química: **Acúmulo = Entrada − Saída**. Depois, vai usar essa equação para explicar o que você vê nos gráficos do simulador.

## Objetivo didático
- Transformar a intuição de “fila crescendo” na equação **Acúmulo = Entrada − Saída**.
- Interpretar filas e ocupação como **inventário (holdup/WIP)**.
- Conectar o restaurante à forma padrão de balanço usada em Engenharia Química.

## Roteiro sugerido (minutos)
- 0–10: a frase-mãe (acúmulo = entrada − saída)
- 10–25: versão “de engenharia química” (com geração/consumo)
- 25–40: onde medir (tabela de tradução + escolha do balanço)
- 40–55: mini-código (passos de tempo)
- 55–70: desafio (ler gráficos e escrever conclusão)

---

## Conceitos-chave
- Balanço de massa (com e sem geração/consumo)
- Acúmulo (fila + ocupação) como holdup/WIP
- Leitura de gráficos: quando a saída “não acompanha” a entrada

## 1) A frase que governa quase tudo
Se você observar qualquer sistema por um período de tempo, uma contabilidade sempre vale:

\[
\textbf{Acúmulo} = \textbf{Entrada} - \textbf{Saída}
\]

No restaurante:
- **Entrada**: clientes que chegam no sistema.
- **Saída**: clientes que terminam e saem do sistema.
- **Acúmulo**: clientes “dentro” (fila + mesas ocupadas + atendimentos em andamento).

> Se a fila cresce, então, por algum tempo, **Entrada > Saída**.

---

## 2) Versão “de Engenharia Química” (para reconhecer quando ver em livros)
A forma geral do balanço é:

\[
\text{Entrada} - \text{Saída} + \text{Geração} - \text{Consumo} = \text{Acúmulo}
\]

No restaurante, normalmente não existe “reação química” (ninguém aparece do nada):
- **Geração ≈ 0**
- **Consumo ≈ 0**

Então fica exatamente:

\[
\textbf{Entrada} - \textbf{Saída} = \textbf{Acúmulo}
\]

---

## 3) Tradução direta: o que entra, o que sai e onde acumula?
| Termo | No restaurante | No processo químico |
|---|---|---|
| Entrada | chegadas de clientes | vazão de alimentação |
| Saída | clientes que deixam o sistema | vazão de produto |
| Acúmulo | fila + ocupação + em serviço | holdup em tanques/linhas |

Essa tabela é a “ponte” do seu TCC: você pega uma situação observável e descreve com a gramática de processos.

---

## 4) Balanço em passos de tempo (o jeito que o computador pensa)
Simuladores frequentemente atualizam o estado em passos (ex.: a cada 1 segundo ou 1 minuto).

Uma forma simples:

```python
acumulo = 0

for t in range(tempo_total):
    entradas = chegadas_no_instante(t)
    saidas = saidas_no_instante(t)
    acumulo = acumulo + entradas - saidas
    acumulo = max(0, acumulo)  # não existe acumulo negativo
```

Isso é literalmente “Acúmulo = Entrada − Saída” rodando em loop.

---

## 5) Onde o balanço “quebra” (e por que isso é útil)
Se você medir entrada e saída e o acúmulo “não fecha”, algo está faltando no modelo, por exemplo:
- pessoas desistindo (abandono) → vira um termo de saída extra
- bloqueio por capacidade máxima (rejeição) → entrada efetiva não é a entrada “tentada”
- múltiplas filas internas (buffet, caixa, mesa) → você precisa escolher **qual** acúmulo está balanceando

Isso não é erro: é o modelo ficando mais realista.

---

## Atividade: escrevendo 3 balanços diferentes
Escreva a equação “Acúmulo = Entrada − Saída” para:
1) a fila do caixa
2) a ocupação das mesas
3) o sistema inteiro (do portão à saída)

Dica: em cada caso, “Entrada” e “Saída” mudam de significado.

---

## Desafio de Simulação (Aula 03)
**Objetivo**: observar o balanço acontecendo (entrada, saída e acúmulo) no tempo.

1) Execute uma simulação e gere as figuras.
2) Compare visualmente dois gráficos típicos:
- **Throughput** (saída ao longo do tempo)
- **Ocupação/Filas** (acúmulo ao longo do tempo)

3) Responda:
- Em quais períodos o throughput “estagna”?
- O acúmulo cresce nesses períodos? (explique usando a equação)

### Entrega (modelo de resposta)
Complete:
> “Entre \(t=\_\_\) e \(t=\_\_\), a saída ficou menor que a entrada, então o acúmulo \_\_\_\_. Quando a saída voltou a superar a entrada, o acúmulo \_\_\_\_.”

---

## Conexão com a analogia química (a validação)
Um processo químico e o restaurante obedecem a mesma lógica:
- **fluxos** (entradas e saídas)
- **inventário** (acúmulo)

Por isso, observar uma fila é um excelente “laboratório” para aprender balanço de massa.

