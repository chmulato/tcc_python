# Aula 01 — O Mundo em Fluxo: o que são sistemas?

> **Contexto deste repositório:** estas aulas usam o **restaurante universitário** como estudo de caso para ensinar
> **Engenharia de Processos**. O objetivo é você enxergar o restaurante como um **Sistema de Eventos Discretos (DES)**,
> igual aos modelos usados em plantas industriais.
>
> Leitura de apoio: `index.html` (paper interativo), `README.md` (case) e `SIMULATING.md` (detalhes de simulação).

## Guia rápido
- **Tempo estimado**: 20–30 min
- **Pré-requisitos**: nenhum (comece por aqui)
- **Materiais**:
  - este repositório (`README.md`, `index.html`, `SIMULATING.md`)
  - Python + terminal (para rodar `python main.py`)
  - (opcional) `docs/figuras/fig_02a_fluxo_servico.png`

## Objetivo da aula
Entender o que é um **sistema** (entrada → processamento → saída) e por que o “restaurante” do simulador é um excelente exemplo para explicar processos industriais.

---

## Explicação simples (analogia do dia a dia)
Imagine um restaurante universitário em horário de almoço:

- **Entram pessoas** (chegadas).
- Elas **passam por etapas** (pegar comida, pagar, sentar).
- No final, elas **saem**.

Isso é exatamente como qualquer sistema de produção: **algo entra**, **é transformado**, e **algo sai**.

[Imagem: Fluxograma simples “Entrada → Processo → Saída”】【restaurante→]

Sugestão de figura do projeto: `docs/figuras/fig_02a_fluxo_servico.png`.

### Um modelo mental útil
Pense em três perguntas:

1. **O que entra?** (pessoas por minuto)
2. **O que acontece lá dentro?** (filas, atendimento, consumo, ocupação)
3. **O que sai?** (pessoas atendidas por minuto)

---

## O salto técnico (termos de Engenharia de Processos)
Na Engenharia de Processos, usamos termos equivalentes:

| No restaurante (serviços) | Termo em processos (indústria) | Ideia central |
|---|---|---|
| Pessoas chegando | **Vazão de alimentação (Feed Rate, \(\lambda\))** | taxa de entrada |
| Etapas (buffet/caixa) | **Operações unitárias** | transformações com capacidade |
| Pessoas sentadas | **Holdup / Inventário em processo (WIP)** | “material” dentro do sistema |
| Pessoas saindo | **Throughput** | taxa de saída |

**Mensagem-chave:** o restaurante é um **Sistema de Eventos Discretos (DES)**. O estado do sistema muda quando ocorrem eventos: chegada, início/fim de atendimento, ocupação/liberação de mesa, saída.

---

## Desafio prático (para testar no software)
1. Rode o simulador:

```sh
pip install -r requirements.txt
python main.py
```

2. Carregue `config/parametros.yaml` e `layouts/layout_padrao.txt`.
3. Execute uma simulação e responda:

- **Quantos clientes foram processados?** (saída total)
- **Qual foi o tempo médio de permanência?** (tempo no sistema)
- **O que parece “segurar” a saída?** (suspeita de gargalo)

Dica: depois, gere as figuras do case:

```sh
python scripts/gerar_figuras.py
```

E observe `docs/figuras/fig_04_throughput.png` (throughput).

Opcional: abra `index.html` e navegue até a seção **Resultados** para ver as figuras já legendadas.

---

## Glossário (termos-chave)
- **Sistema**: conjunto de elementos com entradas, processamento interno e saídas.
- **Entrada (input)**: o que chega ao sistema (ex.: pessoas/min).
- **Processo (process)**: o que acontece dentro (etapas e regras).
- **Saída (output)**: o que o sistema entrega (ex.: atendidos/min).
- **DES (Discrete-Event Simulation)**: simulação baseada em eventos que mudam o estado do sistema.
- **Throughput**: vazão de saída (produção/atendimento efetivo).
- **Holdup / WIP**: acúmulo dentro do sistema (ocupação + filas).

---

## Checklist (ao final desta aula, você deve conseguir…)
- explicar o que é um **sistema** usando “entrada → processamento → saída”.
- apontar, no simulador do restaurante, o que é **entrada** (feed), o que é **processamento** (etapas/recursos) e o que é **saída** (throughput).
- definir, em uma frase, o que é **DES** (simulação por eventos discretos).
- citar (sem fórmulas) o que significam **throughput** e **holdup/WIP**.

---

## Navegação
- **Próxima:** [Aula 02 — A Matemática das Filas](Aula02.md)

