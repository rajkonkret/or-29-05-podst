# krotka, tupla - niemodyfikalna, niemutowalna
# zmienna niezmienna
tupla = ("Tomek", "Asia", "Marek", "Paulina")  # definiowanie tupli
tupla2 = ("Radek",)  # tupla jedoelementowa - zmienna, niezmienna
tupla3 = (43, 55, 22.42, 11, 200)

print(tupla)  # ('Tomek', 'Asia', 'Marek', 'Paulina')
print(type(tupla))  # <class 'tuple'>
print(tupla2)
print(type(tupla2))  # <class 'tuple'>
print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla.count("Tomek"))  # jeden Tomek
print(tupla.index("Tomek"))  # na pierwszym miejscu, czyli index=0

a, b = 1, 2
print(a)
print(b)
a, b = b, a  # zamiana miejscami
print(a, b)

a, *b = 1, 2, 3  # * - worek na dane, których nie wiesz gdzie podstawic
print("a=", a, "b=", b)  # a= 1 b= [2, 3]

tp = 1, 2, 3
print(tp)
print(type(tp))  # <class 'tuple'>
*a, b = tp
print(a, b)

# rozpakowanie tupli
# ('Tomek', 'Asia', 'Marek', 'Paulina')
*imie1, imie2, imie3 = tupla
print(imie1)  # ['Tomek', 'Asia'] - nasz worek bo *
print(imie2)  # Marek
print(imie3)  # Paulina
# ['Tomek', 'Asia'] - nasz worek bo *
# Marek
# Paulina

lista = list(tupla)  # zamiana tupli na liste
print(lista)  # ['Tomek', 'Asia', 'Marek', 'Paulina']
print(type(lista))  # <class 'list'>
