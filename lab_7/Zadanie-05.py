# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

import numpy as np

macierz = np.array([[0, 30, 45], [60, 90, 135]])

print('macierz')
print(macierz)

print()
a = np.empty((2, 3))
a = np.sin(macierz*np.pi/180)

print('a')
print(a)
