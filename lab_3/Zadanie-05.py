# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami:
# y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1

def prostopadlerownolegle(a1,b1,a2,b2):
    if a1==a2:
        return 'sa rownolegle'
    elif a1*a2==-1:
        return 'sa prostopadle'
    else:
        return 'nie sa ani rownolegle ani prostopadle'

print(prostopadlerownolegle(2,4,2,5))
print(prostopadlerownolegle(0.5,3,-2,4))
print(prostopadlerownolegle(3,5,5,6))