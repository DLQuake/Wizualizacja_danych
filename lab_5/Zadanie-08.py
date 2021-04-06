# Zadanie 8
# Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego. Zaimplementuj sprawdzanie czy przekazany
# został string jako argument konstruktora tego iteratora (sprawdź funkcję isinstance()).

class Samogłoski:
    def __init__(self, napis):
        if isinstance(napis, str):
            self.napis = napis
            self.indeks = 0
            self.lista_samoglosek = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó',
                                     'u', 'y', 'A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U', 'Y']
        else:
            raise ValueError("Nie przekazano typu string")

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks >= len(self.napis):
            raise StopIteration
        while self.indeks < len(self.napis):
            if self.napis[self.indeks] in self.lista_samoglosek:
                self.indeks += 1
                return self.napis[self.indeks-1]
            self.indeks += 1


ciag_tekstowy = Samogłoski("Zażółć gęślą jaźń")
print(next(ciag_tekstowy))
print(next(ciag_tekstowy))
print(next(ciag_tekstowy))
print(next(ciag_tekstowy))
print(next(ciag_tekstowy))
if next(ciag_tekstowy) == None:
    print("Nie ma juz wiecej samoglosek")
