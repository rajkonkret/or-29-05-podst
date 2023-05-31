# klasa
# klasa - szablon
# obiekt - wypełniony szablon

class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = ""

    def powitanie(self):
        print("nazywam się", self.imie)

    def moj_wiek(self):
        print("Nazywam się", self.imie, "Mam", self.wiek, 'lat(a)')


# wyswietlenie dokumentacji klasy
print(Human.__doc__)
# print(print.__doc__)

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x0000023D79BED910>
print(cz1.imie)
cz1.imie = "Radek"
print(cz1.imie)  # Radek
cz1.plec = "k"
print(cz1.plec)  # k
cz1.wiek = 44
print(cz1.wiek)  # 44
print(cz1)  # <__main__.Human object at 0x000001978E90D950>
cz1.powitanie()  # nazywam się Radek
cz2 = Human()
cz2.imie = "Tomek"
cz2.powitanie()  # nazywam się Tomek
cz2.wiek = 55
cz2.moj_wiek()  # Nazywam się Tomek Mam 55 lat(a)
