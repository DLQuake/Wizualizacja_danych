# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich
# operację mnożenia.

import numpy as np

macierz_1 = np.array([1, 2, 3])  # liczby całkowite
macierz_2 = np.array([0.4, 0.5, 0.6])  # liczby rzeczywiste

print(macierz_1*macierz_2)

print("Jaki typ danych macierz_1: ", (macierz_1).dtype.name)
print("Jaki typ danych macierz_2: ", (macierz_2).dtype.name)
print("Jaki typ danych macierz_1*macierz_2: ",
      (macierz_1*macierz_2).dtype.name)
