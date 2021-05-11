# Zadanie 4 (1 pkt)
# Napisz funkcję, gdzie generowane będą dwie listy 20 elementowe zawierające wartości losowe całkowite z przedziału <1,100> a
# następnie stworzone zostaną dwie nowe listy, z których jedna będzie zawierała liczby <=50 a druga pozostałe. Wyświetl obie listy.

import random


def zadanie_4(lista1,lista2):
    for _ in random(0,20,1):
        liczby1=random.randint(1,100)
        lista1.append(liczby1)

        liczby2=random.randint(1,100)
        lista2.append(liczby2)

    nowa_lista_1=[]
    nowa_lista_2=[]

    for j in lista1,lista2:
        if lista1<=50:
            nowa_lista_1.append(lista1[j])
        elif lista2>50:
            nowa_lista_2.append(lista2[j])

    print(nowa_lista_1)
    print(nowa_lista_2)

list1=[]
list2=[]
zadanie_4(list1,list2)