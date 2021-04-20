# Zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do
# wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2 4 8 16]

import numpy as np


def potega(n, base):
    return np.logspace(1, n, num=n, base=base)


print(potega(1, 5))
print(potega(2, 4))
print(potega(3, 3))
print(potega(4, 2))
print(potega(5, 1))
