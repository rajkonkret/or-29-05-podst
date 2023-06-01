class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Jadę pojazdem")


class Car(Vehicle):
    def drive(self):
        print("Jadę samochodem")


class Bike(Vehicle):

    def drive(self):
        print("Jadę rowerem")


class HybridCar(Car, Bike):

    def drive(self):
        # super().drive()
        # Bike.drive(self)
        print("Jade samochodem hybrydowym")


car1 = Car("Toyota")
car1.drive()

rower = Bike("Giant")
rower.drive()

hyb = HybridCar("Honda")
hyb.drive()
