# Decorators - A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello world!")
greet()

# Example
def greet_function(func):
    def wrapper():
        print("Hello!")   # extra step before
        func()
        print("Have a nice day!")   # extra step after
    return wrapper

@greet_function
def say():
    print("I am Akhileswar")
say()



# A higher-order function that takes another function as an argument
def fun(f, x):
    return f(x)

# A simple function to pass
def square(x):
    return x * x

# Using apply_function to apply the square function
res = fun(square, 5)
print(res)



# Types of Decorators
# 1. Function Decorators
# Function decorators are used to modify or enhance the behavior of functions.
def simple_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Thanks for Love!")
    return wrapper

@simple_decorator
def greet():
    print("Welcome to GFG")
greet()


# 2. Class Decorators
# Class decorators are used to modify or enhance classes.
def fun(cls):
    cls.class_name = cls.__name__
    return cls
@fun
class Person:
    print("Class Decorator")
print(Person.class_name)


# 3. Method Decorators
# Method decorators are used to modify the behavior of methods in classes.
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()     


# Common Built-in Decorators in Python
# @staticmethod
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
res = MathOperations.add(4,7)
print(res)


# @classmethod
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)


# @property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Using the property
c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)


# Chaining Decorators
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())