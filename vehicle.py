class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def move(self):
        print(f"The {self.make} {self.model} is moving at {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, make, model, speed, number_of_doors):
        super().__init__(make, model, speed)
        self.number_of_doors = number_of_doors

    def move(self):
        print(f"The car {self.make} {self.model} is driving at {self.speed} km/h.")

    def honk(self):
        print("The car honks: Beep beep!")


class Motorcycle(Vehicle):
    def __init__(self, make, model, speed, has_sidecar):
        super().__init__(make, model, speed)
        self.has_sidecar = has_sidecar

    def move(self):
        print(f"The motorcycle {self.make} {self.model} is riding at {self.speed} km/h.")

    def wheelie(self):
        print(f"The {self.make} {self.model} does a wheelie!")