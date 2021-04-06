# Zadanie 9
# Przepisz jeden z napisanych przez siebie iteratorów na generator.

def index_parzysty(lista):
    for i in range(0, len(lista), 2):
        yield lista[i]


liczby = index_parzysty([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby))
