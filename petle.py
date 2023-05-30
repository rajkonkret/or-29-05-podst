# petla for
import random

for i in range(10):  # int 0..9
    print(i)  # wciecie obowiązkowe

for i in range(10):
    pass  # nic nie rób

# pass - nic nie rób
# niama zmienna
for _ in range(10):
    pass

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 50))
lista3 = []
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    lista3.append(wyn)

print(lista3)

lista4 = [2, 7, 9, 10, 23, 45]

for cyfra in lista4:
    print(cyfra)

imiona = ["Radek", "Zenek", "Marta"]
print(imiona)

for p in imiona:
    print(p)

# 0 Radek, 1 Zenek

for p in range(len(imiona)):  # range(3)
    print(p, "-", imiona[p])  # p  indeks, imiona[p] - pobranie elementu po indeksie

# enumerate - zwroci indeks i element spod indeksu
for p, w in enumerate(imiona):
    print(p, "-", w)  # p - indeks, w = imiona[p]
# po , (przecinek) automatycznie wyswietla spacje

for p, w in enumerate(imiona):
    print(p, w, sep=":", end="")  # p - indeks, w = imiona[p]
# sep - separator(domyslnie spacja)
# end - znak konca linii (domyslnie \n - new line)

ludzie = ["Radek", "Zenek", "Asia", "Michał"]
wiek = [47, 67, 32, 48]
jezyk = ['java', 'python']

for p, o in enumerate(ludzie):
    print(p, o, wiek[p])

# zip - łaczy listy
for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

for i1, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):  # zwraca dwie wartosi, indeks, i element z kolekcji
    print(i1, o, w, j)

# 0 Radek 47 java
# 1 Zenek 67 python

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
