class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    


class Dog(Animal):
    def greeting(self):
        return f"Woof! I am {self.name}, {self.age} years old"


class Cat(Animal):
    def greeting(self):
        return f"Meow! I am {self.name}, {self.age} years old"
    



dog = Dog("Buddy", 3)
cat = Cat("Luna", 2)

print(dog.greeting())
print(cat.greeting())