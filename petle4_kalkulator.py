# kalkulator
# menu
# wybor działania przez uzytkownika
# podanie liczb na jakich wykonac działanie
# wyswietlenie wyniku działania

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj odpowiedź")
    if odp == '5':
        break

    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj drugą liczbe"))

    if odp == '1':
        print(f"Wynik dodawnia {a} + {b} = {a + b}")
    elif odp == '2':
        print(f"Wynik odejmowania {a} - {b} = {a - b}")
    elif odp == '3':
        print(f"Wynik mnożenia {a} * {b} = {a * b}")
    elif odp == '4':
        if b != 0:
            print(f"Wynik dzielenia {a} : {b} = {a / b}")
        else:
            print("Nie dziel przez zero")
    else:
        print("Nie znam takiego działania")

# wynik odejmowania 2 - 3 = -1
