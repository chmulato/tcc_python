# Guia do Professor — Módulo “Da Fila ao Reator” (Aulas 01–05)

## Visão geral do módulo
Este conjunto de aulas foi desenhado para levar um estudante que “entende filas por intuição” até a compreensão de um **modelo de simulação** (nível universitário) usando a ponte conceitual:

> **Cliente no restaurante** ↔ **Átomo/Íon (entidade) em processo químico**  
> **Fila** ↔ **Acúmulo (holdup/WIP)**  
> **Etapas** ↔ **Operações unitárias / restrições (gargalos)**

O foco é construir repertório em três camadas:
- **Camada 1 (intuição)**: observar entradas/saídas e perceber acúmulo.
- **Camada 2 (matemática mínima)**: \(\lambda\), \(\mu\), \(\rho\) e balanço \(\text{Acúmulo}=\text{Entrada}-\text{Saída}\).
- **Camada 3 (simulação)**: comparar cenários, validar hipóteses e justificar decisões.

---

## Objetivos de aprendizagem (ao final do módulo)
O estudante será capaz de:
- Identificar **entrada, processamento, saída e acúmulo** em sistemas reais.
- Explicar por que filas surgem usando **taxas** (\(\lambda\), \(\mu\)) e **variabilidade**.
- Interpretar filas/ocupação com o balanço \(\text{Acúmulo}=\text{Entrada}-\text{Saída}\).
- Reconhecer **gargalos** e propor intervenções com base em evidência.
- Relatar resultados de simulação com métricas e conclusão justificável.

---

## Preparação (antes da primeira aula)
### Ambiente
- Python 3 instalado
- Dependências do projeto instaladas:

```bash
pip install -r requirements.txt
```

### Arquivos base sugeridos
- `config/parametros.yaml`
- `layouts/layout_padrao.txt`

### Materiais em sala (mínimo)
- Quadro/slide para desenhar “Entrada → Processo → Saída”
- Celular (cronômetro) para coleta de tempos (Aula 02)

---

## Tempo sugerido por aula (pacing)
| Aula | Tema | Tempo sugerido | Produto em sala |
|---:|---|---:|---|
| 01 | Caixa preta (entrada/processo/saída) | 60 min | tabela de medidas (entrada/acúmulo/saída) |
| 02 | Tempo, variabilidade, \(\lambda\), \(\mu\), \(\rho\) | 70 min | comparação “mesma média, variabilidade diferente” |
| 03 | Balanço de massa: acúmulo | 70 min | 3 balanços (caixa/mesa/sistema) |
| 04 | Gargalos e intervenção | 70 min | tabela base vs intervenções |
| 05 | Do restaurante ao reator (síntese) | 80 min | mini-plano de melhoria + justificativa |

Sugestão prática: se o tempo for curto, execute o **desafio** como tarefa de casa e use a aula para discussão dos resultados.

---

## Como conduzir a aula (roteiro padrão)
Use sempre o mesmo padrão (isso reduz carga cognitiva e melhora autonomia do estudante):
- **Aquecimento (5–10 min)**: pergunta do cotidiano (“onde acumula?”).
- **Conceito (15–25 min)**: uma única ideia central + tabela de tradução.
- **Mini-código (5–10 min)**: lógica em Python (sem “otimizar”, só ilustrar).
- **Atividade guiada (10–20 min)**: entrega curta (tabela/frase).
- **Desafio de simulação (20–40 min)**: comparar cenários + registrar métricas.

---

## Rubrica de avaliação (Desafios de Simulação)
Escala sugerida por critério:
- **4 — Excelente**
- **3 — Bom**
- **2 — Básico**
- **1 — Insuficiente**

Pontuação sugerida: 5 critérios × (1 a 4) → **nota de 5 a 20** (ou normalize para 0–10).

### Critérios
| Critério | 4 — Excelente | 3 — Bom | 2 — Básico | 1 — Insuficiente |
|---|---|---|---|---|
| **Definição do sistema** (entrada/saída/acúmulo) | define claramente e sem ambiguidades; identifica onde mede cada métrica | define bem, com pequena imprecisão | define parcialmente (falta 1 componente ou confunde termos) | não define ou define errado |
| **Execução e registro** (cenários, parâmetros) | descreve cenários e parâmetros; resultados tabelados e legíveis | descreve cenários; registro razoável | registra resultados incompletos; parâmetros pouco claros | não registra o suficiente para interpretar |
| **Comparação e evidência** (métricas) | compara com base em 2–4 métricas; destaca trade-offs | compara com base em ao menos 2 métricas | compara com 1 métrica ou sem consistência | não compara / não usa métricas |
| **Justificativa técnica** (bálanço / \(\lambda,\mu,\rho\)) | usa corretamente balanço e/ou \(\rho\) para explicar o comportamento | usa conceitos com pequenas falhas | cita conceitos sem conectar ao resultado | explicação opinativa/sem base |
| **Reprodutibilidade** (qualquer colega consegue repetir) | fornece arquivos/base, mudanças feitas e passos claros | passos claros, faltam pequenos detalhes | passos incompletos | impossível repetir |

### Feedback rápido (frases prontas)
- “Sua conclusão melhorou muito quando você citou **qual métrica mudou** e **por quê**.”
- “Faltou indicar **quais parâmetros** você alterou — sem isso não dá para reproduzir.”
- “A fila cresceu porque, por um período, **Entrada > Saída** (basta você apontar onde isso aparece).”

---

## Dificuldades comuns (e como intervir)
- **Confundir fila com sistema inteiro**: peça para o aluno escrever 3 balanços (Aula 03).
- **Achar que média resolve tudo**: force um caso com variabilidade maior (Aula 02).
- **“Mexer em tudo” ao mesmo tempo**: exigir intervenção de 1 variável por vez e tabela base vs mudança (Aula 04).
- **Conclusão sem evidência**: exigir “2 métricas + 2 frases” como formato mínimo.

---

## Sugestão de nota do módulo (opcional)
- 20%: atividades em sala (entregas curtas)
- 60%: desafios de simulação (rubrica)
- 20%: síntese final (Aula 05 — plano de melhoria e justificativa)

