# Zadanie 9
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z procentowym udziałem
# każdego sprzedawcy w ogólnej sumie zamówień. Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego
# wykresu. Przetestuj ten atrybut na wykresie.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/zamowienia.csv', delimiter=';')
grupa=df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})

sprzedawcy=grupa.index.values
zamowienia=[grupa.values[y][0] for y in range(len(grupa.values))]
Explode=[0 for _ in range(len(grupa.index.values))]
Explode[5]=0.1

wedges, texts, autotexts = plt.pie(zamowienia, explode=Explode, shadow=True, labels=sprzedawcy,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))

plt.setp(autotexts, size=14, weight="bold")
plt.title("ilość złożonych zamówień przez poszczególnych sprzedawców")
plt.legend(title='Sprzedawca')
plt.show()
