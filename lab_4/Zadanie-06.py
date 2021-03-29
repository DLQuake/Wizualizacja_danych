# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa:

    def __init__(self, lista):
        self.lista = lista

    def sprawdz_czy_palindrom(self, wyraz):
        for i in range(0, len(wyraz)//2, 1):
            if wyraz[i] != wyraz[-i-1]:
                return False
        return True

    def sprawdz_czy_metagramy(self, wyraz1, wyraz2):
        rozne = 0
        if len(wyraz1) != len(wyraz2):
            return False
        for i in range(0, len(wyraz1), 1):
            if wyraz1[i] != wyraz2[i]:
                rozne += 1
        if rozne == 1:
            return True
        else:
            return False

    def sprawdz_czy_anagramy(self, wyraz1, wyraz2):
        if sorted(wyraz1) == sorted(wyraz2):
            return True
        else:
            return False

    def wyswietl_wyrazy(self):
        for i in range(0, len(self.lista), 1):
            print(self.lista[i], end="; ")


Lista_slow = ['kajak', 'tata', 'mata', 'tama']
obiekt = Slowa(Lista_slow)
print('Lista: ', end=" ")
obiekt.wyswietl_wyrazy()

print("\n--------------------")
print("Palindrom")
print()
for i in obiekt.lista:
    print('Słowo "'+str(i)+'" ', end='')
    if obiekt.sprawdz_czy_palindrom(i) == True:
        print('jest palindromem')
    else:
        print('nie jest palindromem')


print("--------------------")
print("Metagram")
print()
for i in obiekt.lista:
    for j in obiekt.lista:
        print('Słowa: "'+str(i)+'" oraz "'+str(j)+'" ', end='')
        if obiekt.sprawdz_czy_metagramy(i, j) == True:
            print('są metagramami')
        else:
            print('nie są metagramami')


print("--------------------")
print("Anagram")
print()
for i in obiekt.lista:
    for j in obiekt.lista:
        print('Słowa: "'+str(i)+'" oraz "'+str(j)+'" ', end='')
        if obiekt.sprawdz_czy_anagramy(i, j) == True:
            print('są anagramami')
        else:
            print('nie są anagramami')
