# Zadanie 7
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:

# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:

# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

import numpy as np

def macierz(n):
    mat = np.diag([2 for _ in range(n)])
    for indeks in range(1, n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        mat += np.diag(vec, indeks)
        mat += np.diag(vec, -indeks)
    return mat

print(macierz(3))