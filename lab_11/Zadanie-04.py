# Zadanie 4
# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot( 151 , projection = '3d' )
ax2 = fig.add_subplot( 152 , projection = '3d' )
ax3 = fig.add_subplot( 153 , projection = '3d' )
ax4 = fig.add_subplot( 154 , projection = '3d' )
ax5 = fig.add_subplot( 155 , projection = '3d' )

# fikcyjne dane
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade = True ,color='red')
ax1.set_title('Wykres zacieniony')

ax2.bar3d(x, y, bottom, width, depth, top, shade = True , color='orange')
ax2.set_title('Wykres przeswitujacy')

ax3.bar3d(x, y, bottom, width, depth, top, shade = False )
ax3.set_title('Wykres nie zacieniony')

ax4.bar3d(x, y, bottom, width, depth, top, shade = False ,color='yellow',edgecolor=['green','yellow','purple'])
ax4.set_title('Wykres z krawedziami')

ax5.bar3d(x, y, bottom, width, depth, top, shade = True ,color='green',zsort='max')
ax5.set_title('Wykres z krawedziami')
plt.show()
