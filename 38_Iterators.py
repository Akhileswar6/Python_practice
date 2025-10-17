# Iterators in Python
# An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time.

# __iter__(): Returns the iterator object itself.
# __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

# Built-in Iterator Example
s = "GFG"
it = iter(s)

print(next(it))
print(next(it))
print(next(it))

# Creating a Custom Iterator

# Define the Class: Start by defining a class that will act as the iterator.
# Initialize Attributes: In the __init__() method of the class, initialize any required attributes that will be used throughout the iteration process.
# Implement __iter__(): This method should return the iterator object itself. This is usually as simple as returning self.
# Implement __next__(): This method should provide the next item in the sequence each time it's called.

class EvenNumbers:
    def __iter__(self):
        self.n = 2  # Start from the first even number
        return self

    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)

# Print the first five even numbers
print(next(it))  
print(next(it)) 
print(next(it))  
print(next(it)) 
print(next(it))


# StopIteration Exception
li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break


# Difference between Iterator and Iterable
# Iterable: list
numbers = [1, 2, 3]

# Iterator: created using iter()
it = iter(numbers)
print(next(it)) 
print(next(it))  
print(next(it))