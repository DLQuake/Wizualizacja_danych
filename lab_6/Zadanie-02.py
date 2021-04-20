# # Zadanie 2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.

import numpy as np

tablica1 = np.arange(1, 10, 0.2)
tablica2 = tablica1.astype('int64')
print(tablica1)
print(tablica2)
