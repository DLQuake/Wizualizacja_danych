# Zadanie 9
# Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. Wynik wyświetla na ekranie. Wykorzystaj pętle while.
liczba=input("Podaj liczbe wielocyfrowa: ")
a=int(liczba)
suma=0
while (a!=0):
    suma=suma+(a%10)
    a=a//10

print("Suma cyfr liczby ",liczba,"wynosi ",suma)