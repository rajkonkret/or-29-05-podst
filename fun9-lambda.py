# lambda  - skrócona wersja funkcji

odejmij = lambda a, b: a - b

print(odejmij(5, 6))

# jest to dokłądnie to samo co w lambdzie
# def odejmij(a, b):
#     return a - b

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(5))
print(wiek(11))
print(wiek(19))
# print(wiek("19"))  # TypeError: '<' not supported between instances of 'str' and 'int'

lista = [1, 2, 7, 8, 10, 56]
# map() - mapowanie dnych z kolekcji
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 14, 16, 20, 112]

# filter - filtrowanie danych wg warunku w lambdzie
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
# wyfiltrowac większe od 8
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter: [10, 56]
# wieksze od 3, mniejsze od 20
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
# Zastosowanie filter: [7, 8, 10]
