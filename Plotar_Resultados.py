import matplotlib.pyplot as plt

#| PLOTAR EM TABELA NO TERMINAL |

def plotar_em_tabela(n, x, y, a_retas, b_retas, y_retas, desvios_retas, desvios_totais_retas):
    """
    Exibe no terminal uma tabela formatada comparando os pontos amostrados, os valores
    estimados, os desvios individuais (di) e o desvio total (D) das três retas.

    @param n: Quantidade total de pontos amostrados (int).
    @param x: Lista com as abscissas (valores de x) dos pontos de entrada (list[float]).
    @param y: Lista com as ordenadas (valores de y) dos pontos de entrada (list[float]).
    @param a_retas: Lista com os coeficientes lineares das 3 retas [reta1, reta2, melhor_reta] (list[float]).
    @param b_retas: Lista com os coeficientes angulares das 3 retas [reta1, reta2, melhor_reta] (list[float]).
    @param y_retas: Matriz contendo as listas de ordenadas estimadas para cada uma das 3 retas (list[list[float]]).
    @param desvios_retas: Matriz contendo as listas de desvios individuais (di) de cada reta (list[list[float]]).
    @param desvios_totais_retas: Lista com o desvio total quadrático (D) de cada uma das 3 retas (list[float]).
    @return: None (apenas imprime a tabela formatada no console).
    """

    #Confere o sinal de n para y = m + ny
    sinal_1 = "+" if b_retas[0] >= 0 else "-"
    sinal_2 = "+" if b_retas[1] >= 0 else "-"
    sinal_3 = "+" if b_retas[2] >= 0 else "-"

    #Prepara o cabeçalho
    eq_1 = f"Y_r1i = {a_retas[0]:.2f} {sinal_1} {abs(b_retas[0]):.2f}Xi"
    eq_2 = f"Y_r2i = {a_retas[1]:.2f} {sinal_2} {abs(b_retas[1]):.2f}Xi"
    eq_3 = f"Yi = {a_retas[2]:.2f} {sinal_3} {abs(b_retas[2]):.2f}Xi"

    #Cabeçalho
    print(f"{'':^39} | {eq_1:^33} | {eq_2:^33} | {eq_3:^33}")

    #Sub-cabeçalho
    print(f"{'i':^11} | {'Xi':^11} | {'Yi':^11} | {'Y_r1i':^15} | {'D_r1i':^15} | {'Y_r2i':^15} | {'D_r2i':^15} | {'Yi':^15} | {'Di':^15}")

    #Resultados obtidos
    for i in range(n):
        print(f"{i+1:^11} | {x[i]:^11.2f} | {y[i]:^11.2f} | {y_retas[0][i]:^15.2f} | {desvios_retas[0][i]:^15.2f} | {y_retas[1][i]:^15.2f} | {desvios_retas[1][i]:^15.2f} | {y_retas[2][i]:^15.2f} | {desvios_retas[2][i]:^15.2f}")

    #Desvios finais das retas
    print(f"{'':^39} | {'D_r1 = ' + f'{desvios_totais_retas[0]:.2f}':^33} | {'D_r2 = ' + f'{desvios_totais_retas[1]:.2f}':^33} | {'D = ' + f'{desvios_totais_retas[2]:.2f}':^33}")



#| PLOTAR EM PLANO CARTESIANO |


def plotar_plano_cartesiano(x, y, a_retas, b_retas, desvios_totais_retas):
    """
    Gera e exibe um gráfico no plano cartesiano contendo os pontos amostrados (dispersão)
    e as três retas (duas aleatórias e a melhor reta), com suas equações e valores de D na legenda.

    @param x: Lista com as abscissas (valores de x) dos pontos de entrada (list[float]).
    @param y: Lista com as ordenadas (valores de y) dos pontos de entrada (list[float]).
    @param a_retas: Lista com os coeficientes lineares das 3 retas [reta1, reta2, melhor_reta] (list[float]).
    @param b_retas: Lista com os coeficientes angulares das 3 retas [reta1, reta2, melhor_reta] (list[float]).
    @param desvios_totais_retas: Lista com o desvio total quadrático (D) de cada uma das 3 retas (list[float]).
    @return: None (abre a janela interativa do matplotlib com o gráfico).
    """

    #Pega o menor e maior x
    x_min = min(x) - 1
    x_max = max(x) + 1
    x_linha = [x_min, x_max]    

    #Pega os pontos minimos e maximos de cada reta
    y_r1 = [a_retas[0] + b_retas[0] * x_min, a_retas[0] + b_retas[0]*x_max]
    y_r2 = [a_retas[1] + b_retas[1] * x_min, a_retas[1] + b_retas[1]*x_max]
    y_mr = [a_retas[2] + b_retas[2] * x_min, a_retas[2] + b_retas[2]*x_max]

    #Confere o sinal de n para y = m + ny
    s1 = "+" if b_retas[0] >= 0 else "-"
    s2 = "+" if b_retas[1] >= 0 else "-"
    s3 = "+" if b_retas[2] >= 0 else "-"

    plt.figure(figsize=(10, 6))

    plt.scatter(x, y, color= "blue", s=50, zorder=5, label="Pontos amostrados")

    #Constrói as retas (Amarelo = retas da entrada; Verde = melhor reta)
    plt.plot(
        x_linha, y_r1,
        color  ="gold", linestyle="--", linewidth=1.8,
        label=f"Reta 1: y = {a_retas[0]:.2f} {s1} {abs(b_retas[0]):.2f}x (D = {desvios_totais_retas[0]:.2f})"
        )

    plt.plot(
            x_linha, y_r2,
            color  ="gold", linestyle="-.", linewidth=1.8,
            label=f"Reta 2: y = {a_retas[1]:.2f} {s2} {abs(b_retas[1]):.2f}x (D = {desvios_totais_retas[1]:.2f})"
            )

    plt.plot(
                x_linha, y_mr,
                color  ="green", linestyle="-", linewidth=2.5,
                label=f"Melhor Reta: y = {a_retas[2]:.2f} {s3} {abs(b_retas[2]):.2f}x (D = {desvios_totais_retas[2]:.2f})"
                )

    #Constrói o Plano Cartesiano
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.grid(True, linestyle=":", alpha=0.7)

    #Ajusta as configuções do Plano Cartesiano
    plt.title("Ajuste Linear Simples (ALS) - Comparação de Retas")
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo Y")
    plt.legend(loc="best")
    plt.tight_layout()

    #Abre o Plano Cartesiano
    plt.show()
