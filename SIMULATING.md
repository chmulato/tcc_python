# Tipos de Simulação e Utilização das Variáveis

## 1. Introdução

O simulador de tempo de permanência em restaurantes oferece dois tipos principais de simulação: **Determinística** e **Eventos Discretos (DES)**. Cada abordagem possui características, vantagens e limitações próprias. Este documento explica cada tipo, apresenta uma comparação e detalha como as variáveis de entrada são utilizadas.

---

## 2. Simulação Determinística

Utiliza médias e valores fixos para calcular o comportamento do sistema. Não há variabilidade ou aleatoriedade: todos os clientes são tratados de forma igual, e os resultados são sempre os mesmos para os mesmos parâmetros.

**Características:**
- Utiliza médias para tempo de chegada, atendimento e permanência.
- Não considera filas, atrasos ou variações individuais.
- Resultados rápidos e previsíveis.
- Útil para cenários simples ou para obter uma estimativa inicial.

---

## 3. Simulação por Eventos Discretos (DES)

Modela o sistema como uma sequência de eventos (chegada, atendimento, saída, etc.), permitindo a inclusão de variabilidade, filas e recursos limitados. Cada cliente é tratado individualmente, e o tempo de cada evento pode ser sorteado de uma distribuição estatística.

**Características:**
- Considera a dinâmica real do sistema (filas, recursos, atrasos).
- Permite variabilidade nos tempos (aleatoriedade).
- Resultados podem variar a cada execução (simulação estocástica).
- Útil para cenários complexos, análise de gargalos e dimensionamento realista.

---

## 4. Tabela Comparativa

```plaintext
| Característica                | Determinística                        | Eventos Discretos (DES)           |
|-------------------------------|---------------------------------------|-----------------------------------|
| Tempo de execução             | Muito rápido                          | Mais lento (simula cada evento)   |
| Considera filas               | Não                                   | Sim                               |
| Considera variabilidade       | Não                                   | Sim                               |
| Resultados sempre iguais      | Sim                                   | Não (pode variar)                 |
| Complexidade do modelo        | Baixa                                 | Alta                              |
| Uso recomendado               | Estimativas rápidas, cenários simples | Análise detalhada, cenários reais |
| Exemplos de uso               | Capacidade máxima, uso médio          | Tempos de espera, gargalos        |
```

---

## 5. Utilização das Variáveis de Entrada

### Determinística

As variáveis de entrada são usadas como valores médios e fixos para o cálculo dos resultados, sem variabilidade ou sorteio de valores.

- **clientes_por_minuto**: Define quantos clientes chegam a cada minuto.
- **tempo_medio_almoco**: Tempo fixo de permanência de cada cliente.
- **cadeiras_por_mesa** e **numero_de_mesas**: Capacidade total do restaurante.
- **tempo_total_simulacao**: Período total simulado.
- **numero_caixas**, **tempo_medio_atendimento**, etc.: Usados apenas como referência, sem filas ou restrições dinâmicas.

### Eventos Discretos (DES)

As variáveis de entrada são usadas para gerar eventos individuais e controlar o fluxo dinâmico do sistema.

- **clientes_por_minuto** e/ou **tempo_entre_clientes**: Agendam a chegada de cada cliente, podendo incluir variabilidade.
- **tempo_medio_almoco**: Base para o tempo de permanência, podendo ser sorteado de uma distribuição.
- **cadeiras_por_mesa**, **numero_de_mesas**: Limitam a quantidade de clientes sentados simultaneamente.
- **numero_caixas**, **tempo_medio_atendimento**: Limitam o atendimento simultâneo e determinam o tempo de cada cliente no caixa.
- **variabilidade_almoco**, **variabilidade_chegada**: Adicionam aleatoriedade nos tempos.
- **capacidade_maxima_fila**: Limita o tamanho das filas.
- **tempo_total_simulacao**: Tempo máximo da simulação ou número máximo de clientes.

---

## 6. Exemplos Práticos

### Fluxo típico do cliente no restaurante

```plaintext
[Fila] → [Buffet/Serve] → [Balança/Pesa] → [Caixa/Paga] → [Mesa/Come] → [Saída]
```

### Simulação Determinística

**Cenário:**  
- Clientes por minuto: 10  
- Tempo médio de refeição: 30 minutos  
- Número de mesas: 20  
- Cadeiras por mesa: 4  
- Tempo total da simulação: 60 minutos  

**Como funciona:**  
- Total de clientes: `10 * 60 = 600`
- Capacidade total: `20 * 4 = 80 lugares`
- Mesas ocupadas: `min(20, 600 // 4) = 20`
- Uso médio das mesas: `20 / 20 = 100%`
- Tempo total gasto: `600 * 30 = 18.000 minutos`

**Resultado:**  
Sempre igual para os mesmos parâmetros, sem variabilidade ou filas.

---

### Simulação por Eventos Discretos (DES)

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
- O tempo de chegada e de refeição de cada cliente pode variar.
- Se todas as mesas estiverem ocupadas, o cliente espera em uma fila.
- Atendimento no caixa pode gerar filas.
- Resultados variam a cada execução, refletindo situações reais.

**Exemplo de resultado:**  
- Total de clientes atendidos: 590  
- Tempo médio de espera na fila: 3,2 minutos  
- Uso médio das mesas: 97%  
- Tempo total gasto: 17.800 minutos  
- Número máximo de clientes na fila: 8

---

## 7. Quando usar cada abordagem?

- **Determinística:**  
  Para estimativas rápidas, planejamento inicial ou quando não há interesse em analisar filas e variabilidade.

- **DES:**  
  Para análises detalhadas, identificação de gargalos, avaliação do impacto de filas, recursos limitados e variabilidade nos processos.

---

**Dica:**  
Para obter uma visão completa do sistema, recomenda-se rodar ambos os tipos de simulação e comparar os resultados.

---