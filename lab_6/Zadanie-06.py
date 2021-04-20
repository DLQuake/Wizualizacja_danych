# Zadanie 6
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo będzie wypisane w
# kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.

import numpy as np

malina = 'malina'
lizak = 'lizak'
jagoda = 'jagoda'

n = 7

wykreslanka = np.empty((n, n), dtype='str')

for i in range(0, n, 1):
    for j in range(0, n, 1):
        wykreslanka[i, j] = ' '

for i in range(0, len(lizak), 1):
    wykreslanka[i+1, 0] = lizak[i]

for i in range(0, len(malina), 1):
    wykreslanka[0, i+1] = malina[i]

for i in range(0, len(jagoda), 1):
    wykreslanka[i, i] = jagoda[i]

for i in range(0, n, 1):
    for j in range(0, n, 1):
        print(wykreslanka[i, j],'', end='')
    print()