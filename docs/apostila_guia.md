# Apostila Guia (Dual Reality) — Do RU à Engenharia Química

> **Objetivo**: estudar os **mesmos fenômenos** em dois “universos” (serviços e processos químicos) e aprender a traduzir intuição em **engenharia**.
>
> - **Sala RU**: fluxo de pessoas, filas, capacidade e variabilidade (DES).
> - **Sala Industrial**: fluxo de material, balanços, residência e gargalos (processos químicos).
>
> **Entrada rápida**: `portal.html` (Sala Digital) • `index.html` (paper interativo / case) • `docs/tcc.html` (documentação técnica)

---

## Como usar esta apostila

- **Leia o “Box de Analogia”** no começo de cada capítulo (cotidiano → industrial).
- Primeiro, entenda com linguagem simples (método **Feynman**). Depois, suba o rigor: **Balanço de Massa**, **Termodinâmica**, **Cinética**, **Tempo de Residência**.
- Sempre que aparecer “🔗 Código”, clique e veja **onde a teoria acontece no simulador**.

---

## Mapa de imagens estratégicas (e placeholders)

> **Você pode substituir os placeholders** abaixo por infográficos próprios, mantendo os títulos/captions como guia editorial.

### IMAGEM 1 — O Fluxograma (paralelo visual RU ↔ P&ID simplificado)

- **RU (serviços)**: bandejas/minuto → buffers (filas) → serviço (buffet/caixa) → residência (mesa) → saída
- **Industrial (processo)**: correntes → reator (τ) → separação → produto

> **Sugestão de arte**: duas “linhas” lado a lado, com a mesma topologia (entrada → blocos → saída), mudando apenas os rótulos.

**Placeholder já disponível no repositório:**
- `docs/figuras/fig_02a_fluxo_servico.png`
- `docs/figuras/fig_02b_fluxo_processo.png`

### IMAGEM 2 — O Acúmulo (Holdup) (fila ↔ volume de controle de tanque)

- **RU**: fila crescendo = “material” acumulando antes da etapa limitante
- **Industrial**: tanque enchendo = acúmulo no volume de controle

**Placeholder já disponível no repositório:**
- `docs/figuras/fig_05_ocupacao_e_filas.png` (holdup e buffers ao longo do tempo)

### IMAGEM 3 — O Gargalo (pressão/vazão ↔ taxa de caixa)

- **RU**: o caixa tem capacidade \(\mu\). Se \(\lambda \to \mu\), a fila explode.
- **Industrial**: quando a “demanda” excede a curva de capacidade, a queda de pressão/limitação de vazão domina (gargalo).

**Placeholder recomendado (a criar):**
- um gráfico “capacidade vs demanda” (curva) com uma região de saturação e anotação de “gargalo”.
  - Alternativamente: use `docs/figuras/fig_04_throughput.png` como base para um infográfico híbrido (capacidade → throughput).

---

## Capítulo 1 — O Fluxograma (a mesma história em dois rótulos)

### Box de Analogia (RU ↔ Industrial)

- **No RU**: pessoas entram, esperam, são atendidas, ocupam mesas e saem.
- **Na indústria**: material entra, espera/estoca, reage/se transforma, acumula em volumes e sai como produto.

### Feynman (explicação simples)

Pense no sistema como uma sequência de “caixas” conectadas por setas. As caixas têm **capacidade**. Se entra mais do que sai, o sistema **acumula** (fila/estoque).

### Tradução para Engenharia Química

- **Entrada**: alimentação \(F\) (ou taxa de chegada \(\lambda\))
- **Operação unitária**: reator/serviço com taxa de processamento \(\mu\)
- **Buffer**: inventário em processo (WIP/holdup)
- **Saída**: produção/throughput \(Q\)

**Placeholders (use como figuras do capítulo):**

![IMAGEM 1A — Fluxo em sistema de serviços (DES)](figuras/fig_02a_fluxo_servico.png)

![IMAGEM 1B — Fluxo em sistema de processo (engenharia química)](figuras/fig_02b_fluxo_processo.png)

<details>
<summary><strong>Curiosidade técnica</strong>: por que “fluxograma” já é um balanço implícito?</summary>

Qualquer setinha no fluxograma sugere uma contabilidade: *o que passa por aqui por unidade de tempo*. Isso é literalmente o começo de um balanço de massa (ou de entidades).
</details>

---

## Capítulo 2 — O Acúmulo (Holdup): quando “some” gente (ou material)

### Box de Analogia (RU ↔ Industrial)

- **RU**: “cadê todo mundo?” → está no **buffer** (fila) ou no **volume de residência** (mesas).
- **Industrial**: “cadê o material?” → está no **tanque/reator** (holdup) ou em **linhas/vasos** (inventário).

### Feynman (explicação simples)

Se você fecha parcialmente uma saída (capacidade limitada), o “tráfego” se acumula. Esse acúmulo **não é erro**: é o estado do sistema mudando.

### Tradução para Engenharia Química

O holdup é o **acúmulo dentro do volume de controle**. Em engenharia:

\[
\text{Entrada} - \text{Saída} + \text{Geração} - \text{Consumo} = \text{Acúmulo}
\]

**Placeholder do capítulo:**

![IMAGEM 2 — Holdup e buffers por minuto](figuras/fig_05_ocupacao_e_filas.png)

<details>
<summary><strong>Curiosidade técnica</strong>: holdup vs WIP vs inventário</summary>

- **Holdup**: quantidade “retida” dentro de um equipamento/volume.
- **WIP (work-in-process)**: inventário em processo entre etapas.
- **Fila**: WIP em forma operacional (entidades aguardando capacidade).
</details>

---

## Capítulo 3 — O Gargalo: a etapa que governa o sistema

### Box de Analogia (RU ↔ Industrial)

- **RU**: um caixa lento domina o tempo total → filas crescem “a montante”.
- **Industrial**: uma válvula, bomba, trocador, ou reator pode dominar a vazão → o resto “espera”.

### Feynman (explicação simples)

Se uma etapa é a mais lenta, ela vira o **ritmo** do sistema. Melhorar outras etapas ajuda pouco enquanto o gargalo não mudar.

### Tradução para Engenharia Química

O gargalo é a **restrição ativa**: a etapa com maior utilização ou maior espera média. Em regime próximo de saturação:

- \(\rho = \lambda/\mu\) (quando \(\rho \to 1\), a fila explode)

🔗 **Código (identificação de gargalo no DES)**: o simulador compara KPIs das estações para estimar o gargalo por utilização/espera.

<details>
<summary><strong>Curiosidade técnica</strong>: gargalo não é “o que está cheio”, é “o que limita”</summary>

Um buffer cheio pode ser apenas o sintoma. O gargalo é a causa: a etapa cuja capacidade efetiva governa o throughput.
</details>

---

## Capítulo 4 — Tempo de Residência: \( \tau = V/Q \) (o coração do “motor matemático”)

### Box de Analogia (RU ↔ Industrial)

- **RU**: quanto maior o “volume do restaurante” (pessoas ocupando mesas/filas), ou menor a vazão de saída, maior o tempo médio no sistema.
- **Industrial**: quanto maior o volume do reator/tanque (ou holdup) e menor a vazão, maior a residência → afeta conversão, estabilidade e controle.

### Feynman (explicação simples)

Imagine uma banheira:

- **V** = quantidade de água na banheira (volume).
- **Q** = quanta água sai por minuto.

Se a banheira tem 100 litros e saem 10 L/min, uma “gota média” fica cerca de **10 minutos** lá dentro. Isso é \( \tau = V/Q \).

### Tradução para Engenharia Química (rigor)

\[
\tau = \frac{V}{Q}
\]

Onde:

- \(V\): volume de controle (ou holdup médio equivalente)
- \(Q\): vazão volumétrica (ou vazão de entidades, em “pessoas/min”)

No contexto do RU, é útil pensar em:

- \(V \approx \text{número médio de pessoas no sistema}\)
- \(Q \approx \text{throughput (pessoas/min)}\)

Isso é a forma intuitiva da **Lei de Little**:

\[
L = \lambda W \quad \Rightarrow \quad W = \frac{L}{\lambda}
\]

Aqui, \(W\) é o tempo médio no sistema (residência), \(L\) o número médio no sistema (holdup) e \(\lambda\) a taxa de chegada (em regime).

### Trecho de “código pedagógico” (didático)

```python
# τ = V / Q
# V: "volume" médio no sistema (ex.: pessoas médias no RU / holdup)
# Q: vazão de saída (ex.: pessoas por minuto)

def tempo_de_residencia(V: float, Q: float) -> float:
    if Q <= 0:
        return 0.0
    return V / Q
```

### Como o simulador calcula o tempo de residência (na prática)

No DES, o simulador mede \( \tau \) **por entidade** como o tempo entre chegada e saída:

- \(dt = t_{out} - t_{in}\)
- e depois calcula a média.

🔗 **Código (residence time no DES)**:
`https://github.com/chmulato/tcc_python/blob/main/src/simulador.py#L617-L703`

🔗 **Código (histograma do tempo de residência / Fig 06)**:
`https://github.com/chmulato/tcc_python/blob/main/scripts/gerar_figuras.py#L261-L270`

<details>
<summary><strong>Curiosidade técnica</strong>: por que \( \tau = V/Q \) continua válido em DES?</summary>

Mesmo com variabilidade, a relação aparece como **média** em regime: o sistema oscila, mas o “orçamento” de fluxo ainda existe.
</details>

---

## Capítulo 5 — Do simples ao acadêmico: Termodinâmica e Cinética (ponte conceitual)

### Box de Analogia (RU ↔ Industrial)

- **RU**: tempo de serviço é como “velocidade” de uma etapa; variar o tempo muda filas.
- **Industrial**: cinética/termodinâmica mudam taxas efetivas e equilíbrio; isso muda acúmulos e vazões.

### Feynman (explicação simples)

Uma etapa “fica lenta” por algum motivo (poucos caixas, procedimento mais demorado, equipamento limitante). O sistema então se reorganiza: filas crescem e o throughput se estabiliza em outro patamar.

### Tradução para Engenharia Química

- **Cinética**: taxa de reação (equivalente à taxa de serviço \(\mu\) no modelo de filas).
- **Termodinâmica**: limitações de equilíbrio (equivalente a “não dá para passar de um certo ponto” mesmo aumentando esforço).
- **Transferência** (massa/energia/momento): limitações que criam gargalos “de transporte”.

<details>
<summary><strong>Curiosidade técnica</strong>: “pessoa” e “molécula” são a mesma entidade matemática</summary>

O que muda é a interpretação do estado e das taxas. O motor de simulação observa **entidades**, **eventos** e **restrições**.
</details>

---

## Apêndice A — Figuras e reprodutibilidade (infografia com rastreabilidade)

Para regenerar as figuras do case usadas no `index.html`, rode:

```bash
python scripts/gerar_figuras.py
```

🔗 **Código (pipeline de figuras)**:
`https://github.com/chmulato/tcc_python/blob/main/scripts/gerar_figuras.py`

---

## Apêndice B — Onde estudar a teoria “dentro do código”

- **Tempo de residência / média do ciclo**: `src/simulador.py` (cálculo por entidade e agregação)
  - 🔗 `https://github.com/chmulato/tcc_python/blob/main/src/simulador.py#L617-L703`
- **Throughput / holdup / filas (séries)**: `scripts/gerar_figuras.py` (figuras 04–06)
  - 🔗 `https://github.com/chmulato/tcc_python/blob/main/scripts/gerar_figuras.py#L230-L270`

