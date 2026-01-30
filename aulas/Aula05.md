# Aula 05 — Ponte industrial: do RU às Terras Raras/ETE (sem perder o rigor)

| Campo | Valor |
|---|---|
| **Público-alvo** | Iniciante (síntese das Aulas 01–04) |
| **Tempo estimado** | 30–45 min |
| **Pré-requisitos** | Aula 01–04 |
| **Entrega** | 1 mapa de analogia + 1 síntese (5 linhas) |

> **Objetivo da aula:** mostrar o que é *transferível*: quando você troca “clientes” por “íons”, você não troca a matemática — você troca o rótulo da entidade. O raciocínio de fluxo (balanço, capacidade, gargalo, variabilidade) permanece.

## Objetivos de aprendizagem

Ao final desta aula, você consegue:

- mapear entidades, buffers, unidades e saídas em um processo industrial de forma qualitativa;
- apontar o que muda (cinética/equilíbrio) e o que não muda (balanço/capacidade/gargalo);
- escrever uma síntese técnica em linguagem acessível.

## Materiais

- Figura de processo: `../docs/figuras/fig_02b_fluxo_processo.png`
- Paper interativo (ponte conceitual): `../docs/index.html`
- (Opcional) README do site: `../docs/README.html`

---

## 1) Intuição: “separar por etapas”

No RU, você “separa” o fluxo por etapas:

- quem ainda está servindo
- quem está pagando
- quem está ocupando mesa (residência)

Em uma rota de separação (hidrometalurgia, por exemplo), você também “separa por etapas”:

- fase aquosa vs fase orgânica
- lavagem (*scrub*)
- re‑extração (*strip*)

O ponto didático aqui não é decorar química, e sim reconhecer **unidades + buffers + restrições**.

---

## 2) O que muda e o que não muda (clareza conceitual)

**Não muda (gramática de engenharia):**

- balanço: Entrada − Saída = Acúmulo (no recorte escolhido)
- capacidade: unidades têm limite (μ efetiva)
- residência: tempo de permanência governa holdup e estabilidade
- gargalo: a etapa limitante governa throughput

**Muda (física do fenômeno):**

- em vez de pessoas, existem espécies químicas (distribuição entre fases)
- em vez de “atendimento”, aparecem fenômenos como **cinética**, **transferência de massa** e **equilíbrio**

### Vocabulário mínimo (para não se perder)

| RU (serviço) | Processo (hidrometalurgia) | Leitura de engenharia |
|---|---|---|
| entidades (clientes) | espécies/íons | “o que se transporta” |
| fila/buffer | tanque/estoque | holdup/inventário |
| buffet/caixa | mixer-settler/coluna/filtro | operações unitárias |
| saída | produto/rejeito | vazão útil/descarga |

---

## 3) Atividade (em sala): mapa de analogias

Faça um mini‑mapa em 6 linhas:

1) Entidade no RU = ____  
2) Entidade no processo = ____  
3) Buffer no RU = ____  
4) Buffer no processo = ____  
5) Gargalo provável no RU = ____  
6) Gargalo provável no processo = ____ (qualitativo)

---

## 4) Desafio (síntese técnica): “por que é universal?”

Escreva 5 linhas completando:

> “A lógica do simulador é universal porque …”

**Requisito:** use pelo menos **2 argumentos** entre: balanço, capacidade, gargalo, variabilidade, residência.

---

## Pain points + mini‑FAQ

**1) Isso não é “simplificar demais” a química?**  
É uma etapa didática: primeiro consolida-se a gramática (fluxo/capacidade/acúmulo). Depois entram as leis específicas (equilíbrio/cinética).

**2) Onde entra “soberania” aqui?**  
Quando você tem um motor/modelo próprio, você reduz tentativa‑e‑erro, acelera desenvolvimento e decide com evidência (cenários).

---

## Checklist de domínio

- Eu separo “o que não muda” (balanço/capacidade) do “que muda” (física/termodinâmica).
- Eu consigo escrever uma síntese técnica em linguagem acessível.

---

## Navegação

- **Anterior:** [Aula 04 — Operações Unitárias](Aula04.md)
- **Próxima:** [Aula 06 — Operando o simulador (decisão baseada em dados)](Aula06.md)
