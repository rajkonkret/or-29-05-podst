user = "Tomek"  # str
wiek = 39  # int
wersja = 3.9000001  # float - zmiennoprzecinkowa
liczba = 134632344532  # int

# %s - str
# %d - liczba calkowita
print("Witaj %s masz teraz %d lat" % (user, wiek))
# ctrl / - komentarz  linijki, lub zaznaczonego bloku
# print("Witaj %s masz teraz %d lat" % (wiek, user)) - nie zadziała - %s oczekuje str  dostaje int (wiek)

print("Witaj %(user)s masz teraz %(age)d lat" % {'user': user, "age": wiek})
print("Witaj {} masz teraz {} lat".format(user, wiek))
print("Witaj {} masz teraz {} lat".format(wiek, user))  # zadziałą ale nie tak jak oczekujemy
print(f"Witaj {user} masz teraz {wiek} lat")  # f - fstring - sformatowany string

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)  # %.1f - jeden znak po przecinku
print("Używamy wersji Python %.2f" % 3.9)  # %.2f - dwa znaki po przecinku
print("Używamy wersji Python %.f" % 3.9)  # %.f - zero znaków po przecinku, ale zaokrągli
# wersja = 3.9000001  # float - zmiennoprzecinkowa
print("Używamy wersji Python {}".format(wersja))

print(f"Używamy wersji {wersja}")  # Używamy wersji 3.9000001
print(f"Używamy wersji {wersja:.1f}")
print(f"Używamy wersji {wersja:.2f}")  # Używamy wersji 3.90

print(f"{user:>10}")  # "     Tomek" - uzepełnia spacje tak aby tekst miał 10 znaków
print(f"{user:>20}")  # "               Tomek" - uzepełnia spacje tak aby tekst miał 20 znaków
print(f"{user:<30}")  # "Tomek                         " - dodał z prawej strony spacje by tekst miał 30 znaków
print(f"{user[0:4]}")  # wyswietla pierwsze 4, od 0 do 3

print(liczba)  # 134632344532
print("Nasza duza liczba {:,}".format(liczba))  # Nasza duza liczba 134,632,344,532
print("Nasza duza liczba {:,}".format(liczba).replace(",", "."))  # Nasza duza liczba 134.632.344.532
print("Nasza duza liczba {:,}".format(liczba).replace(",", " "))  # Nasza duza liczba 134 632 344 532


