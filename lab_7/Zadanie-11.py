# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich
# i wyświetl wyniki. Czy są identyczne?

import numpy as np

a = np.arange(12)
print(a)

print('Przeksztalcamy ja na macierz 3x4')
print(a.reshape((3, 4)))

print('Przeksztalcamy ja na macierz 4x3')
print(a.reshape((4, 3)))

print('Przeksztalcamy ja na macierz 2x6')
print(a.reshape((2, 6)))

print('===============================================================')

print('Splaszczona macierz 3x4')
b = a.reshape((3, 4)).ravel()
print(a.reshape((3, 4)).ravel())

print('Splaszczona macierz 4x3')
c = a.reshape((4, 3)).ravel()
print(c)

print('Splaszczona macierz 2x6')
d = a.reshape((2, 6)).ravel()
print(d)

print()
print('Czy te macierze sa identyczne? ')
print('\n')
if a.all() == b.all() and b.all() == c.all() and c.all() == d.all():
    print('Sa identyczne')
else:
    print('Nie sa identyczne')
