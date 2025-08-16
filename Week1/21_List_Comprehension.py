a = [2,3,45,5]
res = [val ** 2 for val in a]
print(res)

# Using a for loop
b = [2,3,5,6,7]
res = []
for i in b:
    res.append(i*3)
print(res)

# Conditional Statements in List Comprehension
c = [1,2,3,4,5,5]
res = [val for val in c if val%2==0 ]
print(res)

# Creating a list from a range
lst = [i for i in range(11)]
print(lst)

# Using nested loops
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

# Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)



set1 = {0, 2, 4, 6, 8}; 
set2 = {1, 2, 3, 4, 5}; 

print(set1 - set2)