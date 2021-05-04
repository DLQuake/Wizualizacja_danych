# Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

# a) tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# b) tylko rekordy gdzie nadane imię jest takie jak Twoje
# c) sumę wszystkich urodzonych dzieci w całym danym okresie,
# d) sumę dzieci urodzonych w latach 2000-2005
# e) sumę urodzonych chłopców i dziewczynek,
# f) najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# g) najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

import pandas as pd
import xlrd
import openpyxl
from Zadanie_01 import df


def podpunkt_a(df):
    print(df[df['Liczba'] > 1000])


def podpunkt_b(df):
    print(df[df['Imie'] == 'DOMINIK'])


def podpunkt_c(df):
    print(df.agg({'Liczba': ['sum']}))


def podpunkt_d(df):
    urodzeni = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
    print(urodzeni.agg({'Liczba': ['sum']}))


def podpunkt_e(df):
    chlopcy = df[(df['Plec'] == 'M')]
    dziewczynki = df[(df['Plec'] == 'K')]

    print(chlopcy.agg({'Liczba': ['sum']}))
    print(dziewczynki.agg({'Liczba': ['sum']}))


def podpunkt_f(df):
    popularne = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])

    for i, g in enumerate(popularne, 1):
        print(f"{g[0]}")
        print(f"{g[1].iloc[[0],[1]].values[0][0]}", end=" ")
        print(f"{g[1].iloc[[0],[2]].values[0][0]}")


def podpunkt_g(df):
    dziewczynki = df[(df['Plec'] == 'K')]
    dziewczynki_popularne = df[(df['Plec'] == 'K')].max()
    print(dziewczynki[(dziewczynki['Liczba'] == dziewczynki_popularne['Liczba'])])

    chlopcy = df[(df['Plec'] == 'M')]
    chlopcy_popularne = df[(df['Plec'] == 'M')].max()
    print(chlopcy[(chlopcy['Liczba'] == chlopcy_popularne['Liczba'])])


# print(df)
# podpunkt_a(df)
# podpunkt_b(df)
# podpunkt_c(df)
# podpunkt_d(df)
# podpunkt_e(df)
# podpunkt_f(df)
# podpunkt_g(df)
