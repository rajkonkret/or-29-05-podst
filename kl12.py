import pickle

# pickle - ułatwi nam zapisywanie i odczytywanie danych z klas do pliku


lista = [1, 2, 3, 4, 5]

with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', 'r') as f:
    lines = f.read()

print(type(lines))  # <class 'str'>
print(lines)
print(lines[0])  # [
print(lines[1])  # 1

with open('lista_pickle.log', 'wb') as file:
    pickle.dump(lista, file)

with open('lista_pickle.log', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(loaded_list[0])  # 1
print(type(loaded_list))  # <class 'list'>
