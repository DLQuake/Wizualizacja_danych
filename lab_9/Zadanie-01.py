# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

ts = pd.read_excel(pd.ExcelFile("datasets/imiona.xlsx"), "Arkusz1")
print(ts)
temp = ts.groupby(['Rok']).agg({'Liczba': ['sum']})
temp.plot()
plt.legend()
plt.show()
