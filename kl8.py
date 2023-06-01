from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcujna, klasy dziedziczace musza nadpisac tą metode
    def wydaj_odgłos(self):
        pass


class Orzel(Ptak):
    """
    Klasa Orzeł
    """

    def wydaj_odgłos(self):
        print("piiiiiiiii")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Kura(Ptak):
    """
    klasa kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def wydaj_odgłos(self):
        print("kokokokokokokoko")

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


# # gdy klasa ma metode abstrakcyjna, nie mozna stworzyc obiektu tej klasy
# # TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odgłos
# orzel = Ptak("Orzeł", 20)
# orzel.latam()
# orzel.wydaj_odgłos()
#
# kura = Ptak("Kura", 0)
# kura.latam()
# kura.wydaj_odgłos()

or2 = Orzel("orzel", 20)
or2.latam()
or2.wydaj_odgłos()  # piiiiiiiii
or2.poluj()

kura2 = Kura("kura")
kura2.latam()  # Tu kura Ja nie latam
kura2.wydaj_odgłos()  # kokokokokokokoko
kura2.dziobanie()

kura3 = Kura("kura")
kura3.latam()
kura3.dziobanie()
kura3.wydaj_odgłos()
print(kura3.gatunek)
print(kura3.szybkosc)

# Tu kura Ja nie latam
# Tu kura Idę sobie podziobać
# kokokokokokokoko
# kura
# 0