# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:

# a) listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# b) 5 najwyższych wartości zamówień
# c) ilość zamówień złożonych przez każdego sprzedawcę
# d) sumę zamówień dla każdego kraju
# e) sumę zamówień dla roku 2005, dla sprzedawców z Polski
# f) średnią kwotę zamówienia w 2004 roku,
# g) zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.cbg

import pandas as pd


def podpunkt_a(df):
    print(df.Sprzedawca.unique())


def podpunkt_b(df):
    print(df.sort_values('Utarg', ascending=False).iloc[:5])


def podpunkt_c(df):
    print(df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))


def podpunkt_d(df):
    print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))

# def podpunkt_e(df): TODO

# def podpunkt_f(df): TODO

# def podpunkt_g(df): TODO


df = pd.read_csv('datasets/zamowienia.csv', header=0, delimiter=";")
# print(df)
# podpunkt_a(df)
# podpunkt_b(df)
# podpunkt_c(df)
# podpunkt_d(df)
# podpunkt_e(df)
# podpunkt_f(df)
# podpunkt_g(df)
