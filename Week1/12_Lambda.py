s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()
print(s2(s1))


# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))

# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))


li = [lambda arg = x : arg * 10 for x in range(1,6)]
for i in li:
    print(i())


# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))


# Lambda with Multiple Statements
calc = lambda x, y: (x+y,x*y)
print(calc(5, 3))  


# Using lambda with filter()
n = [1,2,3,4,5,6]
even = filter(lambda x : x % 2 == 0, n)
print(list(even))


# Using lambda with map()
a = [1,2,3,4]
b = map(lambda x: x * 2,a)
print(list(b))


# Using lambda with reduce()
from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
