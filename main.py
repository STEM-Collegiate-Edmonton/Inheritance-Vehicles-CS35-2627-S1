from vehicle import Car, Motorcycle


car = Car("Toyota", "Camry", 120, 4)

motorcycle = Motorcycle("Honda", "CBR500R", 160, False)


print("CAR")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Speed: {car.speed} km/h")
print(f"Number of doors: {car.number_of_doors}")

car.move()
car.honk()


print("\nMOTORCYCLE")
print(f"Make: {motorcycle.make}")
print(f"Model: {motorcycle.model}")
print(f"Speed: {motorcycle.speed} km/h")
print(f"Has sidecar: {motorcycle.has_sidecar}")

motorcycle.move()
motorcycle.wheelie()