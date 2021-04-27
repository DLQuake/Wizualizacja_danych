# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

import numpy as np

b = np.arange(81).reshape(9, 9)
print(b)
print(b.shape)

print('przeksztalacamy ja na macierz 3x27')
c = b.reshape((3, 27))
print(c)
print(c.shape)

print('przeksztalacamy ja na macierz 27x3')
d = c.reshape((27, 3))
print(d)
print(d.shape)

print('spłaszczamy macierz zyskujac pierwotny kształt ze zmiennej b')
e = d.ravel()
print(e)
print(e.shape)

print('transpozycja macierzy')
f = c.T
print(f)
print(f.shape)
