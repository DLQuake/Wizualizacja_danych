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


def podpunkt_e(df):
    print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') &
              (df['Kraj'] == 'Polska'))].agg({'Utarg': ['sum']}))


def podpunkt_f(df):
    # możemy również oprócz zwracania określonej liczby wierszy Series lub DataFrame zwrócić określony fragment samego
    # wiersza, np. stringa. Tutaj dla każdego wiersze z kolumny 'Data zamowienia' zwracane są 4 pierwsze znaki czyli
    # wartość roku
    print(df['Data zamowienia'].str[:4])
    # tutaj tej samej techniki używamy do pogrupowania danych po roku (4-ech pierwszych znakach kolumny)
    print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg': ['mean']}))
    # tutaj wybieramy tylko określnone rekordy, gdzie pierwsze 4 znaki są równe 2004 i liczymy średnią
    print(df[((df['Data zamowienia'].str[:4] == '2004'))].agg(
        {'Utarg': ['mean']}))
    # lub za pomocą funkcji mean()
    print(df[((df['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())


def podpunkt_g(df):
    # stosując tę samą technikę filtrujemy dane dla wyznaczonych lat
    rok_2004 = df[((df['Data zamowienia'].str[:4] == '2004'))]
    rok_2005 = df[((df['Data zamowienia'].str[:4] == '2005'))]
    # można to oczywiście zrobić bardziej "klasycznie"
    rok_2004 = df[((df['Data zamowienia'] >= '2004-01-01') &
                   (df['Data zamowienia'] <= '2004-12-31'))]
    # zapisujemy dane do plików
    rok_2004.to_csv("zamowienia_2004.csv", index=False)
    rok_2005.to_csv("zamowienia_2005.csv", sep=';', index=False)


df = pd.read_csv('datasets/zamowienia.csv', header=0, delimiter=";")
# print(df)
# podpunkt_a(df)
# podpunkt_b(df)
# podpunkt_c(df)
# podpunkt_d(df)
# podpunkt_e(df)
# podpunkt_f(df)
# podpunkt_g(df)
