# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = a x + b

# Funkcja jest rosnąca gdy a>0, malejąca jeżeli a<0, stała gdy a=0 i w zależności od tego będzie wyświetlać odpowiedni komunikat.

def monotonicznoscfunkcji(a,b):
    if a<0:
        return 'jest malejaca'
    elif a==0:
        return 'jest stala'
    else:
        return 'jest rosnaca'


print(monotonicznoscfunkcji(-1,2))
print(monotonicznoscfunkcji(0,5))
print(monotonicznoscfunkcji(2,4))