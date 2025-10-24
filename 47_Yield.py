"""Yield keyword is used to create generators, which are special types of iterators that allow values to be produced lazily, one at a time, instead of returning them all at once."""

# Syntax
# def generator_function():
#     yield value


"""Examples of yield"""
# Example 1: Simple Generator to Yield Numbers Sequentially
def fun(m):
    for i in range(m):
        yield i  

# call the generator function
for n in fun(5):
    print(n)

# Example 2: Generator functions and yield
def my_generator():
    yield "Hello world!!"
    yield "GeeksForGeeks"

g = my_generator()
print(type(g))  
print(next(g)) 
print(next(g))

# Example 3: Generating an Infinite Sequence
def infinite_sequence():
    n = 0
    while True:
        yield n
        n += 1

g = infinite_sequence()
for _ in range(10):
    print(next(g), end=" ")


# Example 4: Extracting even numbers from list
def fun(a):
    for n in a:
        if n % 2 == 0:
            yield n

a = [1, 4, 5, 6, 7]
print(list(fun(a)))

# Example 5: Using yield as a boolean expression
def fun(text, keyword):
    w = text.split()
    for n in w:
        if n == keyword:
            yield True

txt = "geeks for geeks"
s = fun(txt, "geeks")
print(sum(s))