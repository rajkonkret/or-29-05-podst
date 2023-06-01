# listy składane - list comphrehesion
numbers = [1, 2, 3, 4, 5]

# Tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]
# for num in numbers:
#     jakaslista.append(x ** 2)

# lista licczb parzystych z zadanej listy - filtrowanie
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # [2, 4]
# for num in numbers:
#     if num % 2 == 0:
#         jakaslista.append(num)


# modyfikacja w zależności od warunku
modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(modifed_numbers)  # [1, 4, 3, 8, 5]
# #
# for num in numbers:
#     if num % 2 == 0:
#         jakaslista.append(num * 2)
#     else:
#         jakaslista.append(num)

even_odd = ["parzysta" if x % 2 == 0 else "nieparzysta" for x in numbers]
print(even_odd)  # ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

even_numbers_range = [num for num in range(10) if num % 2 == 0]  # w zakresie 0..9
print(even_numbers_range)  # [0, 2, 4, 6, 8]

squared_numbers = [x ** 2 for x in range(1, 6)]  # 0..5
print(squared_numbers)  # [1, 4, 9, 16, 25]

# abs() - wartości absolutne
numbers2 = [-1, -2, 3, -4, 5]
absolute_values = [abs(x) for x in numbers2]
print(absolute_values)  # [1, 2, 3, 4, 5]

word = "Python"
letters = [letter for letter in word]
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']
