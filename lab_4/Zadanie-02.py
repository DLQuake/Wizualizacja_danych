# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
import os


plik = open("liczby_podzielne_przez_4.txt", "r")

liczby = plik.readline()

plik.close()

print(liczby)

os.system("pause")
