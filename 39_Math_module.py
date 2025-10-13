# The math module in Python is a built-in library that contains a collection of mathematical functions and constants. It is commonly used to perform standard math operations such as rounding, trigonometry, logarithms and more, all with precise and reliable results.

# Importing math Module
import math

# Constants in math module

# 1. Euler's Number -> The math.e constant returns the Euler’s number: 2.71828182846.

# Example:
import math
print(f"Euler's number: {math.e}")


# 2. Pi -> You all must be familiar with pi. The pi is depicted as either 22/7 or 3.14. math.pi provides a more precise value for the pi.

# Example - 1
import math 
print(f"Pi: {math.pi}")

# Example - 2
import math 
r = 4
pie = math.pi
print(f"Area of Circle: {pie*r*r}") 


# 3. tau -> Tau is defined as the ratio of the circumference to the radius of a circle. The math.tau constant returns the value tau: 6.283185307179586.

# Example:
import math 
print (f"tau: {math.tau}")


# 4. Infinity

# Example 1: This prints positive and negative infinity.
import math 
print (math.inf) 
print (-math.inf)

# Example 2: This compares infinity with a large number.
import math 
print (math.inf > 10e108) 
print (-math.inf < -10e108)


# Numeric Functions in Math Module

# 1. Finding the ceiling and the floor value
import math 
a = 2.3
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a))


# 2. Finding the factorial of the number
import math
a = 5
print("The factorial of 5 is : ", end="")
print(math.factorial(a))


# 3. Finding the GCD
import math 
a = 15
b = 5
print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(b, a))


# 4. Finding the absolute value
import math 
a = -10
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a))


# Logarithmic and Power Functions

# 1. Finding the power of exp -> exp() method is used to calculate the power of e.
import math 
test_int = 4
test_neg_int = -3
test_float = 0.00
print (math.exp(test_int)) 
print (math.exp(test_neg_int)) 
print (math.exp(test_float))


# 2. Finding the power of a number
print ("The value of 3**4 is : ",end="")
print (pow(3,4))


# 3. Finding the Logarithm
import math 
print ("The value of log 2 with base 3 is : ", end="") 
print (math.log(2,3)) 
print ("The value of log2 of 16 is : ", end="") 
print (math.log2(16)) 
print ("The value of log10 of 10000 is : ", end="") 
print (math.log10(10000))


# 4. Finding the Square root
import math 
print(math.sqrt(0)) 
print(math.sqrt(4)) 
print(math.sqrt(3.5))


# Trigonometric and Angular Functions

# 1. Finding sine, cosine and tangent
import math 
a = math.pi/6
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a))


# 2. Converting values from degrees to radians and vice versa
import math 
a = math.pi/6
b = 30
print ("The converted value from radians to degrees is : ", end="") 
print (math.degrees(a)) 
print ("The converted value from degrees to radians is : ", end="") 
print (math.radians(b))