# Simulação (Determinística vs DES) no contexto de Engenharia de Processos

## 1. Introdução (process thinking)

Este projeto é um **motor de Simulação por Eventos Discretos (DES)** aplicado a um sistema de fluxo com recursos finitos. O “restaurante” é um **ambiente análogo** para Engenharia de Processos: entidades entram com uma taxa (alimentação), atravessam operações unitárias, acumulam em buffers (filas) e deixam o sistema como vazão de saída.

Este documento explica:

- como interpretar o sistema como **processo dinâmico**;
- a diferença entre **simulação determinística** e **DES estocástico**;
- como os **parâmetros de entrada** se conectam a métricas industriais (throughput, holdup, tempo de residência);
- como reproduzir as **figuras do estudo de caso** usadas na apresentação (`index.html`).

---

## 2. Mapeamento de conceitos (serviços ↔ processos)

- **clientes_por_minuto** → **Feed Rate** (\(\lambda\)): taxa média de alimentação.
- **tempo_medio_atendimento**, **tempo_buffet**, **tempo_balcao** → **Taxas de serviço** (\(\mu\)) e tempos de processamento em operações unitárias.
- **tempo_medio_almoco** → **Tempo de residência** (\(\tau\)) na área de holdup (mesas).
- **filas** (buffet/caixa/mesa) → **Buffers / Inventário em processo (WIP/Holdup)**.
- **uso_medio_mesas** e picos de fila → **assinaturas de gargalo**.

---

## 3. Simulação determinística (estimativa de regime médio)

A simulação determinística usa **médias fixas** para obter uma estimativa rápida. Ela é útil para:

- triagem de cenários (ordem de grandeza),
- checagens iniciais de capacidade (capacidade instalada vs demanda média),
- comunicação executiva (quando variabilidade não é o foco).

**Limitação central:** não captura formação de filas por variabilidade nem regimes de saturação transiente.

---

## 4. Simulação por Eventos Discretos (DES) — dinâmica e variabilidade

No DES, o sistema é uma sequência de eventos (chegada, início/fim de serviço, alocação/liberação de recurso, saída). Cada entidade é tratada individualmente e o tempo evolui conforme a agenda de eventos.

**O que o DES permite observar:**

- formação de filas (buffers) por restrição de capacidade;
- saturação quando o sistema opera perto de \(\rho \approx \lambda/\mu \to 1\);
- impacto de variabilidade nas caudas (riscos), não só na média.

### Como a variabilidade é aplicada aqui

Os parâmetros:

- **variabilidade_chegada**
- **variabilidade_almoco**

são tratados como **frações (adimensionais)** que modulam a dispersão dos tempos em torno da média. Ex.: `0.10` significa aproximadamente **10% de desvio-padrão relativo**. Internamente, os tempos são amostrados de forma a permanecerem positivos.

---

## 5. Comparativo (resumo)

```plaintext
| Aspecto                         | Determinística                         | DES (eventos discretos)                 |
|---------------------------------|----------------------------------------|-----------------------------------------|
| Variabilidade (aleatoriedade)   | Não                                    | Sim                                     |
| Filas (buffers/WIP)             | Não modela                              | Modela explicitamente                   |
| Gargalos e saturação            | Apenas por média                         | Emergem por dinâmica + variabilidade    |
| Saída típica                    | “média do regime”                        | distribuição de resultados              |
| Uso recomendado                 | estimativa rápida / sanity check         | dimensionamento, gargalos, risco        |
```

---

## 6. Variáveis de entrada (interpretação “de planta”)

### Alimentação (feed)

- **clientes_por_minuto**: taxa média de entrada (\(\lambda\)).
- **tempo_entre_clientes**: intervalo médio entre chegadas (min). Idealmente, deve ser coerente com `clientes_por_minuto`:
  - referência: \(tempo\_entre\_clientes \approx 1 / clientes\_por\_minuto\)

#### Configuração recomendada (para evitar “cenário desligado”)

Para manter a alimentação consistente, recomenda-se **definir `clientes_por_minuto`** e ajustar `tempo_entre_clientes` para a relação:

\[
tempo\_entre\_clientes \approx \frac{1}{clientes\_por\_minuto}
\]

Exemplo de `config/parametros.yaml` coerente:

```yaml
# Alimentação (feed)
clientes_por_minuto: 12
tempo_entre_clientes: 0.0833  # ≈ 1/12 min (≈ 5 s)

# Residência (holdup)
tempo_medio_almoco: 30
numero_de_mesas: 25
cadeiras_por_mesa: 4

# Operações unitárias (serviço)
numero_caixas: 2
tempo_medio_atendimento: 2

# Horizonte de simulação
tempo_total_simulacao: 120

# Variabilidade (fração relativa; ex.: 0.10 ≈ 10%)
variabilidade_chegada: 0.10
variabilidade_almoco: 0.15
```

Se `tempo_entre_clientes` estiver muito maior do que \(1/clientes\_por\_minuto\), o sistema pode parecer “sem alimentação” (poucas chegadas) e mascarar gargalos.

### Capacidade / recursos (unit operations)

- **numero_caixas**, **tempo_medio_atendimento**: capacidade e tempo de serviço em operação crítica.
- (se configurados) **tempo_buffet**, **tempo_balcao**: tempos de processamento intermediários.

### Holdup (residência)

- **numero_de_mesas**, **cadeiras_por_mesa**: capacidade física de residência (limite de holdup).
- **tempo_medio_almoco**: tempo médio de residência.

### Variabilidade e buffers

- **variabilidade_chegada**, **variabilidade_almoco**: dispersão estocástica relativa.
- **capacidade_maxima_fila** (quando aplicável): limite de buffer.

---

## 7. Saídas e métricas (como ler “industrialmente”)

Resultados típicos do DES:

- **clientes_processados**: saída total (produção/throughput acumulado).
- **tempo_medio_permanencia_cliente**: tempo de residência observado.
- **tempo_medio_espera_fila_mesa** e **tamanho_max_fila_mesa**: holdup em buffer e severidade do gargalo.
- **uso_medio_mesas (%)**: utilização média do “volume de processo”.

Essas métricas alimentam as figuras do case: throughput no tempo, holdup/filas, distribuição de residência e comparação antes/depois.

---

## 8. Como reproduzir as figuras do estudo de caso

As figuras usadas no `index.html` são geradas automaticamente em `docs/figuras/`.

1) Instale dependências:

```sh
pip install -r requirements.txt
```

2) Gere as figuras:

```sh
python scripts/gerar_figuras.py
```

Saídas (exemplos):

- `fig_02a_fluxo_servico.png`, `fig_02b_fluxo_processo.png`
- `fig_04_throughput.png`
- `fig_05_ocupacao_e_filas.png`
- `fig_06_distribuicao_residencia.png`
- `fig_07_antes_depois.png`

---

## 9. Quando usar cada abordagem?

- **Determinística**: quando você precisa de uma estimativa rápida do “regime médio” e não pretende discutir risco/variabilidade.
- **DES**: quando o objetivo é **identificar gargalos**, dimensionar capacidade, avaliar impacto de variabilidade e justificar intervenções com evidência.

---

