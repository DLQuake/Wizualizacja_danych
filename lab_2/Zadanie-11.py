# Zadanie 11
# Napisz skrypt, który rysuje diament. Użytkownikpodaje wysokość nie mniej jak 3 i nie więcej jak 9
# np. wysokość = 3
#  o
# ooo
#  o
# wysokość równa 5
#   o
#  ooo
# ooooo
#  ooo
#   o
# itd.

wysokosc = 0
while(wysokosc < 3 or wysokosc > 9):
    print('!!! wysokość musi być nie mniejsza niż 3 i nie większa od 9 !!!')
    wysokosc = int(input('podaj wysokość: '))
wysokosc_parzysta = False
if(wysokosc % 2 == 0):
    wysokosc_parzysta = True
    wysokosc = wysokosc - 1
###################################
# gora diamentu
#   |
#  \/
spacje = wysokosc // 2
kule = 1
for i in range (0, wysokosc // 2, 1):
    for j in range (0, spacje, 1):
        print(' ',end='')
    spacje = spacje - 1
    for j in range (0, kule, 1):
        print('o',end='')
    kule = kule + 2
    print()
###################################
# srodek diamentu
#   |
#  \/
for i in range (0, wysokosc, 1):
    print('o', end='')
print()
if(wysokosc_parzysta == True):
    for i in range (0, wysokosc, 1):
        print('o', end='')
    print()
###################################
# dol diamentu
#   |
#  \/
spacje = 1
kule = wysokosc - 2
for i in range (0, wysokosc // 2, 1):
    for j in range (0, spacje, 1):
        print(' ',end='')
    spacje = spacje + 1
    for j in range (kule, 0, -1):
        print('o',end='')
    kule = kule - 2
    print()