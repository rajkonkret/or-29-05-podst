# dekorator - funkcja, ktora do istniejca funkcji dodaje nowa funkcjonalnosc

import time


def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sec")

        return result

    return wrapper


@dekor  # dodajemy dekorator @dekor
@measure_time
def hej():
    print("Hej")


@measure_time
def my_function():
    # pass
    time.sleep(2)  # wstrzymanie wykonania programu na 2 sekundy


hej()  # Hej
dekor(hej())  # Hej
# po dodaniu dekoratora @dekor wynik działąnia:
# Dekorujemy
# Hej
# Dekorujemy
# Hej
# Czas wykonania funkcji hej: 0.0 sec
my_function()
# Czas wykonania funkcji my_function: 2.011793375015259 sec