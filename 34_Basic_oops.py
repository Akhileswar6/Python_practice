# Python class -> Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating Object
class Dog:
    species = "Golden retriver"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
dog1 = Dog("Buddy",2)
print(dog1.name)
print(dog1.age)

# class and instance variables
class Dog:
    # class variable
    species = "Golden retriver"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# access class and instance variables
print(dog1.species)
print(dog1.name)
print(dog2.name)

# modify instance variables
dog1.name = "maxx"
print(dog1.name)

# modify class variable
Dog.species = "Feline"
print(dog1.species)
print(dog2.species)

# Basic Syntax of class and objects
class Car:
    # class Attributes
    brand = "Toyota"
    color = "red"

    # function inside class
    def start(self):
        print("Car has started")

my_car = Car()
print(my_car.brand)
print(my_car.color)
my_car.start()

# Using __init__() — the Constructor
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car in {self.color} color has started")

car1 = Car("Tesla","Red")
car2 = Car("BMW","black")
car1.start()
car2.start()


# Student Class
class Student:
    def __init__(self,name,branch,roll_no,marks):
        self.name = name
        self.branch = branch
        self.roll_no = roll_no
        self.marks = marks

    def details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Branch : {self.branch}")
        print(f"Marks : {self.marks}")

s1 = Student("Akhileswar","CSC",23,86)
s2 = Student("Vinay","CSD",45,87.2)
s1.details()
s2.details()