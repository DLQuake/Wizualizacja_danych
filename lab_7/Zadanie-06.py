# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

import numpy as np

macierz = np.array([[0, 30, 45], [60, 90, 135]])

print('macierz')
print(macierz)

print()
b = np.empty((2, 3))
b = np.cos(macierz*np.pi/180)

print('b')
print(b)