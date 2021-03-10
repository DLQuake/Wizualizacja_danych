# Zadanie 10
# Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży ale nie więcej jak 10.
# A
# AA
# AAA
# AAAA
# AAAAA
# AAAAAA

import sys
for i in range(0, 6, 1):
    for j in range(0, i+1, 1):
        sys.stdout.write('A')
    sys.stdout.write('\n')