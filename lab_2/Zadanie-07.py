# Zadanie 7
# Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.
lista=[]
for x in range(1,11,1):
    liczba=int(input("Podaj "+str(x)+" liczbe: "))
    lista.append(liczba)
for x in lista:
    print(str(x**2) + " ")