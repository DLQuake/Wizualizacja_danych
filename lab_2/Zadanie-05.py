# Zadanie 5
# Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
# czy a zawiera się w przedziale (0,10>
# oraz czy jednocześnie a>b lub b>c.
# Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

liczba1=input("Podaj pierwsza liczbe: ")
liczba1=int(liczba1)

liczba2=input("Podaj druga liczbe: ")
liczba2=int(liczba2)

liczba3=input("Podaj trzecia liczbe: ")
liczba3=int(liczba3)


if liczba1>0 and liczba1<=10:
    if liczba1>liczba2 or liczba2>liczba3:
        print("liczby",liczba1,liczba2,liczba3," Spelniaja wszytkie warunki")
    else:
        print("liczby",liczba1,liczba2,liczba3,"nie pelniaja wszytkich warunkow")
else:
    print("liczby",liczba1,liczba2,liczba3,"nie spelniaja wszytkich warunkow")
