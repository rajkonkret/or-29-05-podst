# słownik - klucz, wartosc - {'name':'Radek}

dict = {}  # pusty słownik
print(dict)  # {}
print(type(dict))  # <class 'dict'>

dict['imie'] = "Radek"
print(dict)
dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

print(dict.keys())  # dict_keys(['imie', 'wiek'])
print(dict.values())  # dict_values(['Radek', 39])
print(dict.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({'date': '12-12-2023'})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary = {'x': 2}
print(dictionary)  # {'x': 2}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

dict2 = {'imie': 'name', 'kot': 'cat', 'pies': 'dog'}
dict2.update({'szkło': 'glass'})
print("MAmy w słowniku", dict2.keys())
key = input("Podaj słowko do przetłumaczenia")  # input - wczytuje dane od uzytkownika (str)
print(dict2[key.lower().replace(" ", "")])
