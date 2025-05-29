# 📊 Lógica e Fluxos do Simulador de Restaurante

---

## 1. Tipos de Simulação

### 1.1 Simulação Determinística

- **Definição:** Resultados sempre iguais para os mesmos parâmetros, sem aleatoriedade.
- **Características:**
  - Parâmetros fixos (ex: 12 clientes/minuto, 30 min/refeição)
  - Sem filas, sem variabilidade individual
  - Cálculo direto:
    - `total_clientes = clientes/min × tempo_total`
    - `capacidade_total = mesas × cadeiras`
- **Aplicação:** Planejamento teórico, capacidade máxima, cenários estáticos.

### 1.2 Simulação de Eventos Discretos (DES)

- **Definição:** O sistema evolui por eventos (chegada, atendimento, saída), com variabilidade e controle de recursos.
- **Características:**
  - Aleatoriedade nos tempos de chegada e atendimento
  - Controle de ocupação de mesas, filas, rejeição de clientes
  - Resultados diferentes a cada execução
- **Aplicação:** Avaliação realista de filas, gargalos, rotatividade, tomada de decisão operacional.

### 1.3 Comparativo

| Característica   | Simulação Determinística | Simulação de Eventos Discretos |
|------------------|:-----------------------:|:------------------------------:|
| Aleatoriedade    | Não                     | Sim                            |
| Variabilidade    | Não                     | Sim                            |
| Cálculo          | Direto                  | Baseado em eventos             |
| Aplicação        | Planejamento teórico    | Análise operacional            |

---

## 2. Fluxo Lógico do Simulador

### 2.1 Algoritmo Geral

```plaintext
+-----------------------------+
|     Início da Simulação     |
+-----------------------------+
              |
              v
|  Ler parâmetros de entrada  |
|  (clientes/min, tempo_refeição, mesas, etc.) |
              |
              v
| Validar tempo_total_simul. (máx. 12h) |
              |
              v
| Calcular total_clientes e capacidade_total |
              |
              v
| Iniciar simulação minuto a minuto         |
              |
              v
| Atualizar ocupação das mesas              |
              |
              v
| Gerar frames PNG do layout (intervalos)   |
              |
              v
| Montar GIF animado do layout              |
              |
              v
| Calcular estatísticas finais              |
              |
              v
| Armazenar resultados em dicionário        |
              |
              v
| Exportar relatório PDF e informar GIF     |
              |
              v
|        Fim da Simulação                   |
+-----------------------------+
```

---

## 3. Fluxograma do Programa

```plaintext
Início do Programa
      |
Selecionar fonte dos parâmetros (manual, Excel, YAML)
      |
Importar layout ASCII
      |
Validar dados e layout
      |
Executar Simulação (determinística ou DES)
      |
Atualizar ocupação das mesas minuto a minuto
      |
Gerar frames PNG do layout
      |
Montar GIF animado do layout
      |
Gerar relatório PDF com os resultados
      |
Exibir caminhos dos arquivos gerados (PDF/GIF)
      |
Encerrar programa
```

---

## 4. Diagrama de Sequência (Resumo Modular)

```plaintext
Usuário
  |
main.py
  |
src/interface.py
  |---> src/yaml_loader.py / src/excel_loader.py / importar_dados_txt
  |---> src/layout_parser.py
  |---> src/simulador.py
           |---> src/logger_config.py
           |---> src/visualizador_layout.py (frames/GIF)
           |---> src/pdf_exporter.py (PDF)
           |<--- resultado
  |
Relatórios PDF e GIF animado gerados
```

---

## 5. Relatório e Visualização

O simulador gera dois principais artefatos ao final de cada execução:

- **Relatório PDF:**  
  Contém os parâmetros utilizados na simulação, estatísticas finais (como tempo médio de espera, taxa de ocupação das mesas, número de clientes atendidos e rejeitados), recomendações de otimização e caminhos dos arquivos gerados. O relatório é formatado para facilitar a análise gerencial e pode ser personalizado conforme a necessidade do usuário.

- **GIF Animado:**  
  Mostra a evolução do layout do restaurante ao longo do tempo, destacando visualmente a ocupação das mesas, movimentação dos clientes, buffet, caixa e áreas de circulação. Essa animação auxilia na identificação de gargalos e na compreensão do fluxo operacional.

---

## 6. Observações e Recomendações

- Os parâmetros de simulação podem ser ajustados conforme dados reais coletados no restaurante ou para testar cenários hipotéticos.
- O simulador permite comparar diferentes estratégias de layout, atendimento e gestão de filas, apoiando decisões baseadas em dados.
- Para análises mais realistas e identificação de gargalos, recomenda-se utilizar a simulação de eventos discretos (DES).
- O sistema foi desenvolvido de forma modular, facilitando a integração com novos módulos de visualização, exportação ou coleta de dados.
- Recomenda-se a coleta periódica de dados reais para calibrar o simulador e garantir maior aderência à realidade operacional do restaurante.

---

> **Resumo:**  
> O simulador de restaurantes por quilo oferece uma abordagem flexível e realista para análise operacional, permitindo desde cálculos teóricos até simulações dinâmicas com visualização gráfica e relatórios executivos. Sua aplicação contribui para a melhoria contínua dos processos, otimização do atendimento e suporte à tomada de decisão gerencial.