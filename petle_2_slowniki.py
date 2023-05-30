dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

# {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(dictionary)

# zwraca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# zwraca wartosci
for v in dictionary.values():
    print(v)

for k, v in dictionary.items():
    print(k, "=>", v)

dict1 = {'name': 'imie', 'company': "Orange"}
for k, v in dict1.items():
    print(k, v)
print(dict1)  # {'name': 'imie', 'company': 'Orange'}
# zamiana kluczy z wartosciami w słowniku {'imie': 'name', 'Orange': 'company'}
print({value: key for key, value in dict1.items()})

dict2 = {}
for key, value in dict1.items():
    dict2[value] = key

print(dict2)  # {'imie': 'name', 'Orange': 'company'}
