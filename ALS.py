#Funções Auxiliares (Desvios)

def funcao_ordenadas(a, b, x):
    return a + b*x

def desvio_ponto(y, y_o):
    return y - y_o

def desvio_total(d):
    d_total = 0

    for desvio_y in d:
        d_total += desvio_y**2

    return d_total


#Funções Auxiliares (Melhor Reta)

def somatorio_abscissas(x):
    x_total = 0

    for abscissa in x:
        x_total += abscissa

    return x_total

def somatorio_ordenadas(y):
    y_total = 0

    for ordenada in y:
        y_total += ordenada

    return y_total

def somatorio_abscissas_quadrada(x):
    x_total = 0

    for abscissa in x:
        abscissa_quadrada = pow(abscissa,2)
        x_total += abscissa_quadrada

    return x_total

def somatorio_produto(x, y):
    total = 0
    n = 0 

    for abscissa in x:
        total += abscissa*y[n]
        n+=1
    return total

def calcular_coeficiente_angular(n, sxy, sx, sy, sxq):
    return (n * sxy - (sx * sy)) / (n * sxq - pow(sx, 2))

def calcular_coeficiente_linear(n, sx, sy, coe_ang):
    return (sy - (sx * coe_ang)) / n



#Funções Principais (Desvios e Melhor Reta)

#Desvios

def calcular_desvios(x, y, a, b):
    """
    Calcula as ordenadas estimadas pela reta, os desvios individuais (di) para cada ponto
    e o desvio total quadrático (D) de uma reta específica.

    @param x: Lista com as abscissas (valores de x) dos pontos amostrados (list[float]).
    @param y: Lista com as ordenadas (valores de y) reais dos pontos amostrados (list[float]).
    @param a: Coeficiente linear da reta a ser avaliada (float).
    @param b: Coeficiente angular da reta a ser avaliada (float).
    @return: Tupla (ordenadas_reta, desvio_resultado, desvio_total_reta) contendo a lista de
             valores estimados de y (list[float]), a lista de desvios individuais (list[float])
             e o desvio total quadrático D (float)[cite: 2].
    """

    ordenadas_reta = []

    for abscissa in x:
        resultado = funcao_ordenadas(a, b, abscissa)
        ordenadas_reta.append(resultado)

    desvio_resultado = []
    n = 0

    for ordenada in y:
        resultado = desvio_ponto(ordenada, ordenadas_reta[n])
        n+=1
        desvio_resultado.append(resultado)

    desvio_total_reta = desvio_total(desvio_resultado)

    return ordenadas_reta, desvio_resultado, desvio_total_reta

#Melhor Reta

def melhor_reta(n, x, y):
    """
    Calcula os coeficientes da melhor reta pelo método de Ajuste Linear Simples (Mínimos Quadrados)
    a partir dos somatórios das coordenadas fornecidas[cite: 2].

    @param n: Quantidade total de pontos amostrados (int).
    @param x: Lista com as abscissas (valores de x) dos pontos de entrada (list[float]).
    @param y: Lista com as ordenadas (valores de y) dos pontos de entrada (list[float]).
    @return: Tupla (coeficiente_linear, coeficiente_angular) contendo respectivamente os
             coeficientes a e b da melhor reta (tuple[float, float])[cite: 2].
    """
    
    som_x = somatorio_abscissas(x)
    som_y = somatorio_ordenadas(y)
    som_x_quadrado = somatorio_abscissas_quadrada(x)
    som_prod = somatorio_produto(x, y)

    coeficiente_angular = calcular_coeficiente_angular(n, som_prod, som_x, som_y, som_x_quadrado)
    coeficiente_linear = calcular_coeficiente_linear(n, som_x, som_y, coeficiente_angular)

    return coeficiente_linear, coeficiente_angular