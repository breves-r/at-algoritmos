def busca_binaria(array, isbn):
    inicio = 0
    fim = len(array) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        
        if array[meio] == isbn:
            return meio, iteracoes
        elif array[meio] > isbn:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1, iteracoes

def busca_linear(array, isbn):
    iteracoes = 0
    for i in range(len(array)):
        iteracoes += 1
        if array[i] == isbn:
            return i, iteracoes
    return -1, iteracoes

array = list(range(1, 100001))
isbn = 99999

result_binaria, iteracoes_binaria = busca_binaria(array, isbn)
result_linear, iteracoes_linear = busca_linear(array, isbn)

print(f"Binária: {iteracoes_binaria}, Linear: {iteracoes_linear}")
