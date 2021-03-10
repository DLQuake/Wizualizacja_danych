# Zadanie 4
# Napisz skrypt, który pobiera od użytkownika liczbę i wypisuje na ekran wartość bezwzględną tej liczby
a=input("Podaj liczbe: ")
a=int(a)
if a >= 0:
    print("|",a,"| = ",a)
else:
    print("|",a,"| = ",-1*a)