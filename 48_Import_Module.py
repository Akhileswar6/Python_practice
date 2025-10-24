"""Import module in Python
In Python, modules help organize code into reusable files.
They allow you to import and use functions, classes and variables from other scripts."""

# Importing built-in Module
import math
pie = math.pi
print("Value of pi:", pie)


"""Importing External Modules
To use external modules, we need to install them first, we can easily install any external module using pip command in the terminal."""

# Example
"""pip install pandas"""

import pandas

# Create a simple DataFrame
data = {
    "Name": ["Elon", "Trevor", "Swastik"],
    "Age": [25, 30, 35]
}

df = pandas.DataFrame(data)
print(df)


# Importing Specific Functions
from math import pi
print(pi)


# Importing Modules with Aliases
import math as m
result = m.sqrt(25)
print("Square root of 25:", result)


# Importing Everything from a Module (*)
from math import *
print(pi)         # Accessing the constant 'pi'
print(factorial(6))  # Using the factorial function


# Handling Import Errors in Python
try:
    import mathematics  # Incorrect module name
    print(mathematics.pi)
except ImportError:
    print("Module not found! Please check the module name or install it if necessary.")
