# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print('a:')
print(a)
print()

print('b:')
print(b)

print()
print('Wynik dodania macierzy a oraz b:')
print(a+b)

print()
print('Suma elementow macierzy a: ', np.sum(a))
print('Suma elementow macierzy b: ', np.sum(b))
print('Suma elementow sumy macierzy a oraz b: ', np.sum(a+b))
