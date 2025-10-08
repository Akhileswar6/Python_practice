# Polymorphism -> "many forms"
# Polymorphism allows same method, function or operator to behave differently depending on object it is working with.

# Types of Polymorphism (Overloading)
# 1. Compile-time Polymorphism -> Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading.

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))


# 2. Runtime Polymorphism (Overriding) -> Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


# Polymorphism in Built-in Functions
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings


# Polymorphism in Functions
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())


# Polymorphism in Operators
print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation