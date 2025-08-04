# Functions
def func():
    print("Geeks for geeks")
func()

def evenOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOdd(10))
print(evenOdd(11))


# Function with parameters
def func1(name):
    print("Hello " + name)
func1("Geeks")

# Function with multiple parameters
def func2(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")
func2("Geeks", 5)

# Function with default parameter
def func3(name, age=20):
    print("Hello " + name + ", you are " + str(age) + " years old.")
func3("Geeks")
func3("Akhil")

def myfunc(x, y=10):
    print("x:", x)
    print("y:", y)
myfunc(5)
myfunc(5,9)

# keyword Arguments
def Student(fname,lname):
    print(fname,lname)
Student(fname="Geeks", lname="Practice")
Student(fname="Practice", lname="Geeks")

# Postional Argumrments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("suraj",32)

print("\nCase-2:")
print(34,"akhil")


# Arbitary keyword Arguments
# *args in Python (Non-Keyword Arguments)
def myFunc(*argv):
    for i in argv:
        print(i)
myFunc("akhil","vishnu","suresh")

# **kwargs in Python (Keyword Arguments)
def myFunc(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key, value))
myFunc(first="geeks", mid="for", last="geeks")


# Docstring
def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

print(evenOdd.__doc__)


# Python Function within Functions
def f1():
    s="i love you!"

    def f2():
        print(s)
    f2()
f1()


# Anonymous Functions
def cube(x): return x*x*x #without lambda

cube1 = lambda x : x*x*x  #with lambda
print(cube(7))
print(cube1(3))


# Return Statement
def square_value(num):
    return num**3
print(square_value(9))
print(square_value(2))


# Pass by Reference and Pass by Value






# Function with return value
def func4(name):
    return "Hello " + name
result = func4("Geeks")
print(result)

# Function with multiple return values
def func5(name, age):
    return "Hello " + name, age
greeting, age = func5("Geeks", 5)
print(greeting)
print("You are " + str(age) + " years old.")


