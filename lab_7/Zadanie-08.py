# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

import numpy as np
# generujemy macierz 3x3
b = np.arange(9).reshape(3, 3)
print(b)
for a in b:
    print(a)
