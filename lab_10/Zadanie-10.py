# Zadanie 10
# Poszukaj w bibliotece wykresów (https://matplotlib.org/gallery/index.html) przykładów z adnotacjami (annotating plots) na wykresach i dodaj
# adnotacje do dwóch wybranych stworzonych wcześniej wykresów.

# TODO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# adnotacje do wykresu z zadania 7

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg(
    {'Liczba': ['sum']}).values.flatten()
mezczyzni = df[(df.Plec == 'M')].groupby(
    'Rok').agg({'Liczba': ['sum']}).values.flatten()
ax1 = plt.bar(x, kobiety, label="Kobiety")
ax2 = plt.bar(x, mezczyzni, label="Mężczyźni", bottom=kobiety)
# dodamy adnotację do najwyższego słupka wykresu
# na początek rozszerzymy nieco skalę osi Y, żeby adnotacja się zmieściła
# ylim() zwraca krotkę wartości skali (bottom, top) więc możemy najpierw ją pobrać
# a później jeżeli przekazujemy wartości dla funkcji ylim(bottom, top) to ustawiamy te wartości
plt.ylim(plt.ylim()[0], plt.ylim()[1]*1.2)
# teraz trzeba zlokalizować najwyższy słupek, co przy skumulowanym wykresie nie jest już tak łatwe
# ax1 oraz ax2 to odpowiednio serie słupków dla kobiet i mężczyzn
wys_slupkow_ax1 = np.array([p.get_height() for p in ax1.patches])
wys_slupkow_ax2 = np.array([p.get_height() for p in ax2.patches])
suma_wysokosci = wys_slupkow_ax1 + wys_slupkow_ax2
# teraz trzeba zlokalizować, który to słupek
slupek_index = np.where(suma_wysokosci == max(suma_wysokosci))[0][0]
# następnie pobierając parametry słupka o danym indeksie możemy dodać adnotację do wykresu
slupek1 = ax1.patches[slupek_index]
slupek2 = ax2.patches[slupek_index]
# przykład adnotacji w postaci tekstu i strzałki zaczerpnięty z
# https://matplotlib.org/examples/pylab_examples/annotation_demo.html
plt.annotate('To najwyższy słupek',
             xy=(slupek1.get_x(), (slupek1.get_height() +
                                   slupek2.get_height()) * 1.01),
             xycoords='data',
             xytext=(-15, 25), textcoords='offset points',
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='bottom')
# tiki osi x co drugi rok
plt.xticks(x[::2])
plt.ylabel('Liczba narodzonych dzieci')
plt.xlabel('Rok')
plt.legend()
plt.show()

# adnotacja do wykresu sinusoidy, ale lokalizacja wskazana poprzez podanie wartości z osi x oraz y, na przecięciu
# których adnotacja ma się znaleźć
x = np.arange(0, 30, 0.1)
s = np.sin(x)
plt.plot(x, s, label='sin(x)')

# etykiety osi
plt.xlabel('x')
plt.ylabel('sin(x)')

# adnotacja
plt.annotate('początek wykresu',
             xy=(0, 0), xycoords='data',
             xytext=(0.3, 0.3), textcoords='axes fraction',
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')
# i jeszcze jedna
plt.annotate('koniec wykresu',
             xy=(x[-1], s[-1]), xycoords='data',
             xytext=(0.7, 0.7), textcoords='axes fraction',
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='left', verticalalignment='top')

# tytuł wykresu
plt.title("Wykres sin(x)")

# włączamy pokazywanie legendy
plt.legend()
plt.show()
