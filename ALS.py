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
    som_x = somatorio_abscissas(x)
    som_y = somatorio_ordenadas(y)
    som_x_quadrado = somatorio_abscissas_quadrada(x)
    som_prod = somatorio_produto(x, y)

    coeficiente_angular = calcular_coeficiente_angular(n, som_prod, som_x, som_y, som_x_quadrado)
    coeficiente_linear = calcular_coeficiente_linear(n, som_x, som_y, coeficiente_angular)

    return coeficiente_linear, coeficiente_angular