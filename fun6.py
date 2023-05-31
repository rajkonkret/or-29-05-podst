# funkcja do obliczania sredniej

def liczby(*cyfry):
    suma = 0
    print(cyfry)
    print(type(cyfry))
    for cy in cyfry:
        suma += cy
    print(f"Suma: {suma}")
    count = len(cyfry)
    print(f"Liczba ocen: {count}")
    try:
        print(f"Średnia wynosi {suma / count}")
    except Exception as e:
        print("Wystapił bląd", e)


liczby()  # () - tupla  <class 'tuple'>, Wystapił bląd division by zero, program działa nadal
liczby(1)  # (1,)
liczby(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
