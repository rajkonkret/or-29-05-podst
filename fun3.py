# zastosowanie global

a = 10
b = 10


def dodaj():
    a = 6  # nadpisujemy w ramach funkcji zmienna a i b
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # uzywamy globalne a czyli zmieniamy wartosc zmiennej globalnej
    a = 6
    b = 7
    print(a + b)


print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj()  # 13
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj2()  # 20
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj3()  # 13
print("Zmienna a z góry", a)  # Zmienna a z góry 6
print(a + b)  # 16
