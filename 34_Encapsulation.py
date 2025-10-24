"""Encapsulation -> hiding internal details of a class and only exposing what’s necessary.
It helps to protect important data from being changed directly and keeps the code secure and organized."""

# Example of Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
emp = Employee("Akhil",45000)
print(emp.name)
# print(emp.__salary)   # accessing private data


# Public Members -> Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules
class Employee:
    def __init__(self, name):
        self.name = name       # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible


# Protected Members -> Protected members are variables or methods that are intended to be accessed only within the class and its subclasses
class employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class subemployee(employee):
    def show_age(self):
        print("Age:",self._age)

emp = subemployee("ashok",32)
print(emp.name)
emp.show_age()


# Private members -> Private members are variables or methods that cannot be accessed directly from outside the class.
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly



"""Declaring Protected and private methods"""
# 1. Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
# 2. Use a double underscore (__) to define a private method accessible only within class due to name mangling.
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally


# Getter and Setter Methods -> In Python, getter and setter methods are used to access and modify private attributes safely

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())