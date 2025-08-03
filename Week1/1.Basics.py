# This script demonstrates formatting a floating-point number to two decimal places.
amount = 150.7524352
print("Amount: ${:.2f}".format(amount))

# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# Using sep to separate strings with a custom separator
print('Akhil', 'geeksforgeeks', 'Shalini', sep='@')

# This script demonstrates various ways to format strings and numbers in Python.
num = 55
add = num + 5
print("The sum is %d" %add)

# Assigning multiple variables in one line
a = b = c = 100
print(a, b, c)

# Assigning multiple variables with different types
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Using f-string for formatting
name = "Akhil"
age = 21    
print(f"My name is {name} and I am {age} years old.")

# using garbage collection
s = 23
m = s
s = 45
# The variable 'm' still holds the value 23, demonstrating that 's' was reassigned.
print(m)
# If we assgin value to m, it will not change the value of s
m = 100
print(m) # Now 23 is eligible for garbage collection
print(s)

print(10%3)