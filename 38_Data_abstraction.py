# Data Abstraction -> Python abstraction is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

# Abstract Base class
from abc import ABC, abstractmethod

class Greet(ABC):            # abstract class
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())


# Abstractmethod
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass                    # Abstract method, no implementation here



# Concrete method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass                   # Abstract method, no implementation here

    def move(self):
        return "Mving"         # Concrete method with implementation
    
    

# Abstract Properties
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)