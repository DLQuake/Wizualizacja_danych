# Zadanie 8 (2 pkt)
# Napisz funkcję, która posiada zaszytą listę 3 nagród [‘samochód’, ‘10000 PLN’, ‘PS 4 Pro’]. Przygotuj plik z 10 imionami i nazwiskami
# zapisanymi po 1 w wierszu. Następnie funkcja wczytuje plik, losuje zwycięzcę dla każdej z trzech nagród i zapisuje wyniki w pliku o
# nazwie zwycięzcy.txt wpis postaci: Imię nazwisko, nagroda.


def zadanie_8(lista):
    plik = open("dozadanie8.txt", 'r')

    pom = plik.readlines()

    plik.close()

    for i in lista:
        lista_zwyciezcow=[]
        lista_zwyciezcow.append(str(pom))
        lista_zwyciezcow.append(lista[i])

    with open("zwyciezcy.txt", "w") as plik:
        for text in lista:
            plik.write(str(text)+"\n")
    print(pom)


lista=['samochód', '10000 PLN', 'PS 4 Pro']
zadanie_8(lista)
