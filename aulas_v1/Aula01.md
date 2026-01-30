# Aula 01 — A Lógica dos Sistemas: pensar em “Caixa Preta”

| Campo | Valor |
|---|---|
| **Público-alvo** | Ensino médio / técnico (transição para nível universitário) |
| **Tempo sugerido** | 60 min |
| **Pré-requisitos** | Curiosidade + noção de “por minuto” |
| **Ferramentas** | Simulador (`python main.py`) |
| **Entrega** | 1 tabela (entrada/acúmulo/saída) + 3 respostas curtas |

## Visão geral
Você vai aprender a olhar um restaurante como um **sistema** (caixa preta) e descrever o que entra, o que acontece e o que sai. Esse é o primeiro passo para transformar “olhar uma fila” em **modelagem** e, depois, em **simulação**.

## Objetivo didático
- Entender um sistema como **caixa preta**: **Entrada → Processamento → Saída**.
- Começar a “traduzir” o restaurante (serviço) para a linguagem de processos (engenharia).
- Preparar o terreno para simular: definir **o que medir** e **o que controlar**.

## Roteiro sugerido (minutos)
- 0–10: caixa preta (entrada → processo → saída)
- 10–25: “perguntas de engenheiro” (o que medir)
- 25–40: tabela de tradução serviço ↔ processos
- 40–50: mini-código (fila como contador)
- 50–60: desafio (rodar e identificar métricas)

## Ideia central (em 30 segundos)
Um sistema é qualquer coisa onde “algo entra”, “algo acontece lá dentro” e “algo sai”.
Se você consegue medir as entradas e as saídas, você consegue começar a explicar **por que a fila aparece**.

---

## Conceitos-chave
- Caixa preta (entrada → processo → saída)
- Medidas: entrada, saída (throughput) e acúmulo (fila/ocupação)
- Analogia: cliente ↔ átomo/íon; fila ↔ holdup; etapa ↔ operação unitária

## 1) A caixa preta: o que entra, o que acontece, o que sai?
Imagine um restaurante universitário no almoço:

- **Entradas (inputs)**: alunos chegando, fome, tempo disponível, dinheiro/cartão, espaço (mesas), funcionários.
- **Processamento (process)**: pegar bandeja, servir, pagar, encontrar lugar, comer, liberar mesa.
- **Saídas (outputs)**: alunos atendidos, tempo gasto, satisfação, fila formada/zerada.

O pulo do gato: você não precisa saber “cada detalhe humano” para começar. Você só precisa escolher um **nível de detalhe** adequado ao seu objetivo.

### O que um engenheiro pergunta?
- **Qual é a taxa de chegada?** (quantos chegam por minuto)
- **Qual é a capacidade de atendimento?** (quantos o sistema consegue processar por minuto)
- **Onde acumula?** (fila / mesas ocupadas)
- **O que limita a saída?** (gargalo)

---

## 2) Restaurante ≈ Processo industrial (primeira tradução)
Nesta disciplina, vamos validar a analogia:

> **Cliente no restaurante** = **Átomo/Íon (ou “partícula”) em um processo químico**  
> A “fila” é um **acúmulo**; a “etapa” é uma **operação unitária**.

### Tabela de tradução (comece a decorar)
| Restaurante (serviço) | Processos (engenharia) | O que significa |
|---|---|---|
| Cliente | Partícula / átomo / íon | entidade que “flui” |
| Chegada de clientes | Vazão de alimentação (\(\lambda\)) | taxa de entrada |
| Buffet / Caixa | Operação unitária / restrição | etapa com capacidade |
| Fila | Tanque / buffer (holdup) | acúmulo dentro do sistema |
| Mesas ocupadas | Inventário em processo (WIP) | “material” que ainda não saiu |
| Clientes saindo | Throughput | taxa de saída |

**Por que isso é importante?** Porque a mesma lógica (fluxos + acúmulos + restrições) aparece em:
- restaurante (serviços)
- fábrica (produção)
- planta química (processos)

---

## 3) O que é “modelo” (e por que modelar)?
Um **modelo** é uma “versão simplificada” do mundo que:
- mantém o que é relevante para a pergunta;
- ignora o que atrapalha mais do que ajuda.

Exemplos de perguntas:
- “Com este layout e esta equipe, a fila vai explodir no pico?”
- “Se eu adicionar 1 caixa, o tempo de espera cai quanto?”
- “Se o almoço durar mais (tempo de residência), o que acontece com a ocupação?”

---

## 4) Mini-lógica em Python (sem matemática pesada)
Uma fila mínima pode ser vista como um contador:

```python
fila = 0

if cliente_chega:
    fila += 1

if caixa_livre and fila > 0:
    fila -= 1  # um cliente sai da fila e vai para o atendimento
```

O objetivo das próximas aulas é transformar `cliente_chega` e `caixa_livre` em regras baseadas em **tempo**, **taxas** e **capacidade**.

---

## Atividade (sem simulador): “mapa de inputs”
Escolha um restaurante (real ou imaginário) e responda:
- **Quais são 5 inputs medíveis?** (ex.: clientes/min, número de mesas, número de caixas…)
- **Quais são 3 outputs importantes?** (ex.: atendidos/hora, tempo médio de espera…)
- **Quais são 2 pontos de acúmulo?** (onde a fila “mora”?)

Escreva em 10 linhas, no formato:
> Input → Processo → Output

---

## Desafio de Simulação (Aula 01)
**Objetivo**: rodar o simulador e identificar (sem “chutar”) entradas, saídas e acúmulos.

1) Execute o simulador:

```bash
pip install -r requirements.txt
python main.py
```

2) Carregue:
- `config/parametros.yaml`
- `layouts/layout_padrao.txt`

3) Responda com base no relatório/saídas:
- **Qual é a entrada do sistema (em clientes/min ou clientes/h)?**
- **Qual é a saída (throughput)?**
- **Onde o sistema acumula (fila/ocupação)?**

### Entrega (curta)
Uma tabela com 3 linhas:
| Medida | Onde aparece | Unidade |
|---|---|---|
| Entrada | … | … |
| Acúmulo | … | … |
| Saída | … | … |

---

## Checklist de domínio (se você sabe isso, você avançou)
- Eu sei explicar “caixa preta” com minhas palavras.
- Eu consigo listar entradas, saídas e acúmulos do restaurante.
- Eu consigo apontar a analogia cliente ↔ partícula/íon sem perder o sentido físico.

