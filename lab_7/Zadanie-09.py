# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy.

import numpy as np
# generujemy macierz 3x3
b = np.arange(9).reshape(3, 3)
print(b)
for a in b.flat:
    # iterujemy jakby to była macierz płaska
    print(a, end=' ')
