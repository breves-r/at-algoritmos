import time
import random

def bubble_sort(array):
    n = len(array)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def medir_tempo(lista):
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    return fim - inicio


lista1 = [random.randint(1, 1000) for _ in range(1000)]
lista2 = [random.randint(1, 10000) for _ in range(10000)]

tempo1 = medir_tempo(lista1)
tempo2 = medir_tempo(lista2)

print(f"Lista 1: {tempo1:.5f} segundos")
print(f"Lista 2: {tempo2:.5f} segundos")

