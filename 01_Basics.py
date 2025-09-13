# This script demonstrates formatting a floating-point number to two decimal places.
amount = 150.7524352
print("Amount: ${:.2f}".format(amount))

# Seprating with Comma
print('G', 'F', 'G', sep=',')

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
s = 23        # s → 23 (int object)
m = s         # m → 23 (both point to same int object)
s = 45        # s reassigned to new int object (45), m still points to 23
print(m)      # Output: 23

m = 100       # m reassigned to 100, now nothing refers to 23
print(m)      # Output: 100

print(s)      # Output: 45
