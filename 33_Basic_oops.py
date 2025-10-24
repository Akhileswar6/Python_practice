"""Python class -> Classes are blueprints for creating objects.
A class defines a set of attributes and methods that the created objects (instances) can have."""

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


# Instance vs Class Variable
class student:
    # class variable (shared by all)
    college = "SVCE"

    def __init__(self,name, roll_no):
        # instance variables (unique for each)
        self.name = name
        self.roll_no = roll_no

s1 = student("Jagadeesh",23)
s2 = student("Rahul",76)

print(s1.name, s1.college)
print(s2.name, s2.college)

# Changing instance variable (only for s1)
s1.name = 'Akhil'

# Changing class variable (for all)
student.college = "Sri Venkateswara college of engineering"

print(s1.name, s1.college)
print(s2.name, s2.college)


# Student Example
class student1:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} | Marks: {self.marks}")
    
    def is_pass(self):
        if self.marks>=40:
            print(f"{self.name} is passed")
        else:
            print(f"{self.name} is failed")
        
s1 = student1("Ajay",89)
s2 = student1('Arun', 38)

s1.display()
s1.is_pass()
s2.display()
s2.is_pass()


# Restaurant Order System
class Order:
    tax_rate = 0.05   # 5% tax for all orders

    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
    
    def cal_total(self):
        total = self.price + (self.price * Order.tax_rate)
        print(f"Total for {self.item_name} is ₹{total:.2f}")
    
order1 = Order("Pizza", 300)
order2 = Order("Burger", 150)

order1.cal_total()
order2.cal_total()

    
# Employee Management
class employee:
    company = "Google"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def show_info(self):
        print(f"{self.name} work as {self.position} at {employee.company}")
    
    def raise_salary(self, percent):
        self.salary += self.salary * (percent/100)
        print(f'New salary of {self.name}: {self.salary}')

e1 = employee("vishal","SDE",90000)
e2 = employee("Amit","Intern",20000)

e1.show_info()
e1.raise_salary(3)
e2.show_info()
e2.raise_salary(10)


# Bank Account Management
class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.holder_name} deposited ₹{amount} | New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.holder_name} withdrew ₹{amount} | Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}")

acc1 = BankAccount("Akhileswar", 5000)
acc2 = BankAccount("Rahul", 3000)

acc1.deposit(2000)
acc2.withdraw(1000)
BankAccount.change_bank("Indian Bank")

