# Zadanie 2 (1 pkt)
# Napisz funkcję, która z klawiatury przyjmuje tekst postaci „Imię Nazwisko” a następnie na wyjściu wyświetla, np. Marek Kowalski ->
# MK . Funkcja powinna sprawdzać i ewentualnie zamieniać pierwsze małe litery imienia i nazwiska na wielkie, czyli jeżeli
# wprowadzone zostanie marek kowalski to na wyjściu i tak będzie Marek Kowalski -> MK. Funkcja kończy działanie po wpisaniu słowa
# koniec.

def zadanie_2(tekst):
    if tekst=="koniec":
        print("nope")
    elif tekst.islower() == True:
        print(tekst[0].upper()+""+tekst[8].upper())

tekst="dominik lewczynski"
tekst1="koniec"
zadanie_2(tekst)
zadanie_2(tekst1)