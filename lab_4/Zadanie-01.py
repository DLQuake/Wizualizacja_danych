# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

liczby = []
for x in range(1, 100, 1):
    if x % 4 == 0:
        liczby += [x]

plik = open("liczby_podzielne_przez_4.txt", "w+")

plik.writelines(str(liczby))

plik.close()
