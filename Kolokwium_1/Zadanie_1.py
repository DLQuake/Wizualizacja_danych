# Zadanie 1 (1 pkt)
# Korzystając z Python comprehensions wygeneruj listę 20 wartości funkcji y = 2x/3 dla x należącego do przedziału <1,20> z krokiem 1.

lista=[(2*x)/3 for x in range(1,21,1)]

print(lista)