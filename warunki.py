# odp = True  # prawda do zmienej odp
# print(type(odp))  # <class 'bool'>
# if odp:  # jeżeli warunek jest True to wykonujemy kod z wciecia
#     print("Brawo")
#
# # if sprawdza warunek
# # ten warunek musi byc True
#
# odp = 20  # dla pythona to jest True jesli sprawdza w warunku
# print(type(odp))
# if odp:  # <class 'int'>, zrzutował na bool, wszytko inne niz 0 jest prawda
#     print("Brawo2")
#
# czy_znasz_Python = 'n'
# if czy_znasz_Python == 't':  # == - przyrównanie a nie wpisanie wartosci do zmiennej
#     print("Brawo")
# else:
#     print("Uczymy się dalej")
#
# print("Program dziala nadal")
# # 11:30
#
# # hackerrank
#
# podatek = 0.0  # float - w tym niekonieczne
# zarobki = int(input("Dochód"))  # pobieramy odpowiedz uzytkownika, input zawsze zwraca str
# # jezeli dokonac obliczania na danych od uzytkownika to nalezałoby zamienic na liczby ( int lub float)
# if zarobki < 10000:
#     podatek = 0.0  # warunek do 9999
# elif zarobki < 30001:
#     podatek = 0.2  # warunek od 10000 do 30000
# elif zarobki < 100000:
#     podatek = 0.4  # warunek od 30001 do 99999
#
# else:  # inne
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek}zł")
#
# suma_zam = 150
# if suma_zam > 100:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print(f"Rabacik {rabacik}")
#
# rabat = 25 if suma_zam > 100 else 0
# print(f"Rabacik {rabat}")
# # komentarz ctrl /

lista_bledow = []
alert_system = 'console'
error = 'medium'
error_mesage = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_mesage)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)
# test z historii
# wyswietlenie pytania, odpowieddz uzytkownik i sprawdzenie czy prawidłowa
odp = input("Podaj date Chrztu Polski")  # str
if odp == "966":
    print("Prawidłowa odpowiedź")
else:
    print("Masz w ksiazce na stronie 23 ;)")

for i in range(10):
    if i % 2 == 0:  # reszta z dzielenia
        print(i, "jest parzysta")

lista2 = [j for j in range(10) if j % 2 == 0]
print(lista2)
# [0, 2, 4, 6, 8]

for c in lista2:
    if c == 2:
        c += 1
    print(c)