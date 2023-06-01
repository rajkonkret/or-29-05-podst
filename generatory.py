def kwadrat(n):
    for x in range(n):
        print(x ** 2)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonuje dla jednego elementu, zatrzymuje sie i zapamietuje pozycje


kwadrat(5)  # wypisała kwadraty kolejnych liczb 0..4
kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x0000014668F2FED0>
print(next(kwa))  # 0
print(next(kwa))  # 1
print('wypisac cokolwiek')
print('zrobic cokolwiek cokolwiek')
lista = []
lista.append("2344567")
print(next(kwa))  # 4 dla x= 2l
print(next(kwa))
print(next(kwa))


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


def counter2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
c2 = counter2()
print(next(c2))
print(next(c2))
print(c2.send('OK'))
print(next(c2))
print(c2.send('q'))
print(next(c2))