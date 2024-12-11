def knapsack(pesos_itens, valores_itens, capacidade_maxima):
    quantidade_itens = len(valores_itens)
    tabela_dp = [[0] * (capacidade_maxima + 1) for _ in range(quantidade_itens + 1)]

    for i in range(1, quantidade_itens + 1):
        for capacidade in range(capacidade_maxima + 1):
            peso_item = pesos_itens[i - 1]
            valor_item = valores_itens[i - 1]

            if i == 0 or capacidade == 0:
                tabela_dp[i][capacidade] = 0
            elif peso_item <= capacidade:
                tabela_dp[i][capacidade] = max(
                    valor_item + tabela_dp[i - 1][capacidade - peso_item],
                    tabela_dp[i - 1][capacidade]
                )
            else:
                tabela_dp[i][capacidade] = tabela_dp[i - 1][capacidade]

    return tabela_dp[quantidade_itens][capacidade_maxima]


pesos_itens = [1, 3, 4, 5]
valores_itens = [3, 4, 5, 7]
capacidade_maxima = 5

print(f"Valor máximo: {knapsack(pesos_itens, valores_itens, capacidade_maxima)}")
