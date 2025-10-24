"""A generator function is a special type of function that returns an iterator object.
Instead of using return to send back a single value, generator functions use yield to produce a series of results over time."""

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)


# Creating Generators -> Creating a generator in Python is as simple as defining a function with at least one yield statement.
def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)


# Yield vs Return
def fun():
    return 1 + 2 + 3

res = fun()
print(res)


# Generator Expression -> Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)

