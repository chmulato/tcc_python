# Aula 05 — Hidrometalurgia Seletiva: do restaurante às Terras Raras (ponte conceitual)

> **Contexto deste repositório:** o restaurante é a **Prova de Conceito (PoC)**.
> Nesta aula, a ideia é mostrar **como a mesma lógica** pode ser levada para simuladores industriais (ex.: Terras Raras / ETE).
> Você não precisa conhecer química avançada ainda — foque no raciocínio: fluxo, balanço, gargalo e variabilidade.

## Guia rápido
- **Tempo estimado**: 30–45 min
- **Pré-requisitos**: Aula 01–04 (fluxo, filas, balanço e operações unitárias)
- **Materiais**:
  - `docs/figuras/fig_02b_fluxo_processo.png` (fluxo em processo)
  - `README.md` (seção “Evolução Tecnológica”, PoC → ETE/Terras Raras)
  - papel e caneta (para mapear analogias “pessoas ↔ íons”)

## Objetivo da aula
Entender como a lógica de **fluxo + balanço + gargalos + variabilidade** se mantém quando trocamos “pessoas” por “íons” e “mesas/filas” por “tanques/operações de separação”.

---

## Explicação simples (analogia do dia a dia)
No restaurante, você quer “separar” pessoas por etapas:

- quem ainda não pegou comida
- quem está pagando
- quem está comendo

Na hidrometalurgia, você quer separar espécies químicas (íons) em etapas:

- quem está na fase aquosa
- quem migrou para a fase orgânica
- quem foi “lavado” (scrub)
- quem foi “re-extraído” (strip)

[Imagem: “linha de separação” com tanques em série]

---

## O salto técnico (o que muda e o que não muda)
O que **não muda**:

- **Balanço**: o que entra deve sair ou acumular.
- **Capacidade**: tanques, misturadores, decantadores e colunas têm limites.
- **Tempo de residência**: controla conversão, separação e holdup.
- **Gargalos**: uma etapa lenta domina o throughput global.

O que **muda**:

- Em vez de “pessoas”, você tem **espécies químicas** com distribuição entre fases.
- Em vez de “fila”, você tem **inventário de solução/polpa** (volume, concentração).
- Em vez de “atendimento”, você tem **cinética, transferência de massa e equilíbrio químico**.

### Vocabulário mínimo (para não se perder)
| Restaurante | Hidrometalurgia | Leitura de engenharia |
|---|---|---|
| Entidades (clientes) | Espécies / íons | “o que se transporta” |
| Fila/buffer | Tanque/estoque | holdup/inventário |
| Etapas (buffet/caixa) | Mixer-settler / colunas / filtros | operações unitárias |
| “Sair do sistema” | Produto / rejeito | vazão de saída |

---

## Desafio prático (transferência de raciocínio)
Sem mexer no código, faça este exercício mental:

1) No restaurante, qual mudança tende a **reduzir holdup** sem reduzir throughput?
   - reduzir tempo médio de permanência (τ)
   - aumentar capacidade de uma etapa gargalo (μ)
   - reduzir variabilidade na chegada

2) Agora traduza para hidrometalurgia:

- “reduzir τ” → reduzir tempo de residência em tanques? (impacta extração/eficiência)
- “aumentar μ” → aumentar capacidade de separação (mais estágios/unidades em paralelo)
- “reduzir variabilidade” → estabilizar feed (concentração/vazão) por controle de processo

Escreva a resposta em 5 linhas usando a frase:

> “A lógica do simulador é universal porque …”

---

## Glossário (termos-chave)
- **Hidrometalurgia**: extração de metais por rotas em solução.
- **Seletividade**: capacidade de separar espécies (preferência por um íon).
- **Mixer-settler**: operação unitária de mistura + decantação (separação de fases).
- **Extração / Scrub / Strip**: estágios típicos de separação em SX.
- **Transferência de massa**: movimento de espécie entre fases (governa velocidade).

---

## Checklist (ao final desta aula, você deve conseguir…)
- explicar, sem fórmulas, por que **fluxo + balanço + capacidade** também descrevem separação de íons em tanques.
- mapear “fila/buffer” do restaurante para “tanque/inventário” na hidrometalurgia.
- dar exemplos de onde entram **transferência de massa** e **equilíbrio** (o que muda vs serviços).
- escrever a frase “a lógica é universal porque…” com pelo menos 2 argumentos técnicos.

---

## Navegação
- **Anterior:** [Aula 04 — O Restaurante como Reator](Aula04.md)
- **Próxima:** [Aula 06 — Operando o Simulador](Aula06.md)

