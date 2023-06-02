import matplotlib.pyplot as plt
# pip install matplotlib
x = [1, 2, 1, 4, 5]
y = [2, 3, 5, 7, 9]

plt.plot(x, y)
plt.title("Wykres liniowy")
plt.xlabel('Os x')
plt.ylabel('Oś y')

plt.show()