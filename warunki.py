odp = True  # prawda do zmienej odp
print(type(odp))  # <class 'bool'>
if odp:  # jeżeli warunek jest True to wykonujemy kod z wciecia
    print("Brawo")

# if sprawdza warunek
# ten warunek musi byc True

odp = 20  # dla pythona to jest True jesli sprawdza w warunku
print(type(odp))
if odp:  # <class 'int'>, zrzutował na bool, wszytko inne niz 0 jest prawda
    print("Brawo2")

czy_znasz_Python = 'n'
if czy_znasz_Python == 't':  # == - przyrównanie a nie wpisanie wartosci do zmiennej
    print("Brawo")
else:
    print("Uczymy się dalej")

print("Program dziala nadal")
