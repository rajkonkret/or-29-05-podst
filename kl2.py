class Human:
    """
    Dokumentacja
    """

    # konstruktor
    def __init__(self, imie, wiek, wzrost, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def moj_wiek(self):
        print("Nazywam się", self.imie, "Mam", self.wiek, 'lat(a)')

    def moj_wzrost(self):
        print("Nazywam się", self.imie, "Mam", self.wzrost, 'cm wzrostu')

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


cz1 = Human("Radek", "48", "193", "m")
print(cz1)
cz1.powitanie()
cz1.moj_wiek()
cz1.moj_wzrost()
cz1.ruszaj()
cz2 = Human("Mada", "34", "178")
cz2.ruszaj()
cz2.powitanie()
# 15:00