# Zadanie 6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. Następnie na jednym płótnie wyświetl 3
# wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to
# ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
dane_wyk_1 = df.groupby(['Plec']).agg({'Liczba': 'sum'}).reset_index()
dane_wyk_2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
dane_wyk_3 = df.groupby(['Rok']).agg({'Liczba': 'sum'}).reset_index()

# Wykres 1
plt.subplot(1, 3, 1)
plt.bar(dane_wyk_1['Plec'], dane_wyk_1['Liczba'], color=['#762ca8', '#dde01f'])
plt.xlabel('Plec')
plt.ylabel('Ilosc urodzen')


# Wykres 2
plt.subplot(1, 3, 2)
plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'K']['Liczba'], label='Kobiety', color='#a0f06e')
plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'M']['Liczba'], label='Mężczyżni', color='#f0b86e')
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')
plt.legend()

# Wykres 3
plt.subplot(1, 3, 3)
plt.bar(dane_wyk_3['Rok'], dane_wyk_3['Liczba'],color='red')
plt.xlabel('Rok urodzenia')
plt.ylabel('Ilosc urodzen')

plt.show()
