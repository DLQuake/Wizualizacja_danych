# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

import numpy as np
import random

macierz1 = np.empty((3, 3), dtype=int)
macierz2 = np.empty((4, 4), dtype=int)

for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        macierz1[i, j] = random.random()*11

for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        macierz2[i, j] = random.random()*11


print('macierz1')
print(macierz1)
print()
print('Najnizsza wartosc w kolumnie 1: ', macierz1.min(axis=0)[0])
print('Najnizsza wartosc w kolumnie 2: ', macierz1.min(axis=0)[1])
print('Najnizsza wartosc w kolumnie 3: ', macierz1.min(axis=0)[2])
print()
print('Najnizsza wartosc w rzedzie 1: ', macierz1.min(axis=1)[0])
print('Najnizsza wartosc w rzedzie 2: ', macierz1.min(axis=1)[1])
print('Najnizsza wartosc w rzedzie 3: ', macierz1.min(axis=1)[2])
print()
print('============================================================')
print()
print('macierz2')
print(macierz2)
print()
print('Najnizsza wartosc w kolumnie 1: ', macierz2.min(axis=0)[0])
print('Najnizsza wartosc w kolumnie 2: ', macierz2.min(axis=0)[1])
print('Najnizsza wartosc w kolumnie 3: ', macierz2.min(axis=0)[2])
print('Najnizsza wartosc w kolumnie 4: ', macierz2.min(axis=0)[3])
print()
print('Najnizsza wartosc w rzedzie 1: ', macierz2.min(axis=1)[0])
print('Najnizsza wartosc w rzedzie 2: ', macierz2.min(axis=1)[1])
print('Najnizsza wartosc w rzedzie 3: ', macierz2.min(axis=1)[2])
print('Najnizsza wartosc w rzedzie 4: ', macierz2.min(axis=1)[3])
print()
