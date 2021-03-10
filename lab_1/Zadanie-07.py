# Zadanie 7
# Wyświetl na konsoli tekst postaci „W tekście jest {liczba_liter1} liter … oraz {liczba_liter2} liter …” . W miejsca { } podstaw zmienne, które będą
# przechowywały liczbę wystąpień danych liter. Litery, które mają być wyszukane powinny zostać przekazane jako indeks do 3 znaku nazwiska
# oraz 2 znaku imienia osoby wykonującej ćwiczenie, np. imie = „Krzysztof”, nazwisko = „Ropiak”, litera_1 = imie[2], litera_2 = nazwisko[3].
imie="Dominik"
litera_1=imie[2]

nazwisko="Lewczyński"
litera_2=nazwisko[3]

print("W tekscie jest",imie.count(litera_1),"liter",litera_1,"w imieniu Dominik oraz",nazwisko.count(litera_2),"liter",litera_2," w nazwisku Lewczyński")