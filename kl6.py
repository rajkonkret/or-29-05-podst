class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensje = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_wynagrodzenie(self):
        return self.pensje


class Menadzer(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_wynagrodzenie(self):
        return self.pensje + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wynagrodzenie_pracownika = pracownik.oblicz_wynagrodzenie()
print(f"Wynagrodzenie dla {pracownik.imie} {pracownik.nazwisko}: {wynagrodzenie_pracownika} zł")

menadzer = Menadzer("Anna", "Nowak", 8000, 2500)
menadzer.przedstaw_sie()
wynagrodzenie_menadzera = menadzer.oblicz_wynagrodzenie()
print(f"Wynagrodzenie dla {menadzer.imie} {menadzer.nazwisko}: {wynagrodzenie_menadzera} zł")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla Jan Kowalski: 5000 zł
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla Anna Nowak: 10500 zł
# Wynagrodzenie dla Anna Nowak: 10500 zł
# Wynagrodzenie dla Anna Nowak: 10500 zł
# ctl d - kopiowanie linii
# ctrl shift strzałeczki gora/dól - zamienianie kolejnosci linijek

