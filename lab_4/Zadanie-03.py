# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
import os


lista = ["jabłko", "jajko", "mleko", "chleb", "woda",
         "miód", "szynka", "kiełbasa", "marchewka"]

with open("przykladowe_linijki_tekstu.txt", "w") as plik:
    for text in lista:
        plik.write(str(text)+"\n")


with open("przykladowe_linijki_tekstu.txt", "r") as plik:
    for text in plik:
        print(text, end="")

os.system("pause")
