# while  - petla bez licznika
# sterowana jest warunkiem

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat")
    if licznik > 10:
        break  # przerwij bieżącą pętle

print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("Komunikat")
    licznik += 1

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbe")  # input zwraca zawsze str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['5', '6', '7', '8', '12', '3']
print(lista2)  # [5, 6, 7, 8, 12, 3]
