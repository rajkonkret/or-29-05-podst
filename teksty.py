tekst = "Witaj świecie"
print(tekst)

tekst2 = tekst.upper()  # upper() - zamien na duze litery
print(tekst2)
print(tekst)
tekst3 = tekst2.lower()  # zamiana na małe litery
print(tekst3)
print(tekst.upper())  # WITAJ ŚWIECIE
liczba = 39
print(tekst.removeprefix("Witaj"))  # ( świecie)
print(tekst.removesuffix("świecie"))  # (Witaj )
print(tekst)
encoded_s = tekst.encode('utf-8')  # konwersja na typ utf-8
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
tekst_bajtowy = b"To jest tekst bajtowy"
print(tekst_bajtowy)
print(type(tekst_bajtowy))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie
print(tekst.count("i"))  # i wystepuje 3 razy
print(tekst.count("i", 0, 4))  # i wystepuje 1 razy, dotyczy tylko znaków od 0..4
imie = "Radek"
tekst_format = f"Mam\t na imie {imie} \ni lubię \bPytona"
print(tekst_format)
starszy = "Witaj %s!"  # s - oczekuje str
print(starszy % imie)
print("Witaj {}!".format(imie))
print("""
Tekst wielolinijkowy
    druga linia

""")
