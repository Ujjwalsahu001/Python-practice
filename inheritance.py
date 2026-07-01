'''
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand                   #store the brand name in aninstance variable
        self.year = year                     #store the vehicle de=tails as 

    def display_info(self):
        return f"{self.brand} ({self.year})"
    

class Car(Vehicle):

    pass
# create a new object (instances) of the class car
# then automatically calls the __init__ method inherited from the Vehicle

my_car = Car("Verna", 2026)

# calling the display info method inherited from the vehicle class
print(my_car.display_info())
'''

class Animal:

    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def display_info(self):
        return f"{self.name} {self.sound}"
    

class Dog(Animal):
    pass

my_dog = Dog("Jojo","barking")

print(my_dog.display_info())
