# Aula 01 — Sistemas e Fluxo: pensando em “Entrada → Processo → Saída”

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (ensino médio/técnico → início de graduação) |
| **Tempo estimado** | 20–30 min |
| **Pré-requisitos** | Nenhum |
| **Entrega** | 1 tabela (entrada/acúmulo/saída) + 3 respostas curtas |

> **Contexto do projeto:** estas aulas usam o **Restaurante Universitário (RU)** como estudo de caso para ensinar **Engenharia de Processos**. O RU é tratado como um **Sistema de Eventos Discretos (DES)** — a mesma lógica que aparece em plantas industriais.

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- definir um sistema como **Entrada → Processo → Saída**;
- localizar **onde o sistema acumula** (fila/ocupação) e por que isso importa;
- reconhecer o RU como um sistema “didático”, mas com **métrica de engenharia** (throughput, holdup/WIP, tempo no sistema).

## Materiais (links do repositório)

- **Paper interativo (figuras e narrativa):** `../docs/index.html`
- **Sala Digital (trilha):** `../docs/portal.html`
- **Guia técnico (simulação):** `../docs/SIMULATING.html`
- **Figuras (se já tiver gerado):** `../docs/figuras/`

---

## 1) Intuição (sem matemática): o RU como sistema

Imagine o RU no horário de almoço:

- pessoas **chegam** (entrada);
- passam por etapas (processo);
- saem do sistema (saída).

Isso é o mesmo padrão de qualquer processo industrial: **algo entra**, **é transformado/atendido**, **e sai**.

> **Nota de leitura:** em engenharia, “transformado” pode significar serviço (atendimento) ou reação/separação — o padrão de fluxo é o mesmo.

### Modelo mental (3 perguntas)

1) **O que entra?** (clientes por minuto)  
2) **O que acontece dentro?** (filas, serviços, ocupação)  
3) **O que sai?** (clientes processados / taxa de saída)

---

## 2) Tradução para linguagem de Engenharia de Processos

| No RU (serviços) | Em processos (indústria) | O que significa |
|---|---|---|
| Pessoas chegando | **Vazão de alimentação (λ)** | taxa de entrada |
| Buffet/Caixa | **Operações unitárias / recursos** | etapas com capacidade (μ) |
| Filas + ocupação | **Holdup / WIP** | inventário “dentro” do sistema |
| Pessoas saindo | **Throughput** | taxa de saída |

> **Definição prática de DES:** o estado do sistema muda quando ocorre um evento (chegada, início/fim de atendimento, ocupar/liberar mesa, saída).

---

## 3) Atividade (em sala): mapeamento de medidas

Preencha a tabela com base no seu entendimento do RU (não precisa rodar o software ainda):

| Medida | Exemplo no RU | Unidade | Onde aparece |
|---|---|---:|---|
| **Entrada** | clientes chegando | clientes/min | parâmetro do cenário |
| **Acúmulo** | fila + mesas ocupadas | clientes | gráfico/estado |
| **Saída** | clientes que finalizaram | clientes/min | throughput |

**Entrega (curta):** responda em 1 frase:

- “O que entra no RU é ____.”
- “O que acumula no RU é ____.”
- “O que sai do RU é ____.”

---

## 4) Desafio de simulação (reprodutível)

> **Objetivo:** rodar um cenário base e registrar 3 métricas.

1) Instale dependências e execute o simulador:

```bash
pip install -r requirements.txt
python main.py
```

2) Carregue:
- `config/parametros.yaml`
- `layouts/layout_padrao.txt`

3) Rode a simulação e registre:
- **Clientes processados** (saída total)
- **Tempo médio no sistema** (tempo de permanência)
- **Suspeita de gargalo** (qual etapa “segura” a saída?)

4) (Opcional) gere evidências visuais:

```bash
python scripts/gerar_figuras.py
```

Abra `../docs/index.html` e veja “Resultados” para interpretar as figuras.

---

## Pontos de dúvida (pain points) + mini‑FAQ

**1) “Fila” e “acúmulo” são a mesma coisa?**  
Quase: “fila” é **um tipo de acúmulo**. O acúmulo total inclui **fila + ocupação + atendimento em andamento**.

**2) Por que isso é Engenharia de Processos se é um restaurante?**  
Porque a estrutura do problema é a mesma: fluxo com capacidade finita, buffers, gargalos e variabilidade.

**3) O que eu devo medir primeiro?**  
Sempre: **entrada**, **saída** e **acúmulo** (o resto deriva disso).

---

## Checklist de domínio (autoavaliação)

- Eu explico um sistema como **Entrada → Processo → Saída**.
- Eu sei apontar no RU onde ocorre **acúmulo** (fila/ocupação).
- Eu sei dizer, em uma frase, o que é **DES**.

---

## Navegação

- **Próxima:** [Aula 02 — Filas e Gargalos (λ, μ, ρ)](Aula02.md)

