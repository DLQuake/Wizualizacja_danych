# Zadanie 7
# Korzystając z tutoriala pod adresem https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-
# b5d1b8f67596 lub innego zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast wykresu liniowego przedstawiał wykres łupkowy skumulowany
# (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków). Przykład:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
dane_wyk_2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
plt.bar(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'M']['Liczba'], label='Mężczyżni', color='blue')
plt.bar(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'K']['Liczba'], label='Kobiety', color='red',bottom=dane_wyk_2[dane_wyk_2['Plec'] == 'M']['Liczba'])
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')
plt.legend()

plt.xticks(dane_wyk_2['Rok'].unique(),rotation=60)
plt.show()