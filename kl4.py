class Dom:
    """
    To jest kalsa Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def podaj_kolor(self):
        print("Kolor domu to", self.__kolor)

    def podaj_okna(self):
        print("Liczba okien", self.__liczba_okien)

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz"))
        self.__metraz = wybor
        print("Metraż teraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.__kolor = wybor
        print("Kolor mamy", self.__kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        print("Liczba okien wynosi", self.__liczba_okien)

    def __farba(self):
        print("Skończyła sie farba")


dom1 = Dom(175, "czerwony", 8)
dom1.podaj_kolor()
dom1.podaj_metraz()
dom1.zmien_metraz()
dom1.zmien_kolor()
dom1.podaj_metraz()