# Zadanie 3
# Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach: https://matplotlib.org/examples/color/colormaps_reference.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()

kolory = ['PiYG','PRGn','BrBG','PuOr','RdGy']
ax = fig.gca(projection = '3d')
# generuj dane.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

for i in range(321,326,1):
    # rysuj powierzchnię.
    surf = ax.plot_surface(X, Y, Z, cmap =kolory[i-321],linewidth = 0 , antialiased = False)
    ax.set_zlim(-1.01 , 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()