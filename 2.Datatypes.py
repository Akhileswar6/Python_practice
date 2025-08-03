# Numeric - int, float, complex
# Sequence Type - string, list, tuple
# Mapping Type - dict
# Boolean - bool
# Set Type - set, frozenset
# Binary Types - bytes, bytearray, memoryview """

# 1. Numeric Datatypes
a = 10
b = 10.5
c = 1 + 2j

print(type(a)) 
print(type(b))
print(type(c))

# 2. Sequence Datatype

# String - immutable
str = 'Welcome to the Geeks World'
print(type(str))

str1 = """This is a multi-line string.
It can span multiple lines."""
print(str1)

# list - mutable
lst = ["Geeks", "For", "Geeks", 4, 5]
print(type(lst))

# tuple - immutable
tup = ("Geeks", "For", "Geeks", 4, 5)
print(type(tup))

# 3. Mapping Datatype

# Dictionary - mutable, unordered collection of key-value pairs
dict_var = {"name": "Geeks", "age": 5}
print(type(dict_var))


# 4.Boolean Datatype
bool_var = True
print(type(bool_var))
print(int(bool_var))  # Converts True to 1 and False to 0

# 5. Set Datatype

# Set - mutable, unordered collection of unique items
set_var = {1, 2, 3, 4, 5}
print(type(set_var))