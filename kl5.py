class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


# klasa Samochod, dziedziczy po klasie Pojazd
class Samochod(Pojazd):
    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


pojazd = Pojazd("Biały")
pojazd.info()

samochod = Samochod("Czerwony", "Tesla")
samochod.info()
