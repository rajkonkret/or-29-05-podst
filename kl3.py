class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year=2000):
        self.model = model
        self.year = year
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10  # p=p+10
        self.__zmien_bieg()

    def licznik(self):
        print("Prędkość wynosi", self.__predkosc, "km/h")

    def hamuj(self):
        self.__predkosc -= 10  # p = p - 10

    # metoda prywatna do uzycia w ramach klasy
    def __zmien_bieg(self):
        print("zmiana biegu")


car1 = Car("Nissan", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# ustawilismy predkosc jako pole prywatne
# print(car1.predkosc)  # AttributeError: 'Car' object has no attribute 'predkosc'
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
