# Zadanie 8
# Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Wykorzystaj pętle while.
lista=[]
i=0
while i<6:
    liczba=input("Podaj liczbę: ")
    lista.append(int(liczba))
    i+=1
print(lista)