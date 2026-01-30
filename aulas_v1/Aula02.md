# Aula 02 — O Tempo como Variável: por que o mundo não chega “em intervalos perfeitos”

| Campo | Valor |
|---|---|
| **Público-alvo** | Ensino médio / técnico (transição para nível universitário) |
| **Tempo sugerido** | 70 min |
| **Pré-requisitos** | Aula 01; noção de taxa “por minuto” |
| **Ferramentas** | Celular (cronômetro) + simulador |
| **Entrega** | 1 comparação de cenários + 1 conclusão (2 frases) |

## Visão geral
Nesta aula, o tempo deixa de ser “detalhe” e vira a variável principal: chegadas e atendimentos variam, e essa variabilidade muda a fila mesmo quando a média parece igual.

## Objetivo didático
- Entender que **tempo** é a variável central em filas e simulação.
- Introduzir **estocástica** (aleatoriedade): por que chegadas e atendimentos variam.
- Diferenciar **tempo de ciclo**, **tempo de espera** e **tempo no sistema**.

## Roteiro sugerido (minutos)
- 0–10: experimento mental (mundo perfeito vs mundo real)
- 10–25: vocabulário do tempo (tabela)
- 25–40: \(\lambda\), \(\mu\), \(\rho\) (interpretação)
- 40–55: mini-código (variabilidade)
- 55–70: desafio (mesma média, variabilidade diferente)

---

## Conceitos-chave
- Tempo de espera (\(W_q\)) vs tempo no sistema (\(W\))
- Taxa de chegada (\(\lambda\)) e taxa de atendimento (\(\mu\))
- Utilização (\(\rho\)) e sensibilidade a variabilidade

## 1) Um experimento mental: dois mundos
### Mundo A (perfeito)
Chega exatamente 1 pessoa a cada 30 segundos. O caixa atende exatamente 1 pessoa a cada 30 segundos.

Resultado: quase não existe fila.

### Mundo B (real)
Às vezes chegam 3 pessoas “de uma vez”, depois fica um intervalo maior.
Às vezes o caixa demora mais (problema no pagamento), às vezes menos.

Resultado: **fila aparece**, mesmo que “na média” o sistema pareça equilibrado.

**Mensagem-chave:** a média importa, mas a **variabilidade** decide o tamanho da fila.

---

## 2) Vocabulário do tempo (sem misturar conceitos)
| Nome | Símbolo (opcional) | O que é | Exemplo no restaurante |
|---|---:|---|---|
| Intervalo entre chegadas | \(T_a\) | tempo entre um cliente chegar e o próximo | 0, 10 s, 50 s… |
| Tempo de serviço | \(T_s\) | tempo para atender um cliente em uma etapa | pagar no caixa |
| Tempo de espera | \(W_q\) | tempo parado na fila antes do serviço | tempo na fila do caixa |
| Tempo no sistema | \(W\) | espera + serviço + outras etapas | do portão até sair |
| Tempo de ciclo | \(CT\) | tempo para “processar” uma entidade | tempo total por cliente |

---

## 3) Chegadas como “taxa” (\(\lambda\)) e atendimentos como “capacidade” (\(\mu\))
Vamos usar duas grandezas:
- \(\lambda\): **taxa média de chegada** (clientes por minuto)
- \(\mu\): **taxa média de atendimento** (clientes por minuto) de uma etapa

A utilização (quão perto do limite você está) é:

\[
\rho = \frac{\lambda}{\mu}
\]

Interpretação:
- \(\rho < 1\): em média dá para atender, mas pode ter fila por variabilidade.
- \(\rho \approx 1\): o sistema fica sensível; qualquer oscilação vira fila grande.
- \(\rho > 1\): a fila tende a crescer sem parar (até um limite físico/regra).

---

## 4) “Estocástica” em linguagem simples
“Estocástico” não significa “bagunçado”. Significa:
> existe variação, e você descreve essa variação com regras probabilísticas.

Dois exemplos de como modelar um tempo:
- **Determinístico**: todo cliente demora exatamente 40 s no caixa.
- **Aleatório**: a maioria demora perto de 40 s, mas alguns demoram 10 s e outros 120 s.

---

## 5) Mini-código em Python: gerando variação de chegadas
Sem precisar saber cálculo, você consegue simular intervalos de chegada assim:

```python
import random

lambda_por_minuto = 2.0  # em média 2 clientes por minuto
lambda_por_segundo = lambda_por_minuto / 60.0

# Intertempo exponencial é um modelo comum para "chegadas aleatórias"
tempo_ate_proxima_chegada_s = random.expovariate(lambda_por_segundo)
```

E uma variação simples de tempo de serviço:

```python
import random

tempo_medio_servico_s = 40
variacao_s = 15
tempo_servico_s = max(5, int(random.gauss(tempo_medio_servico_s, variacao_s)))
```

**Leitura orientada:** não é para decorar distribuições agora. É para entender que “o tempo muda” e que isso muda as filas.

---

## Atividade: medindo o tempo com o celular
Escolha uma fila (restaurante, padaria, cantina) e registre 10 observações:
- 10 intervalos entre chegadas (aprox.)
- 10 tempos de atendimento (aprox.)

Depois responda:
- A variação é pequena ou grande?
- Você viu “rajadas” (várias pessoas chegando juntas)?

---

## Desafio de Simulação (Aula 02)
**Objetivo**: provar que **variabilidade** muda o desempenho mesmo com “mesma média”.

1) Rode dois cenários mantendo as médias iguais e mudando só a variabilidade (procure no `config/parametros.yaml`):
- `variabilidade_chegada` (ou parâmetro equivalente)
- `variabilidade_almoco` (ou parâmetro equivalente)

2) Compare (anote os valores):
- tempo médio de espera
- tamanho médio/máximo das filas
- throughput (saída por tempo)

3) Conclusão em 2 frases:
> “Mesmo com a mesma \(\lambda\) e \(\mu\), quando a variabilidade aumenta, ____ porque ____.”

---

## Conexão com a analogia química (um passo a mais)
No processo químico:
- “chegadas” podem ser variações na vazão de alimentação;
- “tempo de serviço” pode ser variação em mistura, transferência de massa, reação;
- “fila” é inventário acumulando em um tanque/linha.

| Restaurante | Processo químico | Efeito de variabilidade |
|---|---|---|
| Chegadas variáveis | Vazão de alimentação oscilando | tanque “enche/esvazia” |
| Serviço variável | cinética/transferência variando | etapa vira gargalo em picos |
| Fila | holdup | muda qualidade/estabilidade operacional |

