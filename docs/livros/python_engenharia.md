---

![CAPA](imagens/01_capa.png)

---

![SOBRECAPA](imagens/02_capa.png)

---

### Título: Introdução à Programação Python Aplicada à Engenharia
### Autor: Christian Vladimir Uhdre Mulato

### Sumário

1. [Apresentação](#1-apresentação)
2. [Fundamentos da Programação em Python](#2-fundamentos-da-programação-em-python)
    - [2.1. Tipos de Dados em Python](#21-tipos-de-dados-em-python)
        - [2.1.1. Inteiros (INT)](#211-inteiros-int)
        - [2.1.2. Números de Ponto Flutuante (FLOAT)](#212-números-de-ponto-flutuante-float)
        - [2.1.3. Cadeias de Caracteres (STR)](#213-cadeias-de-caracteres-str)
        - [2.1.4. Booleanos (BOOL)](#214-booleanos-bool)
        - [2.1.5. Exemplo: Cálculo da Tensão em um Resistor](#215-exemplo-cálculo-da-tensão-em-um-resistor)
        - [2.1.6. Exemplo: Simulação da Trajetória de um Projétil](#216-exemplo-simulação-da-trajetória-de-um-projétil)
    - [2.2. Operadores Aritméticos e Lógicos em Python](#22-operadores-aritméticos-e-lógicos-em-python)
        - [2.2.1. Operadores Aritméticos](#221-operadores-aritméticos)
        - [2.2.2. Operadores Lógicos](#222-operadores-lógicos)
        - [2.2.3. Exemplos Aplicados à Engenharia](#223-exemplos-aplicados-à-engenharia)
        - [2.2.4. Exercício Proposto: Cálculo de Área e Perímetro de um Terreno e Verificação de Viabilidade](#224-exercício-proposto-cálculo-de-área-e-perímetro-de-um-terreno-e-verificação-de-viabilidade)
        - [2.2.5. Exercício Proposto: Análise da Deformação de uma Viga](#225-exercício-proposto-análise-da-deformação-de-uma-viga)
        - [2.2.6. Curiosidade – Mecânica dos Sólidos](#226-curiosidade--mecânica-dos-sólidos)
    - [2.3. Entrada e Saída de Dados em Python](#23-entrada-e-saída-de-dados-em-python)
        - [2.3.1. Entrada de Dados: input()](#231-entrada-de-dados-input)
        - [2.3.2. Saída de Dados: print()](#232-saída-de-dados-print)
        - [2.3.4. Exercício Proposto: Cálculo de Conversão em um Reator](#234-exercício-proposto-cálculo-de-conversão-em-um-reator)
        - [Figura 2.3.1 – Esquema Técnico](#figura-231--esquema-técnico)
    - [2.4. Primeiros Cálculos Aplicados à Engenharia](#24-primeiros-cálculos-aplicados-à-engenharia)
        - [2.4.1. Engenharia Civil: Cálculo da Área de uma Viga](#241-engenharia-civil-cálculo-da-área-de-uma-viga)
        - [2.4.2. Engenharia Elétrica: Lei de Ohm](#242-engenharia-elétrica-lei-de-ohm)
        - [2.4.3. Engenharia Mecânica: Energia Potencial Gravitacional](#243-engenharia-mecânica-energia-potencial-gravitacional)
        - [2.4.4. Engenharia Química: Vazão Molar](#244-engenharia-química-vazão-molar)
        - [2.4.5. Engenharia Ambiental: Cálculo de Concentração](#245-engenharia-ambiental-cálculo-de-concentração)
    - [2.5. Conclusão](#25-conclusão)
3. [Estrutura de Controle](#3-estrutura-de-controle)
    - [3.1. Condicionais: if, elif, else](#31-condicionais-if-elif-else)
        - [3.1.1. A estrutura if](#311-a-estrutura-if)
        - [3.1.2. A estrutura if-else](#312-a-estrutura-if-else)
        - [3.1.3. A estrutura if-elif-else](#313-a-estrutura-if-elif-else)
        - [3.1.4. Exercício Proposto: Classificação de Solos](#314-exercício-proposto-classificação-de-solos)
        - [3.1.5. Curiosidade – Engenharia Civil](#315-curiosidade--engenharia-civil)
        - [3.1.6. Conclusão](#316-conclusão)
    - [3.2. Laços de Repetição: for, while](#32-laços-de-repetição-for-while)
        - [3.2.1. O laço for](#321-o-laço-for)
        - [3.2.2. O laço while](#322-o-laço-while)
        - [3.2.3. Exercício Proposto: Simulação de um Reator Batelada Isotérmico](#323-exercício-proposto-simulação-de-um-reator-batelada-isotérmico)
        - [3.2.4. Curiosidade – Engenharia Química](#324-curiosidade--engenharia-química)
        - [3.2.5. Conclusão](#325-conclusão)
    - [3.3. Aplicações Práticas em Verificação de Condições Operacionais](#33-aplicações-práticas-em-verificação-de-condições-operacionais)
        - [3.3.1. Monitoramento de Temperatura em um Reator Químico](#331-monitoramento-de-temperatura-em-um-reator-químico)
        - [3.3.2. Controle de Nível em um Tanque](#332-controle-de-nível-em-um-tanque)
        - [3.3.3. Verificação de Pressão em um Sistema de Tubulação](#333-verificação-de-pressão-em-um-sistema-de-tubulação)
        - [3.3.4. Contagem de Ciclos de um Equipamento](#334-contagem-de-ciclos-de-um-equipamento)
        - [3.3.5. Análise de Dados de Sensores](#335-análise-de-dados-de-sensores)
    - [3.4. Conclusão](#34-conclusão)
4. [Funções e Modularizações](#44-funções-e-modularizações)
    - [4.1. Definição de Funções](#41-definição-de-funções)
        - [4.1.1. Sintaxe de Definição de Função](#411-sintaxe-de-definição-de-função)
        - [4.1.2. Exemplo de Definição de Função](#412-exemplo-de-definição-de-função)
        - [4.1.3. Benefícios do Uso de Funções](#413-benefícios-do-uso-de-funções)
    - [4.2. Parâmetros e Retorno](#42-parâmetros-e-retorno)
        - [4.2.1. Parâmetros](#421-parâmetros)
        - [4.2.2. Retorno](#422-retorno)
        - [4.2.3. Benefícios de Parâmetros e Retorno](#423-benefícios-de-parâmetros-e-retorno)
    - [4.3. Organização de Código em Módulos Reutilizáveis](#43-organização-de-código-em-módulos-reutilizáveis)
        - [4.3.1. O que são Módulos?](#431-o-que-são-módulos)
        - [4.3.2. Criando Módulos](#432-criando-módulos)
        - [4.3.3. Importando Módulos](#433-importando-módulos)
        - [4.3.4. Benefícios da Modularização](#434-benefícios-da-modularização)
        - [4.3.5. Exemplo de Uso de Módulos](#435-exemplo-de-uso-de-módulos)
        - [4.3.5 Exercício Proposto: Gestão de Inventário Florestal](#435-exercício-proposto-gestão-de-inventário-florestal)
    - [4.4. Conclusão](#44-conclusão)

---

## 1. Apresentação

A presente apostila tem como objetivo introduzir os conceitos fundamentais de programação em linguagem Python com foco na aplicação em problemas práticos de engenharia. Python é uma linguagem moderna, acessível e amplamente adotada nas áreas de ciência, tecnologia e automação de processos industriais. Seu ecossistema rico em bibliotecas permite que engenheiros realizem desde simples análises numéricas até simulações e otimizações complexas com rapidez e precisão.
O conteúdo foi organizado em módulos progressivos, partindo dos fundamentos da programação até aplicações reais por meio de projetos. A ideia é desenvolver a lógica de programação, incentivar a experimentação e fortalecer a capacidade de modelar problemas de engenharia utilizando ferramentas computacionais.

Ao final, o leitor será capaz de:

- Compreender os principais conceitos da linguagem Python.
- Resolver problemas matemáticos aplicados à engenharia com auxílio de bibliotecas como NUM_PY, PANDAS, MAT_PLOT_LIB e SCI_PY.
- Modelar, simular e visualizar sistemas físicos e processos.
- Desenvolver soluções computacionais práticas com uma abordagem estruturada.

Esta apostila é indicada para estudantes de cursos técnicos e superiores em engenharia e áreas afins, bem como profissionais que desejam iniciar no uso da programação para aplicações técnicas.

Boa leitura e bons estudos!

- Christian V. Uhdre Mulato
- Engenheiro Químico e Desenvolvedor de Sistemas

Campo Largo – PR

---

## 2. Fundamentos da Programação em Python

Este primeiro módulo tem como objetivo estabelecer uma base sólida em programação Python, essencial para todas as aplicações que veremos ao longo desta apostila. Dominar os fundamentos da linguagem é crucial para compreender e desenvolver soluções computacionais eficazes para problemas de engenharia.

Neste módulo, vamos explorar os tipos de dados fundamentais em Python, como números inteiros (INT), números de ponto flutuante (FLOAT), cadeias de caracteres (STR) e valores booleanos (BOOL). Entender como representar e manipular esses diferentes tipos de dados é o primeiro passo para realizar cálculos e processar informações em Python.

Além disso, abordaremos os operadores aritméticos e lógicos, que nos permitem realizar operações matemáticas e tomar decisões lógicas dentro dos nossos programas. A capacidade de realizar cálculos e avaliar condições é fundamental para resolver problemas de engenharia, desde a análise de dados experimentais até a modelagem de sistemas físicos.

Finalmente, introduziremos os conceitos de entrada e saída de dados, ensinando como interagir com o usuário e como ler e escrever informações. Também daremos os primeiros passos na aplicação desses conhecimentos em cálculos simples voltados para a engenharia, preparando o terreno para problemas mais complexos nos módulos seguintes.

Ao concluir estes módulos, você estará apto a escrever programas Python simples, mas poderosos, que podem realizar cálculos, manipular dados e interagir com o mundo exterior, lançando as bases para sua jornada na programação aplicada à engenharia.

---

### 2.1. Tipos de Dados em Python

Em Python, assim como em outras linguagens de programação, os dados são classificados em diferentes tipos. Cada tipo de dado possui características e comportamentos específicos, o que permite ao computador interpretar e manipular as informações corretamente.

Nesta seção, vamos explorar os quatro tipos de dados fundamentais:
- inteiros (INT),
- números de ponto flutuante (FLOAT),
- cadeias de caracteres (STR) e
- booleanos (BOOL).

### 2.1.1. Inteiros (INT)

O tipo de dado int representa números inteiros, ou seja, números que não possuem parte decimal. Eles podem ser positivos, negativos ou zero. 

Exemplos em engenharia: 

- Número de peças em um sistema: numero_pecas = 150
- Quantidade de andares de um edifício: andares = 12
- Número de iterações em um cálculo: iteracoes = 1000

### 2.1.2. Números de Ponto Flutuante (FLOAT)

O tipo de dado `float` representa números reais, ou seja, números que podem possuir uma parte decimal.

Exemplos em engenharia:

- Aceleração da gravidade: `gravidade = 9.81` (m/s²)
- Tensão em um circuito elétrico: `tensao = 220.5` (V)
- Coeficiente de atrito: `atrito = 0.25`
- Vazão de um fluido: `vazao = 2.75` (m³/s)
- Temperatura de um processo: `temperatura = 37.5` (°C)

### 2.1.3. Cadeias de Caracteres (STR)

O tipo de dado `str` representa texto, ou seja, uma sequência de caracteres. As cadeias de caracteres são delimitadas por aspas simples (') ou aspas duplas (").

Exemplos em engenharia:

- Nome de um material: `material = "Aço Carbono"`
- Descrição de um componente: `componente = "Válvula de Segurança"`
- Unidade de medida: `unidade = "MPa"` (MegaPascal)
- Resultado de um ensaio: `resultado_ensaio = "Aprovado"`

### 2.1.4. Booleanos (BOOL)

O tipo de dado `bool` representa valores lógicos, ou seja, verdadeiro (True) ou falso (False). Eles são fundamentais para realizar testes condicionais e controlar o fluxo de execução de um programa.

Exemplos em engenharia:

- Status de um sensor: `sensor_ligado = True`
- Verificação de um limite: `temperatura_acima_limite = False`
- Condição de falha: `falha_detectada = False`
- Estado de uma válvula: `valvula_aberta = True`

Compreender esses tipos de dados é essencial para escrever programas que manipulem informações de forma correta e eficiente em aplicações de engenharia.

### 2.1.5. Exemplo: Cálculo da Tensão em um Resistor

Imagine que você precisa calcular a tensão em um resistor usando a Lei de Ohm (V = I * R),
onde:
- V é a tensão (em Volts)
- I é a corrente (em Amperes)
- R é a resistência (em Ohms)

Além disso, vamos verificar se a potência dissipada no resistor (P = V * I) excede um valor limite. 

**Código em Python:**
```python
# Definição das variáveis

# Corrente elétrica (float)
corrente = 2.0  # Amperes

# Resistência elétrica (float)
resistencia = 10.0  # Ohms

# Limite de potência (float)
potencia_limite = 20.0  # Watts

# Nome do resistor (string)
nome_resistor = "R1"

# Cálculo da tensão (float)
tensao = corrente * resistencia

# Cálculo da potência (float)
potencia = tensao * corrente

# Verificação da potência (bool)
potencia_excede_limite = potencia > potencia_limite

# Exibição dos resultados
print("Cálculo da Tensão e Potência em um Resistor")
print("------------------------------------------")
print("Nome do Resistor:", nome_resistor)
print("Corrente (A):", corrente)
print("Resistência (Ω):", resistencia)
print("Tensão (V):", tensao)
print("Potência (W):", potencia)
print("Potência excede o limite?", potencia_excede_limite)

# Conversão de tipo (demonstração)
# Converter a tensão para inteiro (truncando a parte decimal)
tensao_inteira = int(tensao)
print("Tensão (V, inteiro):", tensao_inteira)
```

**Como usar este código no Visual Studio Code:**

**1.	Abra o Visual Studio Code.**
**2.	Crie um arquivo** (Arquivo > Novo Arquivo) e salve-o com um nome como 01_codigo_calculo_resistor.py.
A extensão .py é importante para que o **VS Code** reconheça que é um arquivo Python.

**3.	Copie e cole o código** acima no arquivo.
**4.	Execute o código:**
- Você pode clicar com o botão direito na janela do editor e selecionar "Executar Python no Terminal".
- Ou você pode usar o atalho Ctrl+Shift+B (ou Cmd+Shift+B no MacOS) se você já tiver configurado uma "Build Task" para Python.
- Ou você pode abrir o terminal integrado do VS Code (Visualizar > Terminal) e digitar python 01_codigo_calculo_resistor.py e pressionar Enter.
**5.	Observe a saída no terminal:** O programa irá imprimir os valores da tensão, potência e a verificação do limite.

**Explicação do Código:**

- **Tipos de Dados:** O código demonstra claramente o uso de float para grandezas físicas como corrente, resistência, tensão e potência, str para o nome do resistor, e bool para o resultado da comparação da potência com o limite.
- **Cálculos:** Realiza cálculos típicos de engenharia elétrica usando os operadores aritméticos * (multiplicação).
- **Tomada de Decisão:** Utiliza uma expressão booleana (potencia > potencia_limite) para simular uma verificação de segurança ou especificação de projeto.
- **Saída Formatada:** Imprime os resultados de forma clara e identificada, o que é crucial para a comunicação de resultados em engenharia.
- **Conversão de Tipo:** A última parte (conversão para int) é um exemplo de como você pode converter um tipo de dado em outro. Note que, neste caso, a parte decimal da tensão é truncada.

Este exemplo prático mostra como os tipos de dados fundamentais são aplicados em um problema simples de engenharia, combinando cálculo, lógica e representação de informações do mundo real.

**Resultado:**

```plaintext
Cálculo da Tensão e Potência em um Resistor
Nome do Resistor: R1
Corrente (A): 2.0
Resistência (Ω): 10.0
Tensão (V): 20.0
Potência (W): 40.0
Potência excede o limite? True
Tensão (V, inteiro): 20
```
---

### 2.1.6. Exemplo: Simulação da Trajetória de um Projétil

Neste exemplo, vamos simular a trajetória de um projétil lançado sob um ângulo e com uma velocidade inicial, e gerar um gráfico da trajetória. Este exemplo combina física básica com a visualização de dados.

**Código em Python:**
```python
import matplotlib.pyplot as plt
import math

# Dados de entrada (tipos float e int)
velocidade_inicial = 20.0  # m/s
angulo_graus = 45       # graus
angulo_radianos = math.radians(angulo_graus) # conversão para radianos
gravidade = 9.81       # m/s²
tempo_total = (2 * velocidade_inicial * math.sin(angulo_radianos)) / gravidade

# Listas para armazenar os pontos da trajetória (listas de floats)
tempos = []
posicoes_x = []
posicoes_y = []

# Cálculo da trajetória
intervalo_tempo = 0.1  # segundos
tempo = 0.0

while tempo <= tempo_total:
    tempos.append(tempo)
    posicao_x = velocidade_inicial * math.cos(angulo_radianos) * tempo
    posicao_y = velocidade_inicial * math.sin(angulo_radianos) * tempo - 0.5 * gravidade * tempo**2
    posicoes_x.append(posicao_x)
    posicoes_y.append(posicao_y)
    tempo += intervalo_tempo

# Nome do projétil (string)
nome_projétil = "Projétil A"

# Geração do gráfico
plt.plot(posicoes_x, posicoes_y)
plt.title("Trajetória de um Projétil")
plt.xlabel("Distância Horizontal (m)")
plt.ylabel("Altura (m)")
plt.grid(True)

# Adicionando informações textuais ao gráfico
plt.text(0, max(posicoes_y) * 0.9, f"Velocidade Inicial: {velocidade_inicial} m/s", fontsize=9)
plt.text(0, max(posicoes_y) * 8, f"Ângulo: {angulo_graus} graus", fontsize=9)
plt.text(0, max(posicoes_y) * 0.7, nome_projétil, fontsize=12, color='red')

plt.show()

# Imprimindo informações relevantes (demonstração de uso de tipos)
print(f"Tempo total de voo: {tempo_total:.2f} s")  # Formatação de float
print(f"Tipo da variável 'nome_projétil': {type(nome_projétil)}") # Mostrando o tipo
print(f"A altura máxima atingida foi: {max(posicoes_y):.2f} m")
```
**Como usar este código no Visual Studio Code:**
1. **Abra o Visual Studio Code.**
2. **Crie um arquivo** e salve-o como 02_codigo_trajetoria_projetil.py.
3. **Copie e cole o código** acima no arquivo.
4. **Certifique-se de ter o Matplotlib instalado.** Se não tiver, abra o terminal no VS Code e digite: pip install matplotlib e pressione Enter.
5. **Execute o código** da mesma forma que no exemplo anterior.
6. **Observe a saída:** Além da saída no terminal, uma janela com o gráfico da trajetória do projétil será exibida.

**Explicação do Código:**

**Tipos de Dados:**
- **FLOAT:** Usado para velocidade, ângulo (em radianos), gravidade, tempo e as posições x e y.
- **INT:** Usado para o ângulo em graus.
- **STR:** Usado para o nome do projétil.
- **LIST:** Usado para armazenar sequências de valores de tempo, posições x e posições y. Listas são estruturas de dados que armazenam múltiplos valores do mesmo tipo (neste caso, float).

**Cálculos:** O código realiza cálculos de física para determinar a trajetória do projétil, decompondo a velocidade inicial em componentes horizontal e vertical e usando as equações do movimento uniformemente variado.

**Visualização:** A biblioteca matplotlib.pyplot é usada para criar o gráfico da trajetória. plt.plot() desenha a linha, plt.title(), plt.xlabel(), plt.ylabel() e plt.grid() definem o título, rótulos dos eixos e a grade do gráfico, respectivamente. plt.show() exibe o gráfico. plt.text() adiciona texto informativo ao gráfico.

**Estruturas de Dados:** As listas tempos, posicoes_x e posicoes_y são usadas para armazenar múltiplos valores de dados, o que é essencial para plotar o gráfico.

**Conversão de Tipo:** A função math.radians() converte o ângulo de graus para radianos, demonstrando a conversão entre tipos relacionados.

**Formatação de Saída:** O uso de f-strings (strings formatadas) com especificadores de formatação (:.2f) permite controlar o número de casas decimais na saída. type() é usado para exibir o tipo de uma variável.

Este exemplo é mais complexo e demonstra como os tipos de dados são usados em conjunto com cálculos matemáticos e bibliotecas de visualização para resolver e apresentar um problema de engenharia de forma completa.

**Resultado:**

![PROJETIL](imagens/03_imagem_projetil.png)

---

## 2.2. Operadores Aritméticos e Lógicos em Python

Em Python, operadores são símbolos especiais que realizam operações em valores (chamados de operandos). Eles são essenciais para realizar cálculos, comparações e manipular dados em geral. Nesta seção, vamos explorar os operadores aritméticos e lógicos, que são fundamentais para a programação em engenharia.

### 2.2.1. Operadores Aritméticos

**Código Python:**
```python
# Exemplo de uso de operadores aritméticos
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

Os operadores aritméticos são usados para realizar operações matemáticas básicas.

**Adição (+):** Soma dois valores. 
        Exemplo: forca1 + forca2
 (soma de duas forças)

**Subtração (-):** Subtrai o segundo valor do primeiro. 
        Exemplo: temperatura_final - temperatura_inicial
 (variação de temperatura)

**Multiplicação (*):** Multiplica dois valores. 
        Exemplo: comprimento * largura
(área de uma superfície)

**Divisão (/):** Divide o primeiro valor pelo segundo (sempre retorna um FLOAT). 
        Exemplo: distancia / tempo
 (velocidade média)

**Divisão Inteira (//):** Divide o primeiro valor pelo segundo e retorna a parte inteira do resultado (truncando a parte decimal). 
        Exemplo: total_pecas // pecas_por_caixa
 (número de caixas completas)

**Módulo (%):** Retorna o resto da divisão do primeiro valor pelo segundo. 
        Exemplo: total_segundos % 60
 (obter os segundos restantes após dividir por 60)

**Exponenciação (**):** Eleva o primeiro valor à potência do segundo valor. 
        Exemplo: base ** altura

### 2.2.2. Operadores Lógicos

Os operadores lógicos são usados para combinar ou negar expressões lógicas (valores booleanos True ou False).

**AND (and):** Retorna True se ambas as expressões forem True. 
        Exemplo: temperatura > temperatura_minima and pressao < pressao_maxima
 (verificar se a temperatura está dentro da faixa e a pressão também)

**OR (or):** Retorna True se pelo menos uma das expressões for True. 
        Exemplo: nivel_tanque < nivel_minimo or valvula_emergencia_aberta
 (verificar se o nível do tanque está baixo ou a válvula de emergência está aberta)
 
**NOT (not):** Nega uma expressão (inverte seu valor lógico). 
        Exemplo: not sensor_ativado
 (verificar se o sensor não está ativado)

 ---

 ### 2.2.3. Exemplos Aplicados à Engenharia

**1) Cálculo da Área de um Retângulo:**

```python
comprimento = 10.5  # metros (float)
largura = 5.0     # metros (float)
area = comprimento * largura  # metros quadrados (float)
print("Área do retângulo:", area, "m²")
```

**Resultado:**
```plaintext
Área do retângulo: 52.5 m²
```
**2) Verificação de Condições de Segurança:**

```python
pressao = 250.0  # PSI (float)
temperatura = 120.0 # graus Celsius (float)
pressao_maxima = 240.0 # PSI (float)
temperatura_maxima = 110.0 # graus Celsius (float)

seguro = pressao <= pressao_maxima and temperatura <= temperatura_maxima # bool

print("Condições de operação seguras:", seguro)
```
**Resultado:**
```plaintext
Condições de operação seguras: False
```
**3) Cálculo de Força Resultante:**
```python
massa = 5.0  # kg (float)
aceleracao = 9.8  # m/s² (float)
forca_resultante = massa * aceleracao  # N (float)
print("Força resultante:", forca_resultante, "N")
```
**Resultado:**
```plaintext
Força resultante: 49.0 N
```

Este texto fornece uma base sólida sobre operadores aritméticos e lógicos, juntamente com exemplos práticos de como eles são usados em contextos de engenharia.

---

### 2.2.4. Exercício Proposto: Cálculo de Área e Perímetro de um Terreno e Verificação de Viabilidade

**Descrição:**

Um engenheiro civil precisa desenvolver um programa em Python para auxiliar no cálculo da área e perímetro de um terreno retangular e verificar se ele atende a certos critérios de viabilidade para construção.

**Requisitos:**

1. **Entrada de Dados:**
    - O programa deve solicitar ao usuário que insira o comprimento e a largura do terreno em metros.
    - O programa deve solicitar ao usuário a área mínima permitida para construção no local.

2. **Cálculos:**
    - Calcular a área do terreno (`área = comprimento * largura`).
    - Calcular o perímetro do terreno (`perímetro = 2 * (comprimento + largura)`).

3. **Verificação de Viabilidade:**
    - Verificar se a área do terreno é maior ou igual à área mínima permitida para construção.
    - Verificar se o perímetro do terreno é menor que um valor máximo (por exemplo, 100 metros - este valor pode ser fixo no programa).

4. **Saída de Dados:**
    - Exibir a área e o perímetro do terreno com duas casas decimais.
    - Exibir uma mensagem indicando se o terreno é viável para construção, com base nos critérios de área e perímetro.

**Exemplo de Interação:**

```plaintext
Digite o comprimento do terreno (m): 50
Digite a largura do terreno (m): 30
Digite a área mínima permitida para construção (m²): 1000
Área do terreno: 1500.00 m²
Perímetro do terreno: 160.00 m
Terreno viável para construção: Sim
```

**Dicas:**
- Use os tipos de dados `float` para representar as medidas do terreno e a área mínima.
- Use os operadores aritméticos `*`, `+` e `/` para realizar os cálculos.
- Use os operadores lógicos `>=` e `<` e o operador `and` para realizar as verificações de viabilidade.
- Use a função `input()` para obter os dados do usuário.
- Use a função `print()` para exibir os resultados.
- Use f-strings para formatar a saída com duas casas decimais.

**Código Python de Exemplo:**

```python
# Solicitar entrada do usuário
comprimento = float(input("Digite o comprimento do terreno (m): "))
largura = float(input("Digite a largura do terreno (m): "))
area_minima = float(input("Digite a área mínima permitida para construção (m²): "))

# Calcular área e perímetro
area = comprimento * largura
perimetro = 2 * (comprimento + largura)

# Verificar viabilidade
viavel = area >= area_minima and perimetro < 100

# Exibir resultados
print(f"Área do terreno: {area:.2f} m²")
print(f"Perímetro do terreno: {perimetro:.2f} m")
print(f"Terreno viável para construção: {'Sim' if viavel else 'Não'}")
```

**Resultado:**

```plaintext
Área do terreno: 1500.00 m²
Perímetro do terreno: 160.00 m
Terreno viável para construção: Sim
```

Este exercício combina o uso de tipos de dados, operadores aritméticos e lógicos em um contexto prático de engenharia civil, proporcionando uma aplicação mais completa dos conceitos aprendidos.

---

### 2.2.5. Exercício Proposto: Análise da Deformação de uma Viga

**Descrição:**

Um engenheiro mecânico precisa analisar a deformação de uma viga sob diferentes cargas. O programa em Python deve calcular a deflexão da viga em função da posição ao longo do seu comprimento e gerar um gráfico da deflexão.

**Requisitos:**

1. **Entrada de Dados:**
    - O programa deve solicitar ao usuário que insira o comprimento da viga (L) em metros.
    - O programa deve solicitar ao usuário o módulo de elasticidade do material da viga (E) em Pascal (Pa).
    - O programa deve solicitar ao usuário o momento de inércia da seção transversal da viga (I) em m⁴.
    - O programa deve solicitar ao usuário o tipo de carregamento (1 para carga uniforme, 2 para carga pontual no meio).
    - Se o carregamento for uniforme, solicitar a intensidade da carga (w) em N/m.
    - Se o carregamento for pontual, solicitar a magnitude da carga (P) em N.

2. **Cálculos:**
    - Calcular a deflexão (y) da viga em função da posição (x) ao longo do comprimento, usando as seguintes fórmulas:

    - **Deflexão para Carga Uniforme:**
        ```
        y = (w / (24 * E * I)) * (-x⁴ + 2 * L * x³ - L³ * x)
        ```

    - **Deflexão para Carga Pontual:**
        ```
        Para 0 ≤ x ≤ L/2:
        y = (P * x / (48 * E * I)) * (3 * L² - 4 * x²)

        Para L/2 < x ≤ L:
        y = (P * (L - x) / (48 * E * I)) * (3 * L² - 4 * (L - x)²)
        ```

    Onde:
    - y = Deflexão da viga
    - x = Posição ao longo do comprimento da viga
    - w = Intensidade da carga uniforme
    - P = Magnitude da carga pontual
    - L = Comprimento da viga
    - E = Módulo de elasticidade
    - I = Momento de inércia

3. **Geração do Gráfico:**
    - Usar a biblioteca `matplotlib` para gerar um gráfico da deflexão (y) em função da posição (x).
    - O gráfico deve ter título, rótulos nos eixos e grade.

4. **Saída de Dados:**
    - Exibir os valores de entrada (L, E, I, w ou P).
    - Exibir o valor máximo da deflexão.
    - Salvar o gráfico em um arquivo PNG.

**Exemplo de Interação:**

```plaintext
Digite o comprimento da viga (m): 5
Digite o módulo de elasticidade (Pa): 200000000000
Digite o momento de inércia (m^4): 0.0001
Digite o tipo de carregamento (1-Uniforme, 2-Pontual): 1
Digite a intensidade da carga (N/m): 1000
```

**Código Python de Exemplo:**

```python
import matplotlib.pyplot as plt

# Entrada de dados
L = float(input("Digite o comprimento da viga (m): "))
E = float(input("Digite o módulo de elasticidade (Pa): "))
I = float(input("Digite o momento de inércia (m^4): "))
tipo_carregamento = int(input("Digite o tipo de carregamento (1-Uniforme, 2-Pontual): "))

if tipo_carregamento == 1:
    w = float(input("Digite a intensidade da carga uniforme (N/m): "))
    P = 0
elif tipo_carregamento == 2:
    P = float(input("Digite a magnitude da carga pontual (N): "))
    w = 0
else:
    print("Tipo de carregamento inválido.")
    exit()

# Cálculo da deflexão
num_pontos = 100
x_valores = [i * L / num_pontos for i in range(num_pontos + 1)]
y_valores = []

for x in x_valores:
    if tipo_carregamento == 1:
        y = (w / (24 * E * I)) * (-x**4 + 2 * L * x**3 - L**3 * x)
    elif tipo_carregamento == 2:
        if 0 <= x <= L / 2:
            y = (P * x / (48 * E * I)) * (3 * L**2 - 4 * x**2)
        else:
            y = (P * (L - x) / (48 * E * I)) * (3 * L**2 - 4 * (L - x)**2)
    y_valores.append(y)

# Geração do gráfico
plt.plot(x_valores, y_valores)
plt.title("Deflexão da Viga")
plt.xlabel("Posição (m)")
plt.ylabel("Deflexão (m)")
plt.grid(True)
plt.savefig("deflexao_viga.png")
plt.show()

# Saída de dados
print("\nComprimento da viga:", L, "m")
print("Módulo de elasticidade:", E, "Pa")
print("Momento de inércia:", I, "m^4")
if tipo_carregamento == 1:
    print("Carga uniforme:", w, "N/m")
elif tipo_carregamento == 2:
    print("Carga pontual:", P, "N")
print("Deflexão máxima:", max(y_valores), "m")
print("Gráfico da deflexão salvo como deflexao_viga.png")
```

**Resultado:**

```plaintext
Digite o comprimento da viga (m): 5
Digite o módulo de elasticidade (Pa): 200000000000
Digite o momento de inércia (m^4): 0.0001
Digite o tipo de carregamento (1-Uniforme, 2-Pontual): 1
Digite a intensidade da carga (N/m): 1000
Deflexão máxima: 0.01042 m
Gráfico da deflexão salvo como deflexao_viga.png
```

**Gráfico:**

![Gráfico da Deflexão da Viga](imagens/06_imagem_grafico_deflexao.png)

---

Este exercício é mais completo e envolve:
- Entrada de dados variados (comprimento, propriedades do material, tipo e intensidade de carregamento).
- Cálculos condicionais (usando IF e ELIF) para aplicar a fórmula correta de deflexão.
- Uso de listas para armazenar múltiplos valores de X e Y para plotagem.
- Geração de um gráfico com `matplotlib` para visualizar a deformação da viga.
- Saída formatada dos resultados.

Este tipo de problema é representativo de análises comuns em engenharia mecânica e demonstra a utilidade da programação para resolver problemas complexos e visualizar resultados.

---

### 2.2.6. Curiosidade – Mecânica dos Sólidos

No exemplo do cálculo da deflexão da viga, a teoria física aplicada é a da **Mecânica dos Sólidos**, especificamente a **Teoria da Elasticidade Linear** para vigas. As fórmulas utilizadas derivam das equações da linha elástica, que descrevem o comportamento de vigas sob flexão.

**Fórmulas e Teoria Detalhada:**

1.	**Deflexão para Carga Uniforme:**

**Fórmula:**
```
y = (w / (24 * E * I)) * (-x⁴ + 2 * L * x³ - L³ * x)
```
**Teoria:**
- Esta fórmula é derivada da equação diferencial da linha elástica para uma viga submetida a uma carga uniformemente distribuída.
- A equação da linha elástica relaciona a curvatura da viga com o momento fletor interno.
- As suposições incluem que o material da viga é linearmente elástico, homogêneo e isotrópico, e que as deflexões são pequenas em comparação com o comprimento da viga.

2.	**Deflexão para Carga Pontual:**

**Fórmula:**
```
    Para 0 <= x <= L/2:
    y = (P * x / (48 * E * I)) * (3 * L² - 4 * x²)

    Para L/2 < x <= L:
    y = (P * (L - x) / (48 * E * I)) * (3 * L² - 4 * (L - x)²)
```

**Teoria:**
- Estas fórmulas são derivadas da equação da linha elástica para uma viga com uma carga concentrada aplicada no meio do vão.
- Existem duas equações porque o comportamento da viga é diferente à esquerda e à direita da carga pontual.
- As mesmas suposições da teoria da carga uniforme se aplicam aqui.

Onde:
- y = Deflexão da viga (deslocamento vertical)
- x = Posição ao longo do comprimento da viga
- L = Comprimento total da viga
- E = Módulo de elasticidade do material (resistência do material à deformação elástica)
- I = Momento de inércia da seção transversal da viga (resistência da seção da viga à flexão)
- w = Intensidade da carga uniforme (força por unidade de comprimento)
- P = Magnitude da carga pontual (força concentrada)

**Importância na Engenharia:**

Essas fórmulas e a teoria da flexão de vigas são fundamentais na engenharia estrutural e mecânica. Engenheiros usam esses princípios para:
- Dimensionar vigas: Determinar as dimensões e o material de uma viga para suportar cargas com segurança e dentro de limites aceitáveis de deflexão.
- Analisar estruturas: Calcular as tensões e deformações em estruturas que contêm vigas.
- Projetar máquinas: Garantir que os componentes de máquinas que atuam como vigas (eixos, suportes etc.) funcionem corretamente.

Compreender a teoria por trás das fórmulas é crucial para aplicar corretamente os resultados dos cálculos e garantir a segurança e a eficiência dos projetos de engenharia.

---

## 2.3. Entrada e Saída de Dados em Python

Em programação, a entrada e saída de dados referem-se à forma como um programa recebe informações (entrada) e como ele apresenta os resultados (saída). Em Python, as funções input() e print() são as mais comuns para realizar essas operações.

### 2.3.1. Entrada de Dados: input()

A função `input()` permite que o programa receba dados do usuário através do teclado.

- **Sintaxe:** `variavel = input("Mensagem para o usuário")`
- **Funcionamento:**
    1. A função `input()` exibe a mensagem para o usuário (prompt) na tela.
    2. O usuário digita a informação e pressiona Enter.
    3. A função `input()` retorna a informação digitada como uma string.
    4. A informação retornada é atribuída à variável.

- **Importante:** Mesmo que o usuário digite números, a função `input()` sempre retorna uma STRING. Se você precisar usar a entrada como número, será necessário convertê-la explicitamente usando as funções `int()` (para inteiros) ou `float()` (para números de ponto flutuante).

- **Exemplos em engenharia:**

Solicitar ao usuário o diâmetro de um tubo:

```python
diametro_tubo = float(input("Digite o diâmetro do tubo (em metros): "))
print("Diâmetro do tubo:", diametro_tubo, "m")
```

Pedir a vazão de um fluido:

```python
vazao_fluido = float(input("Digite a vazão do fluido (em m³/s): "))
print("Vazão do fluido:", vazao_fluido, "m³/s")
```

Obter o nome de um material:

```python
nome_material = input("Digite o nome do material: ")
print("Nome do material:", nome_material)
```
### 2.3.2. Saída de Dados: print()

A função `print()` exibe informações na tela do computador.

- **Sintaxe:** `print(argumento1, argumento2, ..., argumentoN)`
- **Funcionamento:**
    1. A função `print()` exibe os valores dos argumentos na tela.
    2. Os argumentos podem ser variáveis, valores literais (números, strings etc.) ou expressões.
    3. Múltiplos argumentos são separados por vírgula, e a função `print()` os exibe separados por espaço.
    4. Por padrão, a função `print()` adiciona uma quebra de linha ao final da saída, ou seja, o próximo `print()` exibirá na linha seguinte.
- **Formatação de saída:** Python oferece várias maneiras de formatar a saída para torná-la mais clara e organizada. As f-strings (strings formatadas) são uma forma conveniente de formatar strings incluindo variáveis.
- **Exemplos em engenharia:**

Exibir o resultado de um cálculo:

```python
resultado = 2 + 2
print("O resultado da soma é:", resultado)
```

Mostrar uma mensagem de alerta:

```python
print("Atenção: Verifique os dados de entrada!")
```

Exibir informações formatadas:

```python
nome_material = "Aço"
diametro_tubo = 0.1
print(f"Dados do tubo:")
print(f"Nome do material: {nome_material}")
print(f"Diâmetro: {diametro_tubo} m")
```

Apresentar os dados de um experimento:

```python
temperatura = 25.5
pressao = 101.3
print(f"Dados do experimento:")
print(f"Temperatura: {temperatura} °C")
print(f"Pressão: {pressao} kPa")
```

A habilidade de obter dados do usuário e apresentar resultados de forma clara é fundamental para criar programas interativos e úteis em engenharia.

---

### 2.3.4. Exercício Proposto: Cálculo de Conversão em um Reator

**Descrição:**

Um engenheiro químico precisa de um programa para calcular a conversão de um reagente em um reator.  
O programa deve solicitar ao usuário a quantidade inicial do reagente, a quantidade final após a reação e exibir a conversão calculada. Além disso, deve pedir informações sobre o tipo de reator e o tempo de reação.

**Requisitos:**

1. **Entrada de Dados:**
    - O programa deve solicitar ao usuário o nome do reagente (`str`).
    - O programa deve solicitar ao usuário a quantidade inicial do reagente em mols (`float`).
    - O programa deve solicitar ao usuário a quantidade final do reagente em mols (`float`).
    - O programa deve solicitar ao usuário o tipo do reator (`str`).
    - O programa deve solicitar ao usuário o tempo de reação em minutos (`float`).

2. **Cálculo:**

Calcular a conversão do reagente usando a fórmula:

```python
conversao = (quantidade_inicial - quantidade_final) / quantidade_inicial * 100
```

3. **Saída de Dados:**
    - Exibir o nome do reagente.
    - Exibir a quantidade inicial e final do reagente, formatadas com 2 casas decimais.
    - Exibir a conversão calculada, formatada como porcentagem com 2 casas decimais (ex: 80.00%).
    - Exibir o tipo do reator e o tempo de reação.

**Exemplo de Interação:**

```plaintext
Digite o nome do reagente: Amoníaco
Digite a quantidade inicial do reagente (em mols): 10.0
Digite a quantidade final do reagente (em mols): 2.0
Digite o tipo do reator: Reator de Batelada
Digite o tempo de reação (em minutos): 30.0
Reagente: Amoníaco
Quantidade inicial: 10.00 mols
Quantidade final: 2.00 mols
Conversão: 80.00%
Tipo do reator: Reator de Batelada
Tempo de reação: 30.00 minutos
```

**Código Python de Exemplo:**

```python
# Solicitar entrada do usuário
nome_reagente = input("Digite o nome do reagente: ")
quantidade_inicial = float(input("Digite a quantidade inicial do reagente (em mols): "))
quantidade_final = float(input("Digite a quantidade final do reagente (em mols): "))
tipo_reator = input("Digite o tipo do reator: ")
tempo_reacao = float(input("Digite o tempo de reação (em minutos): "))

# Cálculo da conversão
conversao = (quantidade_inicial - quantidade_final) / quantidade_inicial * 100

# Exibir resultados
print(f"\nReagente: {nome_reagente}")
print(f"Quantidade inicial: {quantidade_inicial:.2f} mols")
print(f"Quantidade final: {quantidade_final:.2f} mols")
print(f"Conversão: {conversao:.2f}%")
print(f"Tipo do reator: {tipo_reator}")
print(f"Tempo de reação: {tempo_reacao:.2f} minutos")
```

**Dicas:**
- Use a função `input()` para obter os dados do usuário.
- Use os tipos de dados `float` e `str` para armazenar os valores.
- Lembre-se de converter as entradas numéricas de `input()` para `float`.
- Use f-strings para formatar a saída, especialmente a conversão (:.2f%).

---

#### Figura 2.3.1 – Esquema Técnico

```plain
+---------------------+
|   Programa Python   |
+---------------------+
         ||
+---------------------+
|   Entrada de Dados  |
+---------------------+
         ||
+---------------------+
|       input()       |
+---------------------+
         ||
+-----------------------------+
|  Dados do Usuário (Teclado) |
+-----------------------------+
         ||
+-------------------------------+
| Processamento (Cálculos, Lógica) |
+-------------------------------+
         ||
+---------------------+
|   Saída de Dados    |
+---------------------+
         ||
+---------------------+
|      print()        |
+---------------------+
         ||
+---------------------+
|    Resultados       |
|      (Tela)         |
+---------------------+
         ||
```

**Descrição do Esquema:**
1.	**Programa Python:** Representa o código Python que o engenheiro escreve para resolver um problema específico (e.g., cálculo de tensões, simulação de um circuito).
2.	**input() function:** Indica o ponto onde o programa interage com o usuário para receber dados. A função input() aguarda que o usuário digite informações através do teclado.
3.	**Dados do Usuário (Teclado):** Mostra a entrada de dados feita pelo usuário, que podem ser valores numéricos, texto etc.
4.	**Processamento (Cálculos, Lógica):** Representa a parte do programa onde os dados de entrada são manipulados, cálculos são realizados, decisões lógicas são tomadas etc.
5.	**print() function:** Indica o ponto onde o programa exibe os resultados ou informações para o usuário. A função print() envia a saída para a tela.
6.	**Resultados (Tela):** Mostra a saída do programa, que pode incluir números, texto, mensagens, gráficos (em módulos mais avançados) etc.

**Detalhes Técnicos:**
- O esquema é genérico e se aplica a muitos programas que interagem com o usuário.
- As setas indicam a direção do fluxo de dados.
- Os retângulos representam componentes ou processos do programa.
- Não há cores para manter o estilo técnico.

Este esquema ajuda a visualizar o fluxo de informações em um programa Python, desde a obtenção dos dados até a apresentação dos resultados.

**Código Python:**

```python
# Entrada de dados
nome_reagente = input("Digite o nome do reagente: ")
quantidade_inicial = float(input("Digite a quantidade inicial de " + nome_reagente + " (mols): "))
quantidade_final = float(input("Digite a quantidade final de " + nome_reagente + " (mols): "))
tipo_reator = input("Digite o tipo do reator: ")
tempo_reacao = float(input("Digite o tempo de reação (minutos): "))

# Cálculo da conversão
conversao = (quantidade_inicial - quantidade_final) / quantidade_inicial

# Saída de dados
print("\nReagente:", nome_reagente)
print(f"Quantidade Inicial: {quantidade_inicial:.2f} mols")
print(f"Quantidade Final: {quantidade_final:.2f} mols")
print(f"Conversão: {conversao * 100:.2f} %")
print("Tipo do Reator:", tipo_reator)
print("Tempo de Reação:", tempo_reacao, "minutos")
```

**Resultado:**
```plaintext
Reagente: Amoníaco
Quantidade Inicial: 10.00 mols
Quantidade Final: 2.00 mols
Conversão: 80.00 %
Tipo do Reator: Reator de Batelada
Tempo de Reação: 30.00 minutos
```
Este exercício aborda um problema prático de engenharia química e reforça o uso de entrada e saída de dados com formatação.

---

## 2.4. Primeiros Cálculos Aplicados à Engenharia

Nesta seção, vamos explorar como aplicar os fundamentos da programação Python para realizar cálculos simples em problemas de engenharia. Os exemplos a seguir ilustram como usar os tipos de dados, operadores aritméticos e entrada/saída para resolver tarefas comuns em diferentes disciplinas da engenharia.


### 2.4.1. Engenharia Civil: Cálculo da Área de uma Viga

**Problema:** Calcular a área da seção transversal de uma viga retangular.
**Fórmula:** Área = base * altura
**Código Python:**
```python
# Entrada de dados
base = float(input("Digite a base da viga (m): "))
altura = float(input("Digite a altura da viga (m): "))

# Cálculo da área
area = base * altura

# Saída de dados
print(f"A área da seção transversal da viga é: {area:.2f} m²")
```

### 2.4.2. Engenharia Elétrica: Lei de Ohm

**Problema:** Calcular a corrente elétrica em um resistor dado a tensão e a resistência.
**Fórmula:** Corrente = Tensão / Resistência
**Código Python:**
```python
# Entrada de dados
tensao = float(input("Digite a tensão (V): "))
resistencia = float(input("Digite a resistência (Ω): "))

# Cálculo da corrente
corrente = tensao / resistencia

# Saída de dados
print(f"A corrente elétrica é: {corrente:.2f} A")
```

### 2.4.3. Engenharia Mecânica: Energia Potencial Gravitacional

**Problema:** Calcular a energia potencial gravitacional de um objeto.
**Fórmula:** Energia Potencial = massa * gravidade * altura
**Código Python:**
```python
# Entrada de dados
massa = float(input("Digite a massa do objeto (kg): "))
gravidade = 9.81  # Aceleração da gravidade (m/s²)
altura = float(input("Digite a altura (m): "))

# Cálculo da energia potencial
energia_potencial = massa * gravidade * altura

# Saída de dados
print(f"A energia potencial gravitacional é: {energia_potencial:.2f} J")
```

### 2.4.4. Engenharia Química: Vazão Molar

**Problema:** Converter vazão mássica para vazão molar.
**Fórmula:** Vazão Molar = Vazão Mássica / Massa Molar
**Código Python:**

```python
# Entrada de dados
vazao_massica = float(input("Digite a vazão mássica (kg/s): "))
massa_molar = float(input("Digite a massa molar (kg/mol): "))

# Cálculo da vazão molar
vazao_molar = vazao_massica / massa_molar

# Saída de dados
print(f"A vazão molar é: {vazao_molar:.2f} mol/s")
```

### 2.4.5. Engenharia Ambiental: Cálculo de Concentração

**Problema:** Calcular a concentração de um poluente em uma solução.
**Fórmula:** Concentração = Massa do Poluente / Volume da Solução
**Código Python:**

```python
# Entrada de dados
massa_poluente = float(input("Digite a massa do poluente (kg): "))
volume_solucao = float(input("Digite o volume da solução (m³): "))

# Cálculo da concentração
concentracao = massa_poluente / volume_solucao

# Saída de dados
print(f"A concentração do poluente é: {concentracao:.2f} kg/m³")
```
---

### 2.5. Conclusão

Estes exemplos demonstram como os conceitos básicos de Python podem ser aplicados para resolver problemas simples em diferentes áreas da engenharia.
Eles reforçam a importância de:
- Entender os tipos de dados apropriados para representar grandezas físicas.
- Utilizar os operadores aritméticos corretamente para realizar os cálculos.
- Interagir com o usuário para obter os dados necessários e apresentar os resultados de forma clara.
Nos próximos módulos, exploraremos conceitos mais avançados de Python para resolver problemas de engenharia mais complexos.

---

## 3. Estrutura de Controle

Neste módulo sobre estrutura de controle, exploramos os tipos de dados, operadores e entrada/saída, que nos permitem realizar cálculos e interagir com o usuário. No entanto, a capacidade de um programa de tomar decisões e repetir ações é fundamental para resolver problemas mais complexos. É aqui que entram as estruturas de controle.
Este módulo é dedicado ao estudo das estruturas de controle em Python, que são ferramentas essenciais para direcionar o fluxo de execução de um programa. Vamos nos aprofundar em como controlar quais partes do código são executadas e quantas vezes, com base em condições específicas.
Primeiramente, abordaremos as condicionais (IF, ELIF, ELSE). As condicionais permitem que o programa escolha diferentes caminhos de execução, dependendo se uma determinada condição é verdadeira ou falsa. Isso é crucial para implementar a lógica de decisão em problemas de engenharia, como verificar se um sensor excedeu um limite de segurança ou classificar dados de acordo com critérios específicos.
Em seguida, exploraremos os laços de repetição (FOR, WHILE). Os laços de repetição nos permitem executar um bloco de código repetidamente, até que uma condição seja satisfeita. Isso é extremamente útil para automatizar tarefas repetitivas, como iterar sobre conjuntos de dados, realizar cálculos iterativos ou simular o comportamento de sistemas ao longo do tempo.
Finalmente, demonstraremos aplicações práticas em verificação de condições operacionais. Através de exemplos relevantes para a engenharia, mostraremos como as estruturas de controle podem ser usadas para monitorar processos, garantir a segurança de sistemas e automatizar a tomada de decisões em tempo real.
Ao concluir este módulo, você estará apto a desenvolver programas Python que não apenas realizam cálculos, mas também tomam decisões lógicas e executam ações repetitivas, abrindo caminho para a criação de soluções de engenharia mais robustas e inteligentes.

---

## 3.1. Condicionais: if, elif, else

As estruturas condicionais são fundamentais para controlar o fluxo de execução de um programa, permitindo que diferentes blocos de código sejam executados dependendo se uma condição é verdadeira ou falsa. Em Python, as palavras-chave if, elif (abreviação de "else if") e else são usadas para definir essas estruturas.

### 3.1.1. A estrutura if

A estrutura if é a mais básica e executa um bloco de código somente se uma condição especificada for verdadeira.

**Sintaxe:**
```python
if condição:
    # bloco de código a ser executado se a condição for verdadeira
    pass
```
**Funcionamento:**
- A condição é uma expressão que pode ser avaliada como True (verdadeiro) ou False (falso).
- Se a condição for True, o bloco de código indentado abaixo do if é executado.
- Se a condição for False, o bloco de código é ignorado e o programa continua a execução na próxima linha após o bloco if.

- **Exemplo em engenharia:** Verificar se a temperatura de um sistema excedeu um limite de segurança.

**Código Python:**
```python
indice_poluicao = float(input("Digite o índice de poluição do ar: "))

if indice_poluicao <= 50:
    print("Qualidade do ar: Boa")
elif indice_poluicao <= 100:
    print("Qualidade do ar: Moderada")
elif indice_poluicao <= 150:
    print("Qualidade do ar: Insatisfatória")
elif indice_poluicao <= 200:
    print("Qualidade do ar: Ruim")
else:
    print("Qualidade do ar: Muito Ruim")
```
**Resultado:**

```plaintext
Digite o índice de poluição do ar: 75
Qualidade do ar: Moderada
```

---


### 3.1.2. A estrutura if-else

A estrutura if-else permite executar um bloco de código se a condição for verdadeira e outro bloco de código se a condição for falsa.
**Sintaxe:**

```python
if condição:
    # bloco de código a ser executado se a condição for verdadeira
    pass
else:
    # bloco de código a ser executado se a condição for falsa
    pass
```

**Funcionamento:**
- A condição é avaliada.
- Se a condição for True, o bloco de código do if é executado.
- Se a condição for False, o bloco de código do else é executado.
- Apenas um dos blocos de código (o do if ou o do else) é executado.

- **Exemplo em engenharia:** Classificar um material como "resistente" ou "não resistente" com base em um teste de tensão.

**Código Python:**

```python
tensao = float(input("Digite a tensão aplicada (N/m²): "))
limite = 100.0

if tensao > limite:
    print("Material não resistente.")
else:
    print("Material resistente.")
```

**Resultado:**

```plaintext
Digite a tensão aplicada (N/m²): 75
Material resistente.
```
---

### 3.1.3. A estrutura if-elif-else

A estrutura if-elif-else permite verificar múltiplas condições em sequência. O elif (else if) especifica uma nova condição a ser verificada se a condição anterior for falsa.

**Sintaxe:**

```python
if condição1:
    # bloco de código a ser executado se condição1 for verdadeira
    pass
elif condição2:
    # bloco de código a ser executado se condição2 for verdadeira
    pass
else:
    # bloco de código a ser executado se nenhuma das condições anteriores for verdadeira
    pass
```

**Funcionamento:**
- As condições são avaliadas em ordem.
- Se uma condição for True, o bloco de código correspondente é executado e o restante da estrutura (elif e else) é ignorado.
- Se nenhuma condição for True, o bloco de código do else (se houver) é executado.
- Pode haver qualquer número de blocos elif. O bloco else é opcional.

**Exemplo em engenharia:** Classificar a qualidade do ar com base no índice de poluição.

**Código Python:**
```python
indice_poluicao = float(input("Digite o índice de poluição do ar: "))

if indice_poluicao <= 50:
    print("Qualidade do ar: Boa")
elif indice_poluicao <= 100:
    print("Qualidade do ar: Moderada")
elif indice_poluicao <= 150:
    print("Qualidade do ar: Insatisfatória")
elif indice_poluicao <= 200:
    print("Qualidade do ar: Ruim")
else:
    print("Qualidade do ar: Muito Ruim")
```
**Resultado:**

```plaintext
Digite o índice de poluição do ar: 75
Qualidade do ar: Moderada
```

**Pontos-chave:**
- **Indentação:** A indentação é crucial em Python para definir os blocos de código dentro das estruturas condicionais. O código dentro de um bloco if, elif ou else deve ser indentado.
- **Operadores Lógicos:** As condições nas estruturas condicionais geralmente envolvem operadores lógicos (and, or, not) e operadores de comparação (==, !=, >, <, >=, <=).
- **Flexibilidade:** As estruturas condicionais podem ser aninhadas (uma dentro da outra) para criar lógicas de decisão mais complexas.
Compreender e aplicar corretamente as estruturas condicionais é essencial para desenvolver programas que resolvam problemas reais de engenharia, onde a tomada de decisões é uma parte fundamental do processo.

### 3.1.4. Exercício Proposto: Classificação de Solos

**Descrição:**
Um engenheiro civil precisa de um programa para classificar amostras de solo com base em seu Índice de Plasticidade (IP) e Limite de Liquidez (LL). O programa deve solicitar ao usuário os valores de IP e LL e exibir a classificação do solo de acordo com a tabela a seguir:

![CLASSIFICAÇÃO](imagens/07_imagem_exercicio.png)

**Requisitos:**

1. **Entrada de Dados:**
   - O programa deve solicitar ao usuário o Limite de Liquidez (LL) do solo (FLOAT).
   - O programa deve solicitar ao usuário o Índice de Plasticidade (IP) do solo (FLOAT).
2. **Classificação:**
   - Utilizar estruturas condicionais (IF, ELIF, ELSE) para classificar o solo de acordo com a tabela fornecida.
3. **Saída de Dados:**
   - Exibir o Limite de Liquidez (LL) e o Índice de Plasticidade (IP) inseridos pelo usuário, formatados com duas casas decimais.
   - Exibir a classificação do solo.

**Exemplo de Interação:**
```plaintext
Digite o Limite de Liquidez (LL) do solo: 45
Digite o Índice de Plasticidade (IP) do solo: 25
Limite de Liquidez (LL): 45.00
Índice de Plasticidade (IP): 25.00
Classificação do Solo: Solo Argiloso
```

**Dicas:**

- Use a função input() para obter os valores de LL e IP do usuário.
- Use os tipos de dados FLOAT para armazenar os valores de LL e IP.
- Lembre-se de converter as entradas de input() para FLOAT.
- Use os operadores de comparação (>=, <, ==) e os operadores lógicos (AND, OR, NOT) para implementar as condições de classificação.
- Use f-strings para formatar a saída com duas casas decimais.

**Código Python:**
```python
# Entrada de dados
ll = float(input("Digite o Limite de Liquidez (LL): "))
ip = float(input("Digite o Índice de Plasticidade (IP): "))

# Classificação do solo
if ll >= 50 and ip >= 7:
    classificacao = "Argila"
elif ll < 50 and 4 <= ip < 7:
    classificacao = "Silte"
else:
    classificacao = "Solo Não Plástico"

# Saída de dados
print(f"\nLimite de Liquidez (LL): {ll:.2f}")
print(f"Índice de Plasticidade (IP): {ip:.2f}")
print(f"Classificação do Solo: {classificacao}")
```
**Resultado:**
```plaintext
Limite de Liquidez (LL): 45.00
Índice de Plasticidade (IP): 25.00
Classificação do Solo: Solo Argiloso
```
Este exercício aplica as estruturas condicionais em um problema prático de engenharia civil, demonstrando como a lógica de decisão pode ser implementada em programas para classificar dados e auxiliar na análise de materiais.

### 3.1.5. Curiosidade – Engenharia Civil

Na engenharia civil, a classificação de solos é uma etapa crucial no projeto e construção de fundações, estradas e outras estruturas. A tabela de classificação de solos baseada no Índice de Plasticidade (IP) e Limite de Liquidez (LL) é amplamente utilizada para entender as propriedades mecânicas do solo.
A classificação de solos é baseada em normas técnicas, como a ASTM D2487, que define os critérios para categorizar solos em diferentes grupos, como argilas, siltes e solos não plásticos. Esses grupos são importantes porque influenciam diretamente o comportamento do solo sob carga, sua capacidade de suporte e sua suscetibilidade à deformação.
A tabela de classificação apresentada no exercício é uma simplificação, mas reflete os princípios básicos usados na prática. A classificação correta do solo é essencial para garantir a segurança e a estabilidade das estruturas construídas sobre ele.

### 3.1.6. Conclusão

Dominar as estruturas condicionais **IF, ELIF e ELSE** é um marco importante na jornada de programação. Elas fornecem a base para criar programas que não apenas executam cálculos, mas também respondem dinamicamente a diferentes entradas e condições. Nos próximos itens e módulos, veremos como essa habilidade será aplicada em contextos mais complexos, como laços de repetição, funções e projetos de engenharia.

---

## 3.2. Laços de Repetição: for, while

Os laços de repetição são fundamentais na programação, permitindo que um bloco de código seja executado várias vezes, com base em uma condição. Em Python, os principais tipos de laços são o `for` e o `while`.

O laço `for` é usado para iterar sobre uma sequência (como uma lista, tupla ou string) e executar um bloco de código para cada item da sequência. A sintaxe básica é:

```python
for item in sequencia:
    # bloco de código
```

O laço `while`, por outro lado, executa um bloco de código enquanto uma condição específica for verdadeira. A sintaxe básica é:

```python
while condicao:
    # bloco de código
```
Ambos os tipos de laços são amplamente utilizados em problemas de engenharia, como simulações, otimizações e análises de dados.

### 3.2.1. O laço for

Os laços de repetição são estruturas de controle que permitem executar um bloco de código repetidamente, um número específico de vezes ou enquanto uma condição for verdadeira. Em Python, os dois tipos principais de laços são FOR e WHILE.
O laço `for` é usado para iterar sobre uma sequência (como uma lista, tupla ou string) e executar um bloco de código para cada item da sequência. A sintaxe básica é:

```python
for item in sequencia:
    # bloco de código
```
**Funcionamento:**
- A variável `item` assume o valor de cada elemento da `sequencia` a cada iteração.
- O bloco de código indentado abaixo do `for` é executado para cada item.
- O laço termina quando todos os itens da sequência foram processados.
**Exemplo em engenharia:** Calcular a média de uma série de medidas de temperatura.

```python
temperaturas = [20.5, 22.0, 19.8, 21.5, 23.0]
soma_temperaturas = 0.0
for temperatura in temperaturas:
    soma_temperaturas += temperatura
media_temperatura = soma_temperaturas / len(temperaturas)
print(f"Média de temperatura: {media_temperatura:.2f} °C")
```
**Resultado:**
```plaintext
Média de temperatura: 21.16 °C
```
---

### 3.2.2. O laço while

O laço `while` executa um bloco de código enquanto uma condição específica for verdadeira. É útil quando o número de iterações não é conhecido previamente.

**Sintaxe:**
```python
while condicao:
    # bloco de código
```

**Funcionamento:**
- A condição é avaliada antes de cada iteração.
- Se a condição for True, o bloco de código indentado é executado.
- Após a execução do bloco, a condição é verificada novamente.
- O laço continua até que a condição se torne False.

**Exemplos em engenharia:**
Iterar sobre uma lista de medições de temperatura:
![ITERAÇÃO_WHILE](imagens/08_imagem_exercicio.png) 

Calcular a soma dos quadrados dos 10 primeiros números inteiros:

```python
soma_quadrados = 0
contador = 1
while contador <= 10:
    soma_quadrados += contador**2
    contador += 1
print(f"Soma dos quadrados: {soma_quadrados}")
```
**Funcionamento:**
- A condição é avaliada antes de cada iteração.
- Se a condição for True, o bloco de código indentado é executado.
- Após a execução do bloco, a condição é verificada novamente.
- O laço continua até que a condição se torne False.

**Exemplo em engenharia:** Simular o resfriamento de um líquido até atingir uma temperatura segura.

```python
temperatura = 100.0  # Temperatura inicial em °C
while temperatura > 30.0:  # Condição de resfriamento
    print(f"Temperatura atual: {temperatura:.2f} °C")
    temperatura -= 5.0  # Resfriamento de 5 °C por iteração
print("Temperatura segura alcançada.")
```
**Resultado:**
```plaintext
Temperatura atual: 100.00 °C
Temperatura atual: 95.00 °C
Temperatura atual: 90.00 °C
Temperatura atual: 85.00 °C
Temperatura atual: 80.00 °C
Temperatura atual: 75.00 °C
Temperatura atual: 70.00 °C
Temperatura atual: 65.00 °C
Temperatura atual: 60.00 °C
Temperatura atual: 55.00 °C
Temperatura atual: 50.00 °C
Temperatura atual: 45.00 °C
Temperatura atual: 40.00 °C
Temperatura atual: 35.00 °C
Temperatura segura alcançada.
```

**Pontos-chave:**
- **Controle de Iteração:** O laço `for` é ideal quando se sabe o número de iterações ou quando se está iterando sobre uma sequência. O laço `while` é mais flexível, permitindo que o número de iterações dependa de uma condição dinâmica.
- **Condição de Parada:** É crucial definir uma condição de parada para os laços `while` para evitar laços infinitos (onde o laço nunca termina).
- **Variáveis de Controle:** As variáveis usadas nas condições dos laços (como `contador`, `temperatura`, etc.) devem ser atualizadas dentro do laço para garantir que a condição de parada seja eventualmente alcançada.
- **range():** A função `range()` é frequentemente usada com o laço `for` para gerar sequências de números. Por exemplo, `for i in range(10):` itera de 0 a 9.

Os laços de repetição são ferramentas poderosas para automatizar tarefas, processar grandes conjuntos de dados e implementar algoritmos iterativos em diversas aplicações de engenharia. Eles permitem que os engenheiros desenvolvam soluções eficientes e escaláveis para problemas complexos, economizando tempo e esforço no desenvolvimento de software.

---

### 3.2.3. Exercício Proposto: Simulação de um Reator Batelada Isotérmico

**Descrição:**
Um engenheiro químico precisa simular a conversão de um reagente A em um produto B em um reator batelada isotérmico. A reação segue uma cinética de primeira ordem:

```plaintext
Reação: A → B
```

A taxa de reação é dada por:
```math
- rA = -k * CA
```

Onde:
- -rA é a taxa de desaparecimento do reagente A (mol/L·min)
- k é a constante de velocidade da reação (min⁻¹)
- CA é a concentração do reagente A (mol/L)

O programa deve calcular a concentração de A e a conversão de A ao longo do tempo.

**Requisitos:**

1. **Entrada de Dados:**
- O programa deve solicitar ao usuário a concentração inicial de A (CA0) em mol/L (FLOAT).
- O programa deve solicitar ao usuário a constante de velocidade da reação (k) em min⁻¹ (FLOAT).
- O programa deve solicitar ao usuário o tempo total de simulação (tempo_final) em minutos (FLOAT).
- O programa deve solicitar ao usuário o número de pontos no tempo para calcular a concentração (num_pontos) (INT).

2. **Cálculos:**
- Usar um laço for para iterar sobre o tempo, dividindo o tempo total em intervalos iguais.
- Dentro do laço, calcular a concentração de A (CA) em cada ponto no tempo usando a equação integrada para uma reação de primeira ordem em um reator batelada:

```math
CA(t) = CA0 * exp(-k * t)
```

```python
import math

# Entrada de Dados
CA0 = float(input("Concentração inicial de A (CA0) em mol/L: "))
k = float(input("Constante de velocidade da reação (k) em min⁻¹: "))
tempo_final = float(input("Tempo total de simulação (tempo_final) em minutos: "))
num_pontos = int(input("Número de pontos no tempo para calcular a concentração (num_pontos): "))

# Cálculos
tempos = []
concentracoes_A = []
for i in range(num_pontos + 1):
    t = i * (tempo_final / num_pontos)  # Tempo atual
    CA = CA0 * math.exp(-k * t)  # Cálculo da concentração de A
    tempos.append(t)
    concentracoes_A.append(CA)

# Exibição dos resultados
for i in range(len(tempos)):
    print(f"Tempo: {tempos[i]:.1f} min, [A]: {concentracoes_A[i]:.2f} mol/L, [B]: {1 - concentracoes_A[i]:.2f} mol/L")
```

**Saída de Dados:**
```plaintext
Concentração inicial de A (CA0) em mol/L: 1.0
Constante de velocidade da reação (k) em min⁻¹: 0.1
Tempo total de simulação (tempo_final) em minutos: 10
Número de pontos no tempo para calcular a concentração (num_pontos): 10
Tempo: 0.0 min, [A]: 1.00 mol/L, [B]: 0.00 mol/L
Tempo: 1.0 min, [A]: 0.90 mol/L, [B]: 0.10 mol/L
Tempo: 2.0 min, [A]: 0.82 mol/L, [B]: 0.18 mol/L
Tempo: 3.0 min, [A]: 0.74 mol/L, [B]: 0.26 mol/L
Tempo: 4.0 min, [A]: 0.67 mol/L, [B]: 0.33 mol/L
Tempo: 5.0 min, [A]: 0.61 mol/L, [B]: 0.39 mol/L
Tempo: 6.0 min, [A]: 0.55 mol/L, [B]: 0.45 mol/L
Tempo: 7.0 min, [A]: 0.50 mol/L, [B]: 0.50 mol/L
Tempo: 8.0 min, [A]: 0.45 mol/L, [B]: 0.55 mol/L
Tempo: 9.0 min, [A]: 0.41 mol/L, [B]: 0.59 mol/L
Tempo: 10.0 min, [A]: 0.37 mol/L, [B]: 0.63 mol/L
```
Este exercício simula um processo fundamental em engenharia química (reação em reator) e demonstra o uso de laços for para realizar cálculos iterativos ao longo do tempo.

**Dicas:**
- Use a função `input()` para obter os valores de CA0, k, tempo_final e num_pontos do usuário.
- Use os tipos de dados FLOAT para CA0, k e tempo_final, e INT para num_pontos.
- Use a função `math.exp()` para calcular a exponencial na equação da concentração de A.
- Use um laço `for` para iterar sobre o número de pontos no tempo e calcular a concentração de A em cada ponto.
- Use f-strings para formatar a saída com duas casas decimais.

---

### 3.2.4. Curiosidade – Engenharia Química

Na engenharia química, a simulação de reatores é uma prática comum para entender o comportamento de reações químicas em diferentes condições. O exemplo apresentado no exercício propõe uma simulação de um reator batelada isotérmico, onde a concentração de um reagente A diminui ao longo do tempo devido à reação com uma constante de velocidade k.
A cinética de primeira ordem é uma das mais simples e comuns em reações químicas, onde a taxa de reação é proporcional à concentração do reagente. A equação integrada para a concentração de A ao longo do tempo é fundamental para prever como a reação evolui, permitindo aos engenheiros otimizar as condições de operação do reator.
A simulação de reatores é essencial para o design e operação de processos químicos, ajudando a prever a conversão de reagentes, a formação de produtos e a eficiência do processo. Compreender como implementar laços de repetição em Python para simular essas dinâmicas é uma habilidade valiosa para engenheiros químicos.

### 3.2.5. Conclusão

Os laços de repetição `for` e `while` são ferramentas poderosas na programação, permitindo a execução de blocos de código múltiplas vezes com base em condições específicas. Eles são amplamente utilizados em problemas de engenharia para automatizar tarefas, processar dados e simular comportamentos dinâmicos.
Compreender como usar esses laços é essencial para desenvolver programas eficientes e eficazes. Nos próximos módulos, veremos como combinar laços de repetição com outras estruturas de controle, como condicionais e funções, para criar soluções mais complexas e robustas em Python.

---

## 3.3. Aplicações Práticas em Verificação de Condições Operacionais

As estruturas de controle (IF, ELIF, ELSE, FOR, WHILE) são extremamente úteis para monitorar e controlar condições operacionais em sistemas de engenharia. Nesta seção, apresentaremos exemplos práticos de como essas estruturas podem ser aplicadas para garantir a segurança, eficiência e correto funcionamento de processos e equipamentos.

### 3.3.1. Monitoramento de Temperatura em um Reator Químico

Em um reator químico, a temperatura é um parâmetro crítico que deve ser mantido dentro de limites seguros para evitar reações indesejadas ou danos ao equipamento. O código abaixo demonstra como usar condicionais para verificar a temperatura e emitir alertas:

**Código Python:**

```python
temperatura = float(input("Digite a temperatura do reator em °C: "))
if temperatura > 100:
    print("Alerta: Temperatura excessiva!")
elif temperatura < 20:
    print("Alerta: Temperatura muito baixa!")
else:
    print("Temperatura dentro dos limites normais.")
```

**Resultado:**
```plaintext
Digite a temperatura do reator em °C: 120
Alerta: Temperatura excessiva!
Digite a temperatura do reator em °C: 15
Alerta: Temperatura muito baixa!
Digite a temperatura do reator em °C: 50
Temperatura dentro dos limites normais.
```

### 3.3.2. Controle de Nível em um Tanque

O nível de líquido em um tanque é outro parâmetro importante em muitos processos industriais. O código a seguir ilustra como usar condicionais para controlar o nível e acionar bombas ou válvulas:

**Código Python:**

```python
nivel = float(input("Digite o nível do líquido no tanque em %: "))
if nivel > 80:
    print("Alerta: Nível muito alto! Acionando bomba de drenagem.")
elif nivel < 20:
    print("Alerta: Nível muito baixo! Acionando bomba de enchimento.")
else:
    print("Nível dentro dos limites normais.")
```

**Resultado:**
```plaintext
Digite o nível do líquido no tanque em %: 85
Alerta: Nível muito alto! Acionando bomba de drenagem.
Digite o nível do líquido no tanque em %: 15
Alerta: Nível muito baixo! Acionando bomba de enchimento.
Digite o nível do líquido no tanque em %: 50
Nível dentro dos limites normais.
```

### 3.3.3. Verificação de Pressão em um Sistema de Tubulação

A pressão em um sistema de tubulação deve ser monitorada para evitar vazamentos ou rupturas. O código abaixo mostra como usar condicionais para verificar a pressão e emitir avisos:

**Código Python:**

```python
pressao = float(input("Digite a pressão do sistema em bar: "))
if pressao > 10:
    print("Alerta: Pressão excessiva!")
elif pressao < 2:
    print("Alerta: Pressão muito baixa!")
else:
    print("Pressão dentro dos limites normais.")
```

**Resultado:**
```plaintext
Digite a pressão do sistema em bar: 12
Alerta: Pressão excessiva!
Digite a pressão do sistema em bar: 1
Alerta: Pressão muito baixa!
Digite a pressão do sistema em bar: 5
Pressão dentro dos limites normais.
```
### 3.3.4. Contagem de Ciclos de um Equipamento

Em engenharia mecânica, é importante monitorar o número de ciclos de operação de um equipamento para programar a manutenção preventiva. O código a seguir usa um laço WHILE para simular a operação de um equipamento e contar os ciclos:

**Código Python:**

```python
ciclos = 0
while True:
    resposta = input("O equipamento está em operação? (s/n): ")
    if resposta == "s":
        ciclos += 1
        print(f"Ciclos de operação: {ciclos}")
    elif resposta == "n":
        print("Operação encerrada.")
        break
    else:
        print("Resposta inválida.")
```

**Resultado:**
```plaintext
O equipamento está em operação? (s/n): s
Ciclos de operação: 1
O equipamento está em operação? (s/n): s
Ciclos de operação: 2
O equipamento está em operação? (s/n): n
Operação encerrada.
```
### 3.3.5. Análise de Dados de Sensores

Em sistemas de automação, os dados dos sensores precisam ser analisados para tomar decisões em tempo real. O código a seguir usa um laço for para processar dados de um sensor de vibração e identificar valores anormais:

**Código Python:**

```python
dados_sensor = [0.1, 0.2, 0.15, 0.3, 0.25, 0.4]
for i, valor in enumerate(dados_sensor):
    if valor > 0.35:
        print(f"Alerta: Valor anormal detectado no ciclo {i + 1}: {valor}")
    else:
        print(f"Ciclo {i + 1} dentro dos limites normais: {valor}")
```

**Resultado:**
```plaintext
Ciclo 1 dentro dos limites normais: 0.1
Ciclo 2 dentro dos limites normais: 0.2
Ciclo 3 dentro dos limites normais: 0.15
Ciclo 4 dentro dos limites normais: 0.3
Alerta: Valor anormal detectado no ciclo 5: 0.25
Alerta: Valor anormal detectado no ciclo 6: 0.4
```
Estes exemplos demonstram a versatilidade das estruturas de controle na verificação de condições operacionais em diversos campos da engenharia. Ao utilizar IF, ELIF, ELSE, FOR e WHILE, os engenheiros podem criar programas que monitoram sistemas, detectam anomalias, acionam alarmes e automatizam ações de controle, contribuindo para a segurança, eficiência e confiabilidade dos processos e equipamentos.

---

## 3.4. Conclusão

Neste módulo, exploramos as estruturas de controle em Python, incluindo condicionais (IF, ELIF, ELSE) e laços de repetição (FOR, WHILE). Aprendemos como essas estruturas permitem que os programas tomem decisões lógicas e executem ações repetitivas, fundamentais para resolver problemas complexos em engenharia.
Através de exemplos práticos, vimos como aplicar essas estruturas para monitorar condições operacionais, controlar processos e automatizar tarefas. A compreensão e aplicação correta dessas estruturas são essenciais para desenvolver programas eficientes e eficazes em diversas áreas da engenharia.
Nos próximos módulos, continuaremos a explorar conceitos mais avançados de Python, como funções, manipulação de dados e bibliotecas específicas para engenharia, que nos permitirão criar soluções ainda mais robustas e complexas. A prática contínua com estruturas de controle fortalecerá suas habilidades de programação e sua capacidade de resolver problemas reais de engenharia.

---

## 4.4. Funções e Modularizações

Neste módulo 4, vamos explorar dois conceitos fundamentais para a organização e reutilização de código em Python: funções e modularização.
Primeiramente, abordaremos a definição de funções. Funções são blocos de código nomeados que realizam tarefas específicas. Aprenderemos a criar nossas próprias funções para encapsular a lógica de cálculos, processos ou outras operações que precisam ser executadas repetidamente em um programa. Isso evita a duplicação de código e torna os programas mais legíveis e fáceis de manter.
Em seguida, discutiremos parâmetros e retorno. Veremos como as funções podem receber dados de entrada através de parâmetros, permitindo que elas operem sobre diferentes valores. Também aprenderemos como as funções podem retornar resultados, possibilitando que elas forneçam informações para outras partes do programa. O uso adequado de parâmetros e retorno é essencial para criar funções flexíveis e reutilizáveis.
Finalmente, exploraremos a organização de código em módulos reutilizáveis. A modularização envolve a divisão de um programa em arquivos separados chamados módulos. Cada módulo pode conter funções, variáveis e outras definições relacionadas a uma funcionalidade específica. Aprenderemos a criar e importar módulos, o que nos permitirá estruturar projetos maiores de forma eficiente e reutilizar código entre diferentes programas.
Ao concluir este módulo, você estará apto a criar funções para organizar seu código, usar parâmetros e retorno para torná-las flexíveis e estruturar projetos em módulos para promover a reutilização e a manutenção eficiente do código, habilidades cruciais para o desenvolvimento de soluções de engenharia robustas e escaláveis.

---

## 4.1. Definição de Funções

Em Python, uma função é um bloco de código organizado e reutilizável que executa uma tarefa específica. Funções ajudam a dividir programas complexos em partes menores e gerenciáveis, tornando o código mais legível, organizado e fácil de manter.
As funções são definidas usando a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter parâmetros. O corpo da função é indentado abaixo da definição e contém o código que será executado quando a função for chamada.

### 4.1.1. Sintaxe de Definição de Função

A sintaxe para definir uma função em Python é a seguinte:
```python
def nome_da_funcao(parametros):
    # bloco de código a ser executado
    pass
```
**Componentes:**
- `def`: palavra-chave que indica o início da definição de uma função.
- `nome_da_funcao`: o nome da função, que deve ser descritivo e seguir as convenções de nomenclatura do Python.
- `parametros`: uma lista de variáveis que a função pode receber como entrada (opcional).
- `pass`: um comando que indica que a função não faz nada (pode ser substituído pelo código real da função).

### 4.1.2. Exemplo de Definição de Função

Vamos criar uma função simples que calcula a área de um retângulo. A função receberá dois parâmetros: a base e a altura do retângulo, e retornará a área calculada.

```python
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area
# Chamada da função
area = calcular_area_retangulo(5, 10)
print(f"A área do retângulo é: {area} m²")
```

**Resultado:**
```plaintext
A área do retângulo é: 50 m²
```
#### 4.1.3. Benefícios do Uso de Funções

As funções oferecem vários benefícios importantes na programação, especialmente em engenharia:

- Reutilização de código: Funções permitem que você execute o mesmo bloco de código várias vezes sem precisar reescrevê-lo.
- Organização do código: Funções ajudam a dividir programas grandes em partes menores e mais gerenciáveis, tornando o código mais fácil de entender e manter.
- Legibilidade do código: Funções tornam o código mais legível, pois dão nomes significativos a blocos de código, facilitando a compreensão do que cada parte do programa faz.
- Facilidade de manutenção: Se você precisar modificar o comportamento de uma parte específica do código, basta alterar a função correspondente, em vez de procurar e alterar o mesmo código em vários lugares.

No contexto da engenharia, as funções podem ser usadas para encapsular cálculos complexos, simulações, análises de dados e outras tarefas comuns, promovendo a eficiência e a clareza no desenvolvimento de software.

## 4.2. Parâmetros e Retorno

Parâmetros e retorno são mecanismos que permitem que as funções se comuniquem com o "mundo exterior", ou seja, que recebam dados para trabalhar e que forneçam resultados de volta para quem as chamou.

### 4.2.1. Parâmetros

Os parâmetros são variáveis que você define na declaração da função e que permitem que a função receba valores de entrada quando é chamada. Eles são especificados entre parênteses na definição da função.

**Sintaxe:**
```python
def nome_da_funcao(parametro1, parametro2):
    # bloco de código a ser executado
    pass
```
1) Tipos de Parâmetros: 

**Parâmetros Posicionais:** São os mais comuns. A ordem em que você passa os valores ao chamar a função deve corresponder à ordem em que os parâmetros são definidos na função.

**Parâmetros Nomeados (ou Palavra-Chave):** Ao chamar a função, você especifica o nome do parâmetro seguido do valor. Isso permite passar os argumentos em qualquer ordem.

**Parâmetros com Valores Padrão:** Você pode fornecer valores padrão para os parâmetros. Se um valor não for fornecido ao chamar a função, o valor padrão será usado.

**Número Variável de Argumentos:**
Você pode definir funções que aceitam um número variável de argumentos usando `*args` e `**kwargs`.

2) Exemplos de Parâmetros:

```python
def exemplo_args(*args):
    for i in args:
        print(i)

def exemplo_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamada da função com parâmetros posicionais
exemplo_args(1, 2, 3, 4)
# Chamada da função com parâmetros nomeados
exemplo_kwargs(nome="João", idade=30, cidade="São Paulo")
```

### 4.2.2. Retorno

O retorno é o mecanismo pelo qual uma função envia um resultado de volta para quem a chamou. Você pode usar a palavra-chave `return` para especificar o valor que a função deve retornar.

**Sintaxe:**
```python
def nome_da_funcao(parametros):
    # bloco de código a ser executado
    return valor_de_retorno
```

**Exemplo de Retorno:**
```python
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media
# Chamada da função
notas = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(notas)
print(f"A média das notas é: {media:.2f}")
```

**Resultado:**
```plaintext
A média das notas é: 7.75
```
**Importância:**
Parâmetros tornam as funções flexíveis e reutilizáveis, permitindo que operem em diferentes dados. O retorno permite que as funções produzam resultados que podem ser usados em outras partes do programa. Juntos, parâmetros e retorno são cruciais para a criação de funções modulares e eficientes.

### 4.2.3. Benefícios de Parâmetros e Retorno

Parâmetros e retorno oferecem vários benefícios importantes na programação, especialmente em engenharia:
- Flexibilidade: Permitem que as funções operem em diferentes dados, tornando-as reutilizáveis em várias situações.
- Modularidade: Facilitam a criação de funções que podem ser combinadas para resolver problemas complexos, promovendo a organização do código.
- Clareza: A utilização de parâmetros nomeados torna o código mais legível, pois deixa claro o propósito de cada argumento passado para a função.
- Eficiência: Permitem que as funções retornem resultados que podem ser usados imediatamente, evitando a necessidade de variáveis globais ou estados compartilhados.
- Testabilidade: Funções com parâmetros e retorno são mais fáceis de testar, pois você pode verificar se a função produz os resultados esperados para diferentes entradas.
Esses benefícios são essenciais para o desenvolvimento de software de engenharia, onde a clareza, a reutilização e a eficiência do código são fundamentais para resolver problemas complexos e garantir a qualidade das soluções.

---

## 4.3. Organização de Código em Módulos Reutilizáveis

A organização de código em módulos reutilizáveis é uma prática fundamental na programação, especialmente em projetos maiores e mais complexos. Módulos permitem que você divida seu código em arquivos separados, cada um contendo funções, classes e variáveis relacionadas a uma funcionalidade específica. Isso promove a reutilização de código, facilita a manutenção e melhora a legibilidade do programa.

### 4.3.1. O que são Módulos?
Módulos são arquivos Python que contêm definições de funções, classes e variáveis. Eles permitem que você organize seu código em partes lógicas, facilitando a reutilização e a manutenção. Você pode importar módulos em outros arquivos Python para acessar suas funcionalidades.

**Exemplo de Módulo:**
```python
# meu_modulo.py
def saudacao(nome):
    return f"Olá, {nome}!"

def soma(a, b):
    return a + b
# Variável global
mensagem = "Este é um módulo de exemplo."
```

### 4.3.2. Criando Módulos

Para criar um módulo, basta salvar o código Python em um arquivo .py.

**Exemplo:** Criando um módulo chamado calculos_geometricos.py

```python
# calculos_geometricos.py
def area_circulo(raio):
    import math
    return math.pi * raio**2

def perimetro_circulo(raio):
    import math
    return 2 * math.pi * raio
```
### 4.3.3. Importando Módulos

Para usar um módulo em outro arquivo Python, você deve importá-lo. Existem várias maneiras de importar módulos:

1. **Importação Simples:**
   ```python
   import meu_modulo
   print(meu_modulo.saudacao("Maria"))
   ```
2. **Importação Específica:**
   ```python
   from meu_modulo import saudacao
   print(saudacao("Maria"))
   ```
3. **Importação com Alias:**
   ```python
   import meu_modulo as mm
   print(mm.saudacao("Maria"))
   ```
4. **Importação de Todas as Funções:**
   ```python
   from meu_modulo import *
   print(saudacao("Maria"))
   print(soma(5, 10))
   ```

### 4.3.4. Benefícios da Modularização

A modularização oferece vários benefícios importantes na programação, especialmente em engenharia:
- Reutilização de Código: Módulos permitem que você reutilize funções e classes em diferentes projetos, economizando tempo e esforço.
- Organização: Dividir o código em módulos torna mais fácil entender e manter o programa, pois cada módulo pode ser focado em uma funcionalidade específica.
- Colaboração: Em projetos maiores, diferentes desenvolvedores podem trabalhar em módulos separados, facilitando a colaboração e a integração do código.
- Testabilidade: Módulos podem ser testados individualmente, o que facilita a identificação de bugs e a validação do comportamento esperado.
- Escalabilidade: Módulos permitem que você expanda seu código de forma organizada, adicionando novas funcionalidades sem comprometer a estrutura existente.
Esses benefícios são essenciais para o desenvolvimento de software de engenharia, onde a clareza, a reutilização e a eficiência do código são fundamentais para resolver problemas complexos e garantir a qualidade das soluções.

### 4.3.5. Exemplo de Uso de Módulos

```python
import geometria

raio = 5
base = 4
altura = 3

print(f"Área do círculo: {geometria.area_circulo(raio):.2f} m²")
print(f"Perímetro do círculo: {geometria.perimetro_circulo(raio):.2f} m")
print(f"Área do retângulo: {geometria.area_retangulo(base, altura)} m²")
print(f"Perímetro do retângulo: {geometria.perimetro_retangulo(base, altura)} m")
```
Vamos criar um exemplo prático que utiliza módulos para calcular áreas e perímetros de formas geométricas. Primeiro, criaremos um módulo chamado `geometria.py` que conterá funções para calcular a área e o perímetro de um círculo e um retângulo.

```python# geometria.py
import math

def area_circulo(raio):
    return math.pi * raio**2

def perimetro_circulo(raio):
    return 2 * math.pi * raio

def area_retangulo(base, altura):
    return base * altura

def perimetro_retangulo(base, altura):
    return 2 * (base + altura)  
```
Agora, podemos usar esse módulo em outro arquivo Python para realizar os cálculos. Vamos criar um arquivo chamado `main.py` que importa o módulo `geometria` e utiliza suas funções.

```python
# main.py
import geometria
raio = 5
base = 4
altura = 3
print(f"Área do círculo: {geometria.area_circulo(raio):.2f} m²")
print(f"Perímetro do círculo: {geometria.perimetro_circulo(raio):.2f} m")
print(f"Área do retângulo: {geometria.area_retangulo(base, altura)} m²")
print(f"Perímetro do retângulo: {geometria.perimetro_retangulo(base, altura)} m")
```
**Resultado:**
```plaintext
Área do círculo: 78.54 m²
Perímetro do círculo: 31.42 m
Área do retângulo: 12 m²
Perímetro do retângulo: 14 m
```
Neste exemplo, criamos um módulo `geometria.py` que contém funções para calcular a área e o perímetro de um círculo e um retângulo. Em seguida, importamos esse módulo no arquivo `main.py` e utilizamos suas funções para realizar os cálculos necessários. Isso demonstra como a modularização pode tornar o código mais organizado e reutilizável.

---

### 4.3.5 Exercício Proposto: Gestão de Inventário Florestal

**Descrição:**  
Um engenheiro florestal precisa desenvolver um sistema para gerenciar o inventário de uma floresta. O sistema deve calcular o volume de madeira em diferentes parcelas, verificar a idade das árvores para determinar o momento ideal de corte e gerar relatórios resumidos. Para organizar o código e facilitar a reutilização, o sistema será estruturado em módulos e funções.

**Requisitos:**
1. Criar um módulo `calculos_florestais.py` com funções para calcular o volume de uma árvore, a idade de corte e gerar relatórios.
2. No programa principal, importar o módulo, definir dados de exemplo de uma parcela florestal (lista de dicionários), chamar as funções do módulo e exibir o relatório na tela.

![EXERCICIO_PROPOSTO](imagens/09_imagem_exercicio_proposto.png)

---

#### Código do Módulo (`calculos_florestais.py`):

```python
import math

def calcular_volume(dap, altura, fator_forma=0.7):
    """Calcula o volume de uma árvore."""
    raio = dap / 2 / 100
    volume = math.pi * (raio ** 2) * altura * fator_forma
    return volume

def calcular_idade_corte(especie, crescimento_anual):
    """Calcula a idade estimada de corte para uma árvore."""
    idade_corte = 40 / crescimento_anual
    return int(idade_corte)

def gerar_relatorio(parcela, dados_arvores):
    """Gera um relatório sumarizado da parcela florestal."""
    relatorio = f"Relatório da Parcela: {parcela}\n"
    relatorio += "-----------------------------------\n"
    relatorio += "|  Espécie  | DAP (cm) | Altura (m) | Volume (m³) | Idade Corte (anos) |\n"
    relatorio += "-----------------------------------\n"
    for arvore in dados_arvores:
        volume = calcular_volume(arvore['dap'], arvore['altura'])
        idade_corte = calcular_idade_corte(arvore['especie'], arvore['crescimento_anual'])
        relatorio += f"| {arvore['especie']:<9} | {arvore['dap']:8.2f} | {arvore['altura']:8.2f} | {volume:9.3f} | {idade_corte:16} |\n"
    relatorio += "-----------------------------------\n"
    return relatorio
```

---

#### Programa Principal (`main.py`):

```python
import calculos_florestais

if __name__ == "__main__":
    dados_parcela = [
        {'especie': 'Eucalipto', 'dap': 15.5, 'altura': 12.0, 'idade': 7, 'crescimento_anual': 2.5},
        {'especie': 'Pinus', 'dap': 22.0, 'altura': 18.0, 'idade': 12, 'crescimento_anual': 1.8},
        {'especie': 'Acacia', 'dap': 10.0, 'altura': 8.5, 'idade': 5, 'crescimento_anual': 3.0}
    ]

    relatorio_parcela = calculos_florestais.gerar_relatorio("Parcela A1", dados_parcela)
    print(relatorio_parcela)
```

---

**Saída Esperada:**
```plaintext
Relatório da Parcela: Parcela A1
-----------------------------------
|  Espécie  | DAP (cm) | Altura (m) | Volume (m³) | Idade Corte (anos) |
-----------------------------------
| Eucalipto |    15.50 |      12.00 |      1.767 |                16 |
| Pinus     |    22.00 |      18.00 |      3.141 |                22 |
| Acacia    |    10.00 |       8.50 |      0.706 |                13 |
-----------------------------------
```

Este exercício simula um sistema de gestão de inventário florestal, onde o engenheiro florestal pode calcular o volume de madeira, a idade de corte e gerar relatórios sumarizados para diferentes parcelas florestais. A modularização do código permite que as funções sejam reutilizadas em diferentes contextos, promovendo a eficiência e a clareza no desenvolvimento de software de engenharia.

---

## 4.4. Conclusão

Neste módulo, mergulhamos nos conceitos de funções e modularização em Python, aprendendo a criar funções para encapsular a lógica de tarefas específicas, a utilizar parâmetros para torná-las flexíveis e a retornar valores para comunicar resultados. Demonstramos como a modularização permite organizar o código em módulos reutilizáveis, facilitando a manutenção, a colaboração e a escalabilidade de projetos. O exemplo prático de gestão de inventário florestal ilustrou a aplicação desses conceitos em um problema real de engenharia, evidenciando como funções e módulos contribuem para o desenvolvimento de soluções mais estruturadas, eficientes e fáceis de manter. O domínio desses conceitos é um passo fundamental para o desenvolvimento de software de alta qualidade em engenharia.

---