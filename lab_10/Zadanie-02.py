# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

import matplotlib.pyplot as plt
import numpy as np

x=range(1,21)
y=[1/y for y in x]
plt.plot(x,y,label='f(x)=1/x',color='green', linestyle='dotted',marker='>')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,2.5))
plt.yticks(np.arange(0,1.1,0.1))
plt.title("Wykres funkcji f(x)=1/x dla x [1,20]")

plt.legend()
plt.show()