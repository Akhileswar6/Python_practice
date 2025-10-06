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