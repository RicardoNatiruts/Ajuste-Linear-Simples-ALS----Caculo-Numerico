# 📈 Ajuste Linear Simples (ALS) em Python

Este projeto implementa um algoritmo completo e funcional em Python para **Cálculo Numérico** que resolve o problema de **Ajuste de Curvas** utilizando o método de **Ajuste Linear Simples (Mínimos Quadrados)**.

A aplicação recebe uma série de pontos amostrados $(x_i, y_i)$ e duas retas arbitrárias ($\hat{y} = a + bx$ e $\tilde{y} = c + dx$), calcula a **melhor reta** ($y = m + nx$) que minimiza o desvio total $D$, compara o desempenho das três retas por meio de uma tabela detalhada no terminal e exibe a comparação visualmente em um **Plano Cartesiano**.

## ✅ Funcionalidades

O projeto está **100% funcional**, contemplando a base matemática, a exibição tabular e a visualização gráfica:

* **Motor Matemático (`ALS.py`):**
  * Cálculo dos somatórios necessários ($\sum x_i$, $\sum y_i$, $\sum x_i^2$ e $\sum x_i y_i$).
  * Determinação dos coeficientes linear ($b_0$) e angular ($b_1$) da melhor reta pelo método de minimização:
    $$b_1 = \frac{n \cdot \sum x_i y_i - \sum x_i \sum y_i}{n \cdot \sum x_i^2 - (\sum x_i)^2} \qquad \text{e} \qquad b_0 = \frac{\sum y_i - (\sum x_i) b_1}{n}$$
  * Cálculo dos valores estimados ($\hat{y}_i$), dos desvios individuais ($d_i = y_i - \hat{y}_i$) e do Desvio Total quadrático ($D = \sum_{i=1}^{n} d_i^2$) para cada reta.
* **Exibição em Tabela (`Plotar_Resultados.py`):** Formatação alinhada no terminal comparando lado a lado os pontos originais, os valores estimados, os desvios individuais e o Desvio Total ($D$) das três retas (com tratamento automático de sinais positivos e negativos nas equações).
* **Plotagem em Plano Cartesiano (`Plotar_Resultados.py`):** Gráfico interativo gerado com `matplotlib` contendo:
  * Os pontos amostrados em um diagrama de dispersão (azul).
  * As duas retas arbitrárias (amarelo tracejado e traço-ponto) e a **Melhor Reta** (verde sólida).
  * Eixos cartesianos ($x = 0$ e $y = 0$), grade de referência e legenda com a equação e o Desvio Total ($D$) de cada reta.
* **Interface de Terminal (`app.py`):** Script principal que coleta a quantidade de pontos, as coordenadas $(x_i, y_i)$ e os coeficientes das duas retas aleatórias, integrando o processamento, a saída tabular e a exibição do gráfico.

## 📋 Etapas Concluídas

* [x] **Lógica do Ajuste Linear Simples:** Cálculo da melhor reta e dos desvios totais ($D$).
* [x] **Tabela Comparativa:** Exibição estruturada no terminal com as 3 retas e seus desvios.
* [x] **Representação Visual (Plano Cartesiano):** Plotagem dos pontos amostrados (diagrama de dispersão) e das três retas envolvidas no mesmo gráfico utilizando `matplotlib`.

## 🚀 Como executar

Certifique-se de ter o **Python 3+** e a biblioteca **matplotlib** instalados em sua máquina.

1. Clone o repositório ou baixe os arquivos.
2. Instale a dependência para a plotagem gráfica (caso ainda não tenha):
   ```bash
   pip install matplotlib
   ```
3. Abra o terminal e navegue até a pasta do projeto.
4. Execute o arquivo principal:
   ```bash
   python app.py
   ```
5. Informe a quantidade de pontos $n$, digite cada coordenada `x y` separada por espaço e, por fim, os coeficientes `a b` de cada reta aleatória no formato $a + bx$:
   ```text
   Digite a quantidade de pontos: 4
   Digite a coordenada 1: 1 3
   Digite a coordenada 2: 2 6
   Digite a coordenada 3: 3 7
   Digite a coordenada 4: 4 10
   Digite os coeficientes da reta 1: a + bx
   0 2
   Digite os coeficientes da reta 2: a + bx
   2 1
   ```
6. Após a entrada dos dados, a tabela comparativa será exibida no terminal e a janela do gráfico no **Plano Cartesiano** será aberta automaticamente.

## 📂 Estrutura de Arquivos

* `ALS.py`: Contém as funções auxiliares de somatório e desvio, além das funções principais `calcular_desvios()` e `melhor_reta()`.
* `Plotar_Resultados.py`: Responsável pela apresentação dos dados no terminal com `plotar_em_tabela()` e pela visualização gráfica com `plotar_plano_cartesiano()`.
* `app.py`: Ponto de entrada do programa. Gerencia as entradas do usuário e coordena as chamadas entre os módulos.
