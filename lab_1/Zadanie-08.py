# Zadanie 8
# Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów
# oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).
print('{:.5}'.format('xylophone')) #1

print('{: d}'.format((- 23))) #2

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data)) #3

print('{:^10}'.format('test')) #4

print('{:_<10}'.format('test')) #5