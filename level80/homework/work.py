class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"This car is {self.brand} from {self.year}"


car1 = Car("BMW", 2020)
print(car1.info())

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return "The vehicle is moving"


class Bike(Vehicle):
    def move(self):
        return "The bike is moving fast"


bike1 = Bike("Yamaha", 120)
print(bike1.move())

class Bird:
    def move(self):
        return "Flying"


class Fish:
    def move(self):
        return "Swimming"


bird = Bird()
fish = Fish()

print(bird.move())
print(fish.move())

