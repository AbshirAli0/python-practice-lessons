#small challenge
import math

class Shape:
    def area(self):
        raise Exception("Incorrect values")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Rectangle(4,5), Circle(3)]

for shape in shapes:
    print("Area: ", shape.area())


#Homework

#part 1 - Short Answer
# What is a class and how does it relate to an object?
# a class is considered as the blueprint for creating new objects and contains both the attributes and methods that the objects will possess. its relation to an object is that an object is an instance of class.

#Explain the purpose of the __init__ method. When is it called?
# The init method is a constructor method and is used to set up the initial state of the object by assigning its values and attributes. its called automatically when a new object of a class is created.

#What does the self keyword represent inside a class?
# the self keyword represents the specific object that is created from a class and it allows us to access and manipulate its attrubtes and methods that bekong to that object

# What is the difference between a class attribute and an instance attribute?
# a class attribute is a value that is shared accross all objects while an instance attribute are attributes that are unique to the specific obkect

# Define inheritance and explain one advantage of using it.
# its a concept that allows a new class (child class) to take in attributes and methods from an exisiting class (parent class). an advantage of inheritance is that it makes more reusable due to a reduction of code duplication by allowed th echild class to inherit reuable code from the exisiting class. Class attributes are defined outside of any instance method, while instance are ususally found inside init

# Define polymorphism and give an example from real life.
# a concept that allows objects of different types to be treated as objects of a common superclass. through polymorphism, objects can take on different forms which would enable a single method to behave differently depending on the object being used. an examples could be a method called body_type() where certain cars like a sedan and suv are designed differently. This difference can be met when calling car.body_type() on the specific shape object to modify its behavior

# What does it mean to override a method in a subclass?

# its another concept within inheritance when the child class contains the same method as the parent class, causing it to override the earlier method to use the latest version and its own behaviors 

# What is the role of the super() function in Python classes?
# the super() function is one that allows the child class to access and call methods from the parent class, which makes code more reusable and allows method to extend beyond superclass.

#Part 2 - Coding Practice
# task 1 & 2 - Create a Simple Class and add Behavior

class Book:
    def __init__(self, title, author, pages, checked_out = False):
        self.title = title
        self.author = author
        self.pages = pages
        self.checked_out = checked_out
    
    def book_info(self):
        print(f"{self.title} by {self.author} has {self.pages} ")
    
    def check_out(self):
        self.checked_out = True
        print("It has been checked out.")

    def return_book(self):
        self.checked_out = False
        print("It's available now.")

    def status(self):
        if self.checked_out:
            print("checked out")
        else:
            print("avaialble")


book1 = Book("Harry Potter", "J.K Rowling", 350)
book1.book_info()
book1.status()
book1.check_out()
book1.status()
book1.return_book()
book1.status()

#task 3 and 4: inheritance & Polymorphism

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def descibe(self):
        print(f"This is a {self.brand} {self.model}")
    
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def descibe(self):
        print(f"This is a {self.brand} {self.model} with {self.doors} doors.")
    
class Motorcycle(Vehicle):
    def __init__(self,brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc
    
    def descibe(self):
        print(f"This is a {self.brand} {self.model} with {self.cc} cc engine.")



car1 = Car("Honda", "Civic", 4)
bike1 = Motorcycle("Yamaha", "R1", 1000)

def show_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.descibe()
    


car1.descibe()
bike1.descibe()
show_vehicle_info([car1, bike1])

#Part 3 - OOP Simulation - Pet Adoption Center


class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def speak(self):
        print("...")
    
    def info(self):
        print(f"Name: {self.name} Age: {self.age}, Species: {self.species} ")

class Dog(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
    
    def speak(self):
        print("woof")

class Cat(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
    
    def speak(self):
        print("Meow")


class Bird(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
    
    def speak(self):
        print("Chirp")

class AdoptionCenter:
    def __init__(self, pets):
        self.pets = pets

    def add_pet(self, pet):
        self.pets.append(pet)
    
    def show_pets(self):
        for pet in self.pets:
            print(f"Name: {pet.name}, Age: {pet.age}, Species: {pet.species}")
            pet.speak()
    
    def adopt(self, name):
        for pet in self.pets:
            if pet.name == name:
                self.pets.remove(pet)
                print(f"Congratulations! You adopted {pet.name}")

    
    
center = AdoptionCenter([])

dog1 = Dog("Buddy", 3,"Dog")
cat1 = Cat("Whiskers", 2, "Cat")
bird1 = Bird("Tweety", 1, "Bird")


center.add_pet(dog1)
center.add_pet(cat1)
center.add_pet(bird1)

center.show_pets()

center.adopt("Whiskers")
center.show_pets()


