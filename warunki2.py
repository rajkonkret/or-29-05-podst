lista = []

lang = input("Wpisz znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # domyslny
        print("Nie znam takiego języka")

print(lista)