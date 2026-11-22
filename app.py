from ALS import calcular_desvios, melhor_reta
from Plotar_Resultados import plotar_em_tabela, plotar_plano_cartesiano

n = int(input("Digite a quantidade de pontos: "))

abscissas = []
ordenadas = []

for i in range(n):
    x, y = map(float, input(f"Digite a coordenada {i+1}: ").split())
    abscissas.append(x)
    ordenadas.append(y)

a_retas = []
b_retas = []

for i in range(2):
    a, b = map(float, input(f"Digite os coeficientes da reta {i+1}: a + bx\n").split())
    a_retas.append(a)
    b_retas.append(b)

a_melhor_reta, b_melhor_reta = melhor_reta(n, abscissas, ordenadas)
a_retas.append(a_melhor_reta)
b_retas.append(b_melhor_reta)

y_retas = []
desvios_retas = []
desvios_totais_retas = []

for i in range(3):
    y_reta_atual = []
    desvios_reta_atual = []

    y_reta_atual, desvios_reta_atual, desvio_total = calcular_desvios(abscissas, ordenadas, a_retas[i], b_retas[i])

    y_retas.append(y_reta_atual)
    desvios_retas.append(desvios_reta_atual)
    desvios_totais_retas.append(desvio_total)

plotar_em_tabela(n, abscissas, ordenadas, a_retas, b_retas, y_retas, desvios_retas, desvios_totais_retas)

plotar_plano_cartesiano(abscissas, ordenadas, a_retas, b_retas, desvios_totais_retas)


 






