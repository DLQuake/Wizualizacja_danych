# Zadanie 5
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/zamowienia.csv', header=0, delimiter=";")

temp = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})

chart = temp.plot.bar()
chart.legend()

plt.title('Ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.show()
