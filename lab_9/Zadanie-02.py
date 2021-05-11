# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

ts = pd.read_excel(pd.ExcelFile("datasets/imiona.xlsx"), "Arkusz1")
print(ts)
temp = ts.groupby(['Plec']).agg({'Liczba': ['sum']})

chart = temp.plot.bar()
chart.set_ylabel('Mld')
chart.legend()
plt.title('Ilosc urodzen chlopcow i dziewczynek z okresu 2000 - 2017')
plt.show()
