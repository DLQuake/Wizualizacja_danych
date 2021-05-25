# Zadanie 5
# W przykładzie 3 zmień gęstość próbek do wykresu na krok 0.1 oraz włącz antyaliasing. Wyświetl pierwotny i nowy wykres obok siebie.


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()

for i,d,an in ([121,0.25,False],[122,0.1,True]):
    ax = fig.add_subplot(i,projection = '3d')
    # generuj dane.
    X = np.arange(-5, 5, d)
    Y = np.arange(-5, 5, d)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    # rysuj powierzchnię.
    surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
    linewidth = 0 , antialiased = an)
    ax.set_zlim(-1.01 , 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()