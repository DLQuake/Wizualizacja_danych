# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

ts = pd.read_excel(pd.ExcelFile("datasets/imiona.xlsx"), "Arkusz1")
print(ts)

temp = ts.agg({"Rok": ['max']})
temp1 = ts[(ts["Rok"] <= temp.values[0][0]) & (ts["Rok"] > temp.values[0][0]-5)]
temp2 = temp1.groupby(['Plec']).agg({'Liczba': ['sum']})

chart = temp2.plot.pie(subplots=True, autopct='%.2f %%',fontsize=20, figsize=(6, 6))

plt.title('liczba urodzonych chłopców i dziewczynek w ostatnich 5 latach')
plt.show()
