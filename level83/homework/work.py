#OOP  არის სადაც ყველაფერი ობიექტებით და კლასებით იქმნება
#Polymorphism ნიშნავს რომ ერთსა და იმავე მეთოდს სხვადასხვა კლასი  სხვადასხვანაირად იყენებს
#public შეგვიზლია გამოვიყენოთ  კლასის გარეთ და ყველგან private კი მხოლოდ გარკვეულ კლასზე სეგვიზლია

class Character:
    def __init__(self, name, power):
        self.name = name              
        self.__power = power         

    # public method
    def show_info(self):
        print(f"Name: {self.name}")

    # public method
    def attack(self):
        print(f"{self.name} attacks!")
