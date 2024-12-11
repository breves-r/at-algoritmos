def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if array[j]['pontuacao'] < array[min_index]['pontuacao']:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array

jogadores = [
    {'nome': 'Mariana', 'pontuacao': 60},
    {'nome': 'Bruno', 'pontuacao': 40},
    {'nome': 'Rafaela', 'pontuacao': 80}
]

print(selection_sort(jogadores))
