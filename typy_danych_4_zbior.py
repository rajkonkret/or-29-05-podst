# set - zbior - przechowuje niezduplikowane elementy
# nie pamieta kolejnosci

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana listy na set

print(lista)  # [44, 55, 66, 777, 33, 22, 11, 33, 11]

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # pusty zbior
print(zb2)  # set()
zbior.add(33)
print(zbior)
zbior.add(18)
print(zbior)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 66
print(zbior)  # {777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 777
print(zbior)  # {11, 44, 18, 22, 55}

zbior.remove(55)
print(zbior)  # {11, 44, 18, 22}
zbior.remove(18)
print(zbior)  # {11, 44, 22}

lista2 = list(zbior)  # {11, 44, 22}
print(lista2)  # [11, 44, 22]
print(type(lista2))  # <class 'list'>

zbior2 = {66, 11, 44, 18, 52, 62, 999}
print(zbior2)

print(zbior | zbior2)  # suma zbiorów (or) {66, 999, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # cześć wspolna (and) {11, 44}
print(zbior - zbior2)  # różnica {22}
print(zbior.difference(zbior2))  # {22}

print(zbior2 - zbior)  # różnica {66, 999, 18, 52, 62}
print(zbior2.difference(zbior))  # {66, 999, 18, 52, 62}
