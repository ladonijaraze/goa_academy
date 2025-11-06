#1
def two_sort(strings):
    first = sorted(strings)[0]
    return '***'.join(first)
#2
class Person:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def __str__(self):
        return f"{self.name} {self.father_name} {self.surname}"

p = Person("გიორგი", "ბერიძე", "კახას ძე")
print(p)  
#3
class Cat:
    def meow(self):
        return "მე ვკნავი: მიააუუ!"
class Dog(Cat):  
    def bark(self):
        return "მე ვყეფ: ვაფფ!"
cat = Cat()
dog = Dog()

print(cat.meow())  
print(dog.bark())  
print(dog.meow())  