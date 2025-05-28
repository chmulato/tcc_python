# Tipos de Simulação e Utilização das Variáveis

## 1. Introdução

O simulador de tempo de permanência em restaurantes oferece dois tipos principais de simulação: **Determinística** e **Eventos Discretos (DES)**. Cada abordagem possui características, vantagens e limitações próprias. Este documento explica cada tipo, apresenta uma comparação e detalha como as variáveis de entrada são utilizadas em cada abordagem.

---

## 2. Simulação Determinística

A simulação determinística utiliza médias e valores fixos para calcular o comportamento do sistema. Não há variabilidade ou aleatoriedade: todos os clientes são tratados de forma igual, e os resultados são sempre os mesmos para os mesmos parâmetros.

**Características:**
- Utiliza médias para tempo de chegada, atendimento e permanência.
- Não considera filas, atrasos ou variações individuais.
- Resultados rápidos e previsíveis.
- Útil para cenários simples ou para obter uma estimativa inicial.

---

## 3. Simulação por Eventos Discretos (DES)

A simulação DES modela o sistema como uma sequência de eventos (chegada, atendimento, saída, etc.), permitindo a inclusão de variabilidade, filas e recursos limitados. Cada cliente é tratado individualmente, e o tempo de cada evento pode ser sorteado de uma distribuição estatística.

**Características:**
- Considera a dinâmica real do sistema (filas, recursos, atrasos).
- Permite variabilidade nos tempos (aleatoriedade).
- Resultados podem variar a cada execução (simulação estocástica).
- Útil para cenários complexos, análise de gargalos e dimensionamento realista.

---

## 4. Tabela Comparativa

| Característica                | Determinística                        | Eventos Discretos (DES)           |
|-------------------------------|---------------------------------------|-----------------------------------|
| Tempo de execução             | Muito rápido                          | Mais lento (simula cada evento)   |
| Considera filas               | Não                                   | Sim                               |
| Considera variabilidade       | Não                                   | Sim                               |
| Resultados sempre iguais      | Sim                                   | Não (pode variar)                 |
| Complexidade do modelo        | Baixa                                 | Alta                              |
| Uso recomendado               | Estimativas rápidas, cenários simples | Análise detalhada, cenários reais |
| Exemplos de uso               | Capacidade máxima, uso médio          | Tempos de espera, gargalos        |

---

## 5. Utilização das Variáveis de Entrada

### Simulação Determinística

Na simulação determinística, as variáveis de entrada são usadas diretamente como valores médios e fixos para o cálculo dos resultados. Não há variabilidade ou sorteio de valores.

- **clientes_por_minuto**: Define quantos clientes chegam a cada minuto, usado para calcular o total de clientes.
- **tempo_medio_almoco**: Usado como tempo fixo de permanência de cada cliente.
- **cadeiras_por_mesa** e **numero_de_mesas**: Definem a capacidade total do restaurante.
- **tempo_total_simulacao**: Define o período total simulado.
- **numero_caixas**, **tempo_medio_atendimento**, etc.: Usados apenas como referência ou para cálculos diretos, sem filas ou restrições dinâmicas.

### Simulação por Eventos Discretos (DES)

Na simulação DES, as variáveis de entrada são usadas para gerar eventos individuais e controlar o fluxo dinâmico do sistema.

- **clientes_por_minuto** e/ou **tempo_entre_clientes**: Usados para agendar a chegada de cada cliente, podendo incluir variabilidade (aleatoriedade).
- **tempo_medio_almoco**: Usado como base para o tempo de permanência de cada cliente, podendo ser sorteado de uma distribuição.
- **cadeiras_por_mesa**, **numero_de_mesas**: Limitam a quantidade de clientes que podem sentar simultaneamente, controlando filas e ocupação.
- **numero_caixas**, **tempo_medio_atendimento**: Limitam o atendimento simultâneo e determinam o tempo de cada cliente no caixa.
- **variabilidade_almoco**, **variabilidade_chegada**: Usados para adicionar aleatoriedade nos tempos de refeição e chegada.
- **capacidade_maxima_fila**: Limita o tamanho das filas, podendo causar rejeição de clientes.
- **tempo_total_simulacao**: Define o tempo máximo da simulação ou o número máximo de clientes.

### Resumo das Variáveis

| Variável                  | Determinística (uso)          | DES (uso)                                 |
|---------------------------|-------------------------------|-------------------------------------------|
| clientes_por_minuto       | Valor fixo para cálculo       | Gera eventos de chegada                   |
| tempo_medio_almoco        | Valor fixo por cliente        | Tempo individual (pode ser aleatório)     |
| cadeiras_por_mesa         | Capacidade total              | Capacidade e restrição dinâmica           |
| numero_de_mesas           | Capacidade total              | Capacidade e restrição dinâmica           |
| tempo_total_simulacao     | Período fixo                  | Período ou critério de parada             |
| numero_caixas             | Referência                    | Limita atendimento simultâneo             |
| tempo_medio_atendimento   | Referência                    | Tempo individual de atendimento           |
| variabilidade_almoco      | Ignorado                      | Controla aleatoriedade do almoço          |
| variabilidade_chegada     | Ignorado                      | Controla aleatoriedade das chegadas       |
| capacidade_maxima_fila    | Ignorado                      | Limita tamanho das filas                  |

---

## 6. Orientação de Uso

- **Use a simulação determinística** para obter uma visão geral rápida do sistema, especialmente em fases iniciais de estudo ou quando não há necessidade de detalhamento.
- **Use a simulação DES** quando for necessário analisar filas, tempos de espera, gargalos, ou quando a variabilidade dos processos for relevante para a tomada de decisão.


Claro! Aqui estão exemplos práticos para o **Tópico 7** do seu arquivo SIMULATING.MD, mostrando como funcionam as simulações Determinística e DES no contexto do seu simulador:

---

## 7. Exemplos Práticos de Simulação

### Fluxo típico do cliente no restaurante

[Fila] → [Buffet/Serve] → [Balança/Pesa] → [Caixa/Paga] → [Mesa/Come] → [Saída]

---

### 7.1 Simulação Determinística

**Cenário:**  
- Clientes por minuto: 10  
- Tempo médio de refeição: 30 minutos  
- Número de mesas: 20  
- Cadeiras por mesa: 4  
- Tempo total da simulação: 60 minutos  

**Como funciona:**  
Neste modo, o simulador calcula diretamente:
- Total de clientes: `10 clientes/minuto * 60 minutos = 600 clientes`
- Capacidade total do restaurante: `20 mesas * 4 cadeiras = 80 lugares`
- Mesas ocupadas: `min(20, 600 // 4) = 20`
- Uso médio das mesas: `20 / 20 = 100%`
- Tempo total gasto pelos clientes: `600 * 30 = 18.000 minutos`

**Resultado esperado:**  
Os resultados serão sempre os mesmos para os mesmos parâmetros, pois não há variabilidade ou filas.

---

### 7.2 Simulação por Eventos Discretos (DES)

**Cenário:**  
- Clientes por minuto: 10  
- Tempo médio de refeição: 30 minutos  
- Número de mesas: 20  
- Cadeiras por mesa: 4  
- Tempo total da simulação: 60 minutos  
- Variabilidade de chegada: 2 minutos  
- Variabilidade de refeição: 5 minutos  
- Número de caixas: 2  
- Tempo médio de atendimento no caixa: 2 minutos  

**Como funciona:**  
Neste modo, cada cliente é simulado individualmente:
- O tempo de chegada de cada cliente pode variar (ex: sorteado de uma distribuição).
- Se todas as mesas estiverem ocupadas, o cliente espera em uma fila.
- O tempo de refeição de cada cliente pode variar.
- O atendimento no caixa pode gerar filas, dependendo do número de caixas disponíveis.
- O resultado pode variar a cada execução, refletindo situações reais como espera, gargalos e o impacto da variabilidade.

**Exemplo de resultado:**  
- Total de clientes atendidos: 590 (alguns podem não ser atendidos devido à lotação ou filas)
- Tempo médio de espera na fila: 3,2 minutos
- Uso médio das mesas: 97%
- Tempo total gasto pelos clientes: 17.800 minutos
- Número máximo de clientes na fila: 8

---

### 7.3 Quando usar cada abordagem?

- **Determinística:**  
  Use para estimativas rápidas, planejamento inicial ou quando não há interesse em analisar filas e variabilidade.

- **DES:**  
  Use para análises detalhadas, identificação de gargalos, avaliação do impacto de filas, recursos limitados e variabilidade nos processos.

---

**Dica:**  
Para obter uma visão completa do sistema, recomenda-se rodar ambos os tipos de simulação e comparar os resultados.

---

Se quiser exemplos com outros parâmetros ou cenários, é só pedir!