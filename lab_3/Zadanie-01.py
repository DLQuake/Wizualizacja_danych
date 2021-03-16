# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A={1/x: x∈<1,10>}
# B={1, 2, 4, 8,…, 2^10}
# C={x: x∈ B i x jest liczbą podzielną przez 4}

A=[1 / x for x in range(1,11,1)]
B=[2 ** i for i in range(11)]
C=[x for x in B if x % 4 == 0]

print(A)
print(B)
print(C)