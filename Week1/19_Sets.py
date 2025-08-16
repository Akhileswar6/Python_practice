# initializing empty set
s1 = set()

set1 = {1, 2, 3, 4}
print(set1)

# Using the set() function
set2 = set("GeeksForGeeks")
print(set2)

# Creating a Set with the use of a List
set3 = set(["Geeks", "For", "Geeks"])
print(set3)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))


# Unordered, Unindexed and Mutability
sets = {1, 2, 3, 4, 5}
print(sets)
try:
    print(sets[1])
except TypeError as e:
    print('Error', e)


# Adding Elements to a Set in Python
set4 = {3,4,5,6,7,8,9}
set4.add(10)

set4.update([11,"abcd"])
print(set4)


# Accessing a Set in Python
set5= {1, 2, 3, 4, 5}
for i in set5:
    print(i,end=" ")

# Removing Elements from a Set
set6 = {1, 2, 3, 4, 5}
set6.remove(3) 
print(set6)

# Discarding Elements from a Set
set7 = {1, 2, 3, 4, 5}
set7.discard(3)
print(set7)

# Popping Elements from a Set
set8 = {1, 2, 3, 4, 5}
popped_element = set8.pop()
print("Popped Element:", popped_element)
print("Set after popping an element:", set8)

# Clearing a Set
set9 = {1, 2, 3, 4, 5}
set9.clear()
print("Set after clearing:", set9)

# Frozen Sets
fset = frozenset([1,2,3,4,5,6,8])
print(fset)

s = {2,3,4,5,6}
print(frozenset(s))

