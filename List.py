a = [10, 20, "GfG", 40, True]
print(a)
print(type(a))
print(type(a[2]))
print(type(a[4]))

print(a[0])
print(a[-1])
print(a[1:4])
print(a[::-1])


# From a tuple
b = list((1, 2, 3, 'apple', 4.5))  
print(b)


# Creating a list with a range
c = list(range(12))
print(c)


# Creaing list with repeated elements
d = [12] * 5
print(d)


# List comprehension
e = [x**2 for x in range(10)]
print(e)


# Adding Elements into List
lst = []
print("Initial list:", lst)

lst.append(23)
lst.append("GfG")
print("After appending elements:", lst)

lst.insert(1, 45)
print("After inserting an element:", lst)

lst.extend([56, "python"])
print("After extending the list:", lst)


# Updating Elements into List
lst1 = [1, 2, 3, 4, 5]
print("Initial list:", lst1)
lst1[3] = 12
print("After updating an element:", lst1)


# Removing Elements from List
lst2 = [10, 20, 30, 40, 50]

lst2.remove(30)  
print("After remove(30):", lst2)

popped_val = lst2.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", lst2) 

del lst2[0]  
print("After del a[0]:", lst2)


# Python List Operations
lst3 = [1, 2, 3, 4, 5]
print("Initial list:", lst3)
print("Length of list:", len(lst3))
print("Maximum element:", max(lst3))
print("Minimum element:", min(lst3))
print("Sum of elements:", sum(lst3))
print("Index of element 3:", lst3.index(3))
print("Count of element 2:", lst3.count(2))


# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
