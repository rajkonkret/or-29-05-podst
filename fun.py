# funkcja

a = 5
b = 8


# definicja funkcji bezargumentowej
def dodaj():
    print(a + b)


# funkcja z dwoma argumentami a i b
# przy wywołaniu obowiązkowo oba muszą zostac podane
def dodaj2(a, b):
    print(a + b)


# funkcja trzyargumentowa a, b, c
# c domyslnie jest 0, wiec nie musi byc zawsze podany
def odejmij(a, b, c=0):
    print(a + b - c)


# wywołanie funkcji
dodaj()  # 13
b = 7
dodaj()
dodaj2(8, 9)  # dwa argumenty
odejmij(1, 2, 3)  # 0
odejmij(5, 7)  # 12

# podanie argumentów po nazwie
odejmij(b=6, a=9, c=8)

print(dodaj())  # None
