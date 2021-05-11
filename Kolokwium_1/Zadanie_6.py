# Zadanie 6 (1 pkt)
# Napisz funkcję, która na podstawie listy liczb całkowitych jako parametr wejściowy będzie zwracała wartość ze środka listy, jeżeli ich
# liczba będzie nieparzysta lub średnią z dwóch wartości środkowych jeżeli ich liczba jest parzysta. Lista powinna być posortowana
# rosnąco.

def zadanie_6(lista):
    lista.sort()

    if len(lista) % 2 == 0:
        lewa = int(len(lista)/2)-1
        prawa = int(len(lista)/2)
        wynik = (lista[lewa]+lista[prawa])/2
    else:
        wynik = lista[int(len(lista)/2)]

    return wynik


lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5, 6]

print(zadanie_6(lista1))
print(zadanie_6(lista2))
