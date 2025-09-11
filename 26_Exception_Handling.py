# Handling a Simple Exception in Python
n = 10
try:
    res = n/0
except ZeroDivisionError:
    print("Can't be divided by zero!")


# By using exception as e
n = 12
try:
    s = n/0
except ZeroDivisionError as e:
    print("msg: ",e)


# Difference Between Exception and Error

# Syntax Error (Error)
# print("Hello world"   Missing closing parenthesis

ZeroDivisionError (Exception)
n = 10
res = n / 0


# Syntax and Usage
# try:
    # Code that might raise an exception
# except SomeException:
    # Code to handle the exception
# else:
    # Code to run if no exception occurs
# finally:
    # Code to run regardless of whether an exception occurs



# try, except, else and finally Blocks
try:
    n = int(input("Enter a number: "))
    res = 100 / n
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Enter a valid number!")
else:
    print("Result is: ",res)
finally:
    print('Execution completed.')


# Python Catching Exceptions
try:
    x = int(input("Enter something: "))       # This will cause ValueError
    inv = 1/x
except ValueError:
    print("Not valid!")
else:
    print("Result: ",inv)


# Catching Multiple Exceptions
a = ["10","Twenty",30]
try:
    total = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error: ",e)
except IndexError:
    print("Index out of range.")



# Catch-All Handlers and Their Risks
try:
    res = "100" / 20
except ArithmeticError as e:
    print("Error: ",e)
except:
    print("Something went Wrong!")

# Raise an Exception
# raise ExceptionType("Error message")
def set(age):
    if age < 0:
        raise ValueError("Age Can't be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)