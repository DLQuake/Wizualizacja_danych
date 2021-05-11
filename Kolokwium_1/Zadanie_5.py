# Zadanie 5 (1 pkt)
# Napisz funkcję, która losuje 5 liczb całkowitych z przedziału <1, 20> dopóki w jednym losowaniu nie wystąpi 1 i 20. Wyświetl ilość
# wykonanych losowań po spełnieniu warunku.

import random

def zadanie_5():
    ilosc_powtorzen=0
    for _ in range(0,5,1):
        liczby=random.randint(1,20)

    while liczby == 1 and liczby == 20:
        print(liczby)
        ilosc_powtorzen+=1
    print("Wykonano "+str(ilosc_powtorzen)+" powtorzen")


zadanie_5()