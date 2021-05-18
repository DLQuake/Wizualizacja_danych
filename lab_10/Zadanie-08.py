# Zadanie 8
# Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. Wynik rzutów zapisywany jest w postaci listy sum oczek z tych dwóch kostek.
# Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu. Po zakończeniu funkcji wyświetlaj histogram sumy
# rzutów. Dodaj stosowne etykiety do wykresu.

import numpy as np
import matplotlib.pyplot as plt

def rzucaj(n):
    return [(np.random.randint(6)+1)+(np.random.randint(6)+1) for _ in range(n)]

lista=rzucaj(6)
# print(lista)
plt.hist(lista, bins=6, facecolor='g', alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()