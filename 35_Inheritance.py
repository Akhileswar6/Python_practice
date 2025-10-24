"""Inheritance -> It allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class).
It promotes code reusability and establishes a hierarchical relationship between classes."""

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name,"barks")

d = Dog("Buddy")
d.info()
d.sound()


# super() Function -> Super function is used to call the parents class methods, In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes.
class Animal:
    def __init__(self,name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)        # call parent constructor
        self.breed = breed

    def details(self):
        print(self.name, " is a", self.breed)

d = Dog("Ruby","Golden Retriever")
d.info()
d.details()


# 1. Single Inheritance -> In single inheritance, a child class inherits from just one parent class.
class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class employee(Person):
    def show_role(self):
        print(self.name, "is an", self.role)

emp = employee("Akhil","SDE")
emp.show_role()

# 2. Multiple Inheritance -> In multiple inheritance, a child class can inherit from more than one parent class.
class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Jennifer", 50000)
emp.details()


# 3. Multilevel Inheritance -> In multilevel inheritance, a class is derived from another derived class (like a chain).
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")



# 4. Hierarchical Inheritance -> In hierarchical inheritance, multiple child classes inherit from the same parent class.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Intern(Person):  
    def role(self):
        print(self.name, "is an intern")

emp = Employee("David")
emp.role()

intern = Intern("Eva")
intern.role()


# 5. Hybrid Inheritance -> Hybrid inheritance is a combination of more than one type of inheritance.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Sophia", "AI Development")
lead.role()
lead.details()