tup = ("Geeks", "For", "Geeks", 4, 5)
print(type(tup))

# Converting a list to a tuple
lst= [34,234,"akhil", 45.67, 89]
print(tuple(lst))

# using tuple() constructor
a = tuple([2,3,3,32,21,2])
print(a)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup4 = ('Geeks',) * 3
print(tup4)

# Creating a Tuple with the use of range
tup5 = tuple(range(5))
print(tup5)

# Accessing elements in a Tuple
tup6 = ('Geeks', 'For', 'Geeks', 4, 5)
print(tup6[0])
print(tup6[-1])

# Accessing a range of elements using slicing
print(tup6[1:4])  
print(tup6[:3])
print(tup6[::-1])

# Concatenating two tuples
tup7 = (1, 2, 3)
tup8 = (4, 5, 6)
tup9 = tup7 + tup8
print(tup9)


# Tuple unpacking
tup10 = ("Geeks", "For", "Geeks")
# This line unpack values of Tuple1
a, b, c = tup10
print(a)
print(b)
print(c)

tup11 = (1, 2, 3, 4, 5)
a, *b, c = tup11
print(a) 
print(b) 
print(c)