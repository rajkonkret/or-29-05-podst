# lista - kolekcja do przechowywania elementów
lista = []  # pusta lista
print(type(lista))  # <class 'list'>
print(lista)  # []
lista.append("Radek")  # dodawanie elementu do listy
print(lista)  # ['Radek']
lista.append("Maciek")
lista.append("Zenek")
lista.append("Jacek")
lista.append("Jacek")
lista.append("Tadek")
lista.append("Jacek")
print(lista)  # ['Radek', 'Maciek', 'Zenek', 'Jacek', 'Jacek', 'Tadek', 'Jacek']
# ideksowana od 0 - czyli pierwszy element ma indeks 0
print(lista[0])  # Radek
print(lista[2])  # Zenek
# print(lista[10])  # IndexError: list index out of range
print(lista[-2])  # Tadek indeks -2,
print(len(lista))  # długosc kolekcji=7 elementów, czyli ostatni ma indeks=6
print(lista[-1])  # Jacek - ostatni element z listy

# ['Radek', 'Maciek', 'Zenek', 'Jacek', 'Jacek', 'Tadek', 'Jacek']
# zastąpienie elementu o podanym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Jacek', 'Jacek', 'Tadek', 'Jacek']

# wstawienie elementu na wskazany indeks
lista.insert(1, "Paweł")
print(lista)  # ['Radek', 'Paweł', 'Maciek', 'Mikołaj', 'Jacek', 'Jacek', 'Tadek', 'Jacek']

# Usunięcie z listy
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Paweł', 'Maciek', 'Jacek', 'Jacek', 'Tadek', 'Jacek']

# useniecie pierwszego napotkanego
lista.remove("Jacek")
print(lista)  # ['Radek', 'Paweł', 'Maciek', 'Jacek', 'Tadek', 'Jacek']

# usuniecie po indeksie
indeks = lista.index("Tadek")
print(indeks)
print(lista.pop(indeks))  # zwraca co usunęło
print(lista)
print(lista.pop(2))  # zwraca co usunęło

# kopiowanie elmentów listy do drugiej
lista_copy = lista.copy()
print(lista_copy)

# usunięcie całej listy
lista.clear()
print(lista)

# tylko kopia adresu pamieci, obie listy wskazuja te same elemnty w pamieci
# obie naraz modyfikowane
print(lista_copy)
lista_copy.append("A")
lista_copy2 = lista_copy
print(lista_copy2)
print(lista_copy)

print("Jacek" in lista_copy2)  # True

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22, 12.34]
liczby[2] = 6666
print(liczby)
print(liczby[0:3])  # od indeksu 0..2
print(liczby[-2])
print(liczby[:-2])  # od do -3 (-2 juz nie wchodzi)
print(liczby[2:])  # od 2 do końca

liczby.remove(34)
print(liczby)
print(len(liczby))  # długosc kolekcji

krotka = tuple(liczby)  # zamiana listy na krotke
print(krotka)  # (999, 687, 6666, 22, 12.34)
print(type(krotka))  # <class 'tuple'>
