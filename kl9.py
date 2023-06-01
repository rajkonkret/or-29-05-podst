# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    klasa C, dziedziczy po A i B
    """

    def method(self):
        # super().method()
        B.method(self)  # jawne wskazanie klasy z której ma sie wykonac metoda


a = A()
a.method()
b = B()
b.method()

c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
