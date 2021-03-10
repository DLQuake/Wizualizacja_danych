# Zadanie 1
# Korzystając z modułu math wykonaj poniższe działania i wyświetl ich wynik w oknie konsoli.
# e^10
# Pierwiastek 6 stopnia z Ln(5+(sin(8))^2)
# ⌊3.55⌋
# ⌈4.80⌉
import math as m

print("e^10 = ",m.e**10)

i=8 # pi*2/45 = 8
logarytmnaturalny=m.log(5+m.pow(m.sin(m.pi*2/45),2))
print("Pierwiastek 6 stopnia z Ln(",5,"+(sin(",i,"))^2) wynosi ",logarytmnaturalny**(1/6))

print("⌊",3.55,"⌋ = ",m.floor(3.55))

print("⌈",4.80,"⌉ = ",m.ceil(4.80))