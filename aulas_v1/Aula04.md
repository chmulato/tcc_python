# Aula 04 — Gargalos (Bottlenecks): por que o sistema trava?

| Campo | Valor |
|---|---|
| **Público-alvo** | Ensino médio / técnico (transição para nível universitário) |
| **Tempo sugerido** | 70 min |
| **Pré-requisitos** | Aula 01–03 |
| **Ferramentas** | Simulador + comparação de cenários |
| **Entrega** | 1 tabela base vs intervenções + 1 conclusão (gargalo) |

## Visão geral
Você vai aprender a identificar gargalos com evidência (fila + utilização + sensibilidade) e a testar intervenções: melhorar um ponto só ajuda de verdade quando esse ponto é o **gargalo**.

## Objetivo didático
- Identificar **gargalos** como restrições que limitam o throughput.
- Ligar “fila grande” a **utilização alta** e **capacidade insuficiente**.
- Construir um método prático para encontrar gargalos em simulação (e no mundo real).

## Roteiro sugerido (minutos)
- 0–10: definição + sinais de gargalo
- 10–25: \(\rho\) e “operar no limite”
- 25–40: analogia restaurante ↔ planta (restrição de vazão)
- 40–55: método em 3 evidências (sem achismo)
- 55–70: desafio (intervenções e comparação)

---

## Conceitos-chave
- Gargalo como restrição dominante do throughput
- Utilização alta (\(\rho \approx 1\)) e acúmulo antes da etapa
- Intervenção “no gargalo” vs intervenção “fora do gargalo”

## 1) O que é gargalo em linguagem simples
Um gargalo é a etapa que “manda” no sistema:
- quando ela fica lenta, todo mundo atrás dela acumula;
- quando ela fica rápida, o sistema inteiro melhora.

No restaurante, exemplos comuns:
- caixa com poucos atendentes;
- buffet lento (fila para servir);
- mesas insuficientes (ocupação trava o fluxo).

---

## 2) Dois sinais clássicos de gargalo
### Sinal A: fila persistente “na frente” da etapa
Se a fila do caixa fica grande **mesmo fora do pico**, desconfie do caixa.

### Sinal B: etapa com alta utilização
Utilização é “quanto tempo a etapa passa ocupada”.

\[
\rho = \frac{\lambda}{\mu}
\]

Quando \(\rho\) chega perto de 1, a etapa opera “no limite” e vira fonte de fila.

---

## 3) Gargalo no restaurante vs restrição em planta química (analogia validada)
| Restaurante | Planta química | Ideia equivalente |
|---|---|---|
| Caixa limita saída | Válvula/linha limita vazão | restrição de capacidade |
| Mesas lotadas travam entrada | Tanque cheio bloqueia alimentação | capacidade máxima/overflow |
| Buffet lento acumula fila | Operação unitária lenta acumula holdup | unidade dominante |

**Tradução mental:** gargalo em serviços ↔ restrição de vazão em processos.

---

## 4) Método de engenharia: como encontrar gargalo sem “achismo”
Use 3 evidências ao mesmo tempo:
- **(1) Onde a fila cresce?** (acúmulo antes da etapa)
- **(2) Qual recurso fica mais tempo ocupado?** (utilização maior)
- **(3) Qual etapa aumenta o tempo total (W) quando piora um pouco?** (sensibilidade)

Se duas ou três apontarem para o mesmo lugar, você achou o gargalo.

---

## 5) Mini-código em Python: medindo utilização (esqueleto)
Mesmo sem o simulador completo, a lógica é:

```python
tempo_total = 3600  # 1 hora (segundos)
tempo_ocupado_caixa = 0

for t in range(tempo_total):
    caixa_ocupado = (cliente_em_atendimento_no_caixa(t) is not None)
    if caixa_ocupado:
        tempo_ocupado_caixa += 1

utilizacao_caixa = tempo_ocupado_caixa / tempo_total
print(utilizacao_caixa)
```

Se a utilização do caixa está muito alta e existe fila antes dele, ele é um forte candidato a gargalo.

---

## Atividade: “gargalo muda com o cenário”
Responda (sem rodar nada ainda):
- Em horário vazio, qual você acha que é o gargalo? (pode ser nenhum)
- Em horário de pico, o gargalo muda? Por quê?

Isso prepara seu cérebro para a ideia: gargalo é **contextual**, depende de \(\lambda\), variabilidade e capacidades.

---

## Desafio de Simulação (Aula 04)
**Objetivo**: mostrar que “melhorar um ponto” nem sempre melhora o sistema (se não for o gargalo).

1) Escolha um cenário base (parâmetros e layout).
2) Faça duas intervenções separadas:
- **Intervenção 1**: aumente a capacidade do caixa (ex.: mais caixas/atendentes).
- **Intervenção 2**: aumente a capacidade das mesas (ex.: mais lugares).

3) Em cada intervenção, compare:
- throughput
- tempo médio de espera
- tamanho máximo das filas
- utilização (se o relatório trouxer)

4) Conclusão:
- Qual intervenção “mexeu” mais no throughput?
- O que isso revela sobre o gargalo no seu cenário?

### Entrega (curta)
Uma tabela:
| Cenário | Mudança | Throughput | Espera média | Maior fila | Interpretação (gargalo) |
|---|---|---:|---:|---:|---|
| Base | — | … | … | … | … |
| Int. 1 | … | … | … | … | … |
| Int. 2 | … | … | … | … | … |

