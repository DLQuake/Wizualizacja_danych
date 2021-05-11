# Zadanie 3 (1 pkt)
# Napisz funkcję, która oblicza pole, obwód oraz długość przekątnej kwadratu dla podanej długości boku x. Wyświetlaj wyniki na ekran.
import math as m


def zadanie_3(x):
    if x > 0:
        pole = x**2
        print("Pole kwadratu o boku "+str(x)+" wynosi "+str(pole))

        obwod = 4*x
        print("Obwod kwadratu o boku "+str(x)+" wynosi "+str(obwod))

        przekatna = x*m.sqrt(2)
        print("Dlugosc przekatnej kwadratu o boku "+str(x)+" wynosi "+str(przekatna))


x = int(input("Podaj dlugosc boku kwadratu: "))
zadanie_3(x)
