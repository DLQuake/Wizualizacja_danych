# Zadanie 11
# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.

def ciag_fibonacciego(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        temp = a+b
        a = b
        b = temp


print(list(ciag_fibonacciego(10)))
