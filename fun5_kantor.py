kurs_euro = 4.5


def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print("Przeliczam dolary", kwota * 4.13)

    def eur(kwota=0):
        print("Przeliczam euro", kwota * kurs_euro)

    if waluta == 'eur':
        return eur
    else:
        return usd


moj_kantor_eur = kantor("eur")
print(moj_kantor_eur)  # <function kantor.<locals>.eur at 0x000002455D647100>
moj_kantor_eur()  # Przeliczam euro
moj_kantor_eur(1000)  # Przeliczam euro 4500.0

moj_kantor_usd = kantor("usd")
moj_kantor_usd()
moj_kantor_usd(1000)  # Przeliczam dolary 4130.0
