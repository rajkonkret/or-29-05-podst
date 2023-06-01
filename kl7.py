class Animal:

    # konstruktor
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        pass  # nic nie rob

    def info(self):
        print(f"Imię: {self.imie}")


class Dog(Animal):

    def __init__(self, imie, rasa):
        super().__init__(imie)
        self.rasa = rasa

    def daj_glos(self):
        print("hau hau!")

    def info(self):
        super().info()
        print(f'Rasa:  {self.rasa}')


class Cat(Animal):
    def __init__(self, imie, kolor):
        super().__init__(imie)
        self.kolor = kolor

    def daj_glos(self):
        print("Miau Miau!")

    def info(self):
        super().info()
        print(f'Kolor:  {self.kolor}')


class Tiger(Cat):
    def __init__(self, imie, kolor, liczba_paskow):
        super().__init__(imie, kolor)
        self.liczba_paskow = liczba_paskow

    def daj_glos(self):
        print("Arr Arr!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


zwierze = Animal("Bezimienny")
zwierze.info()
zwierze.daj_glos()  # jest pass, nic sie nie dzieje

pies = Dog("Burek", "Kundel")
pies.info()  # Rasa:  Kundel
pies.daj_glos()  # hau hau!

kot = Cat("Filemon", "Szary")
kot.info()  # Kolor:  Szary
kot.daj_glos()  # Miau Miau!

tygrys = Tiger("Rajah", "Pomarańćzowy", 15)
tygrys.info()  # Liczba pasków: 15
tygrys.daj_glos()  # Arr Arr!
