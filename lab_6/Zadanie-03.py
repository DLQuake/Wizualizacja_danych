# Zadanie 3
# Napisz funkcję, która będzie:

# przyjmowała jeden parametr n w postaci liczby całkowitej
# zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

import numpy as np


def tablica(n):
    return np.arange(1, n*n+1).reshape((n, n))


print(tablica(1))
print('\n------------------------\n')
print(tablica(2))
print('\n------------------------\n')
print(tablica(3))
print('\n------------------------\n')
print(tablica(4))
print('\n------------------------\n')
print(tablica(5))
