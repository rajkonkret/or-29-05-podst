import math

pi = math.pi
print(pi)  # 3.141592653589793


def pierw(numer):
    pierwiastek = math.sqrt(numer)
    return pierwiastek


print(pierw(25))  # 5.0

a = pierw(25)
a = 4.4
b = int(a)  # tylko czesc całkowita
print(b)
print(round(a))  # zaokraglił w gore do 5
a = int(round(a))
print(a)
print(type(a))  # <class 'int'>
