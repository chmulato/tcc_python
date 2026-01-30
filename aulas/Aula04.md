# Aula 04 — Operações Unitárias: o RU como “flowsheet” (mesa = residência)

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (já fez Aula 01–03) |
| **Tempo estimado** | 30–40 min |
| **Pré-requisitos** | Aula 01–03 |
| **Entrega** | 1 comparação (2 cenários) + 1 justificativa (3 linhas) |

> **Ideia central:** buffet/caixa/mesa podem ser tratados como **operações unitárias** (unidades com capacidade e tempo). A “mesa” funciona como uma unidade de **residência**: aumentar o tempo médio de permanência eleva holdup e pode reduzir throughput.

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- descrever o RU como um **flowsheet** (unidades + correntes);
- mapear capacidade (μ) e tempos (serviço/residência);
- explicar por que aumentar a residência (τ) aumenta holdup/WIP.

## Materiais

- Figuras: `../docs/figuras/fig_02a_fluxo_servico.png`, `../docs/figuras/fig_02b_fluxo_processo.png`, `../docs/figuras/fig_03_layout_base.png`
- Simulador: `python main.py`

---

## 1) Intuição: “estações” em série

No RU você percorre “estações”:

1) entrada (chegada)  
2) buffet (serviço)  
3) caixa (serviço)  
4) mesa (permanência)  
5) saída

Cada estação tem:

- **capacidade** (quantos atende/acomoda)
- **tempo** (quanto tempo cada entidade permanece ali)

---

## 2) Tradução: serviço ↔ operação unitária

Em processos, um flowsheet conecta unidades (tanques, reatores, separadores) por correntes.

| RU | Processo | Leitura de engenharia |
|---|---|---|
| fila | buffer/tanque | acúmulo (holdup) |
| buffet/caixa | unidade com capacidade | taxa efetiva (μ) |
| mesa | “volume” de residência | tempo médio de permanência (τ) governa holdup |
| entrada/saída | correntes | vazões (λ / throughput) |

Relação útil (interpretação, não cálculo rígido):

```text
τ ≈ Holdup / Vazão
```

---

## 3) Desafio de simulação (reprodutível): efeito residência

> **Objetivo:** manter o resto constante e alterar apenas `tempo_medio_almoco`.

1) Rode dois cenários:

- **Cenário A:** `tempo_medio_almoco = 30` min
- **Cenário B:** `tempo_medio_almoco = 45` min

2) Compare:

- uso médio de mesas (ou ocupação média)
- tempo médio no sistema
- fila para mesa (se existir) e throughput

3) Conclusão (3 linhas):

> “Ao aumentar τ (tempo médio de almoço), o holdup ____ porque ____.”  
> “O efeito esperado no throughput é ____ porque ____.”

> **Dica:** gere figuras e compare `fig_04_throughput.png` vs `fig_05_ocupacao_e_filas.png`.

---

## Pain points + mini‑FAQ

**1) Mesa é “reator”?**  
É uma analogia funcional: a mesa retém entidades por um tempo (residência), como um volume de processo retém material.

**2) Por que residência afeta throughput?**  
Porque capacidade física (mesas/cadeiras) limita holdup máximo. Se τ aumenta, o sistema fica “mais cheio” por mais tempo e pode bloquear novas entradas.

---

## Checklist de domínio

- Eu descrevo o RU como unidades conectadas (flowsheet).
- Eu sei explicar “mesa = residência” e o efeito em holdup.

---

## Navegação

- **Anterior:** [Aula 03 — Balanço](Aula03.md)
- **Próxima:** [Aula 05 — Ponte industrial (RU ↔ íons/ETE)](Aula05.md)

