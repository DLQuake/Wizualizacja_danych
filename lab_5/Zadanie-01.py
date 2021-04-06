# Zadanie 1
# Stwórz 3 klasy: Material, Ubrania, Sweter. Klasa: Material

# Atrybuty:

# rodzaj,
# długość
# szerokość
# Metody:

# konstruktor
# wyświetl_nazwę
# Klasa: Ubrania

# Atrybuty:

# rozmiar
# kolor
# dla_kogo
# Metody:

# wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter

# Atrybuty:

# rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:

# wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.

class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print("Rodzaj materialu: "+str(self.rodzaj))
        print("Dlugosc materialu: "+str(self.dlugosc))
        print("Szerokosc materialu: "+str(self.szerokosc))


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyświetl_dane(self):
        print("Rozmiar ubrania: "+str(self.rozmiar))
        print("Kolor ubrania: "+str(self.kolor))
        print("Dla kogo jest to ubranie: "+str(self.dla_kogo))


class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyświetl_dane(self):
        print("Rodzaj swetra: "+str(self.rodzaj_swetra))


bawelna = Material('bawelna', 1, 1)
jedwab = Material('jedwab', 0.5, 0.5)
welna = Material('welna', 5, 5)
bawelna.wyswietl_nazwe()
print()
jedwab.wyswietl_nazwe()
print()
welna.wyswietl_nazwe()
print()
ubranie = Ubrania('XL', 'czarny', 'Jan Kowalski')
ubranie.wyświetl_dane()
print()
sweter = Sweter('Rozpinany')
sweter.wyświetl_dane()
