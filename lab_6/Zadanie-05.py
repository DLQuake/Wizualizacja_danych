# Zadanie 5
# Napisz funkcję, która:

# na wejściu przyjmuje jeden parametr określający długość wektora,
# na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# generuje macierz diagonalną z w/w wektorem jako przekątną

import numpy as np


def wektor(n):
    return np.diag(range(n, 0, -1))


print(wektor(1))
print('\n------------------------\n')
print(wektor(2))
print('\n------------------------\n')
print(wektor(3))
print('\n------------------------\n')
print(wektor(4))
print('\n------------------------\n')
print(wektor(5))
