# map()
s = [1,2,3,4]
print(list(map(int,s)))

# Converting map object to a list
a = [1,2,3,4,5,6]
def double(val):
    return val**2
print(list(map(double,a)))

# map() with lambda
a = [8,3,4,2]
print(list(map(lambda x: x*3, a)))

# Using map() with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

# Converting to uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

# Extracting first character from strings
words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)
print(list(res))

# Removing whitespaces from strings
s = ['  hello  ', '  world ', ' python  ']
print(list(map(str.strip,s)))



# filter()
def even(n):
    return n % 2 ==0
a = [1,2,3,4,5,6]
print(list(filter(even, a)))

# Using filter() with lambda
a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, a)))

# Combining filter() with Other Functions
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))



# reduce()
from functools import reduce
def add(x,y):
    return x + y
a = [1, 2, 3, 4]
print(reduce(add, a))

# Using reduce() with lambda
from functools import reduce
a = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, a))

# Using reduce() with operator functions
import functools
import operator
a = [1, 2, 3, 4]
print(functools.reduce(operator.add, a))
print(functools.reduce(operator.mul, a))
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))