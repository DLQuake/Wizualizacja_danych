# Zadanie 2
# Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla na ekranie (użyj instrukcji readline() i write()).
import sys
print("Podaj 2 liczby:")
liczba1 = int(sys.stdin.readline())
liczba2 = int(sys.stdin.readline())

print("Wynik mnozenia:")
sys.stdout.write(str(liczba1*liczba2))