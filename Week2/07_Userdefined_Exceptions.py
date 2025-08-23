# User-defined Exceptions in Python with Examples
# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.age} -> {self.msg}"
    
# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to {age}")

# Step 3: Handle the custom exception
try:
    set_age(98)       # This will raise the custom exception
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")



# Customizing Exception Classes
# Step 1: Subclass the Exception class

class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):
        # Custom attributes
        self.age = age
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)  # Call the base class constructor

    # Step 2: Customize the string representation of the exception
    
    def __str__(self):
        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"

# Step 3: Raising the custom exception

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 4: Handling the custom exception with additional information

try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)



# How to use standard Exceptions as a base class?
# NetworkError has base RuntimeError and not Exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)