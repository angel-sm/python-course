class User:
    # Class attrs
    username = ""
    email = ""

cody = User()

#Dinamic attrs
cody.username = "Cody"
cody.email = "cody@gmail.com"

print(cody.username)
print(cody.email)

# Class methods
class Dog: 
    def initialice(self, name, color):
        self.name = name
        self.color = color

roky = Dog()
print(roky.__dict__)
roky.initialice('Roky', 'Brown')
print(roky.__dict__)

# __init__ method
class Cat: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

garfield = Cat('Garfield', 'Orange')
print(garfield.__dict__)

# Herencia
class Animal: 
    def eat(self):
        print("It's eating")
    
    def sleep(self):
        print("It's spleeping")

class Depretator: 
    def hunt(self):
        print("It's hunting")

# Simple herencia
class Tigger(Animal):
    pass

bigCat = Tigger()
bigCat.sleep()

# Multiple herencia
class Shark(Animal, Depretator):
    pass

bigBlue = Shark()
bigBlue.hunt()

# Class method
class Circle:

    pi = 3.1416

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

myArea = Circle.area(14)
print(myArea)