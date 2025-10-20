# Functools module in Python -> The functools module offers a collection of tools that simplify working with functions and callable objects.

# 1. Partial class
# The partial class fix certain arguments of a function and create a new function with fewer parameters.

# Example:
from functools import partial
def power(a, b):
    return a ** b

pow2 = partial(power, b=2) 
pow4 = partial(power, b=4)  
power_of_5 = partial(power, 5) 

print(power(2, 3))    
print(pow2(4))       
print(pow4(3))       
print(power_of_5(2))  

print(pow2.func)     
print(pow2.keywords) 
print(power_of_5.args)


# 2. Partialmethod Class
# Partialmethod works like partial, but for class methods. It allows you to fix some method arguments when defining methods inside classes without making a new method manually.

# Example:
from functools import partialmethod

class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type

    set_red = partialmethod(_color, type='red')
    set_blue = partialmethod(_color, type='blue')
    set_green = partialmethod(_color, type='green')

obj = Demo()
print(obj.color)
obj.set_blue()
print(obj.color)


