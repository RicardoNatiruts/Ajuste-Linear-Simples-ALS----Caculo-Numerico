def plotar_em_tabela(n, x, y, a_retas, b_retas, y_retas, desvios_retas, desvios_totais_retas):

    sinal_1 = "+" if b_retas[0] >= 0 else "-"
    sinal_2 = "+" if b_retas[1] >= 0 else "-"
    sinal_3 = "+" if b_retas[2] >= 0 else "-"
    
    eq_1 = f"Y_r1i = {a_retas[0]:.2f} {sinal_1} {abs(b_retas[0]):.2f}Xi"
    eq_2 = f"Y_r2i = {a_retas[1]:.2f} {sinal_2} {abs(b_retas[1]):.2f}Xi"
    eq_3 = f"Yi = {a_retas[2]:.2f} {sinal_3} {abs(b_retas[2]):.2f}Xi"
    print(f"{'':^39} | {eq_1:^33} | {eq_2:^33} | {eq_3:^33}")
    print(f"{'i':^11} | {'Xi':^11} | {'Yi':^11} | {'Y_r1i':^15} | {'D_r1i':^15} | {'Y_r2i':^15} | {'D_r2i':^15} | {'Yi':^15} | {'Di':^15}")

    for i in range(n):
        print(f"{i+1:^11} | {x[i]:^11.2f} | {y[i]:^11.2f} | {y_retas[0][i]:^15.2f} | {desvios_retas[0][i]:^15.2f} | {y_retas[1][i]:^15.2f} | {desvios_retas[1][i]:^15.2f} | {y_retas[2][i]:^15.2f} | {desvios_retas[2][i]:^15.2f}")

    print(f"{'':^39} | {'D_r1 = ' + f'{desvios_totais_retas[0]:.2f}':^33} | {'D_r2 = ' + f'{desvios_totais_retas[1]:.2f}':^33} | {'D = ' + f'{desvios_totais_retas[2]:.2f}':^33}")