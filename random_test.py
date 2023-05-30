import random

# pip list

# random - generowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6 włacznie
print(random.random())  # float 0...0.99999999
print(random.random() * 6)  # float 0..5.9999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # generuje liste od 1 do 49
print(lista2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
# 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
lista3 = []
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)

wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
print(lista3)

# losowanie 6 liczb z lista2 (nie beda sie powtarzac)
print(random.choices(lista2, k=6))

print(lista)
