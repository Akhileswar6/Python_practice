# Python Random module generates random numbers in Python. It introduce randomness into programs.

# Examples of Random Module
# Example 1: Pick a Random Element from a List
import random
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))


# Example 2: Using seed() for Reproducible Output
import random
random.seed(5)
print(random.random())
print(random.random())


# Example 3: Generate Random Integers in a Range
import random
r1 = random.randint(5, 15)
print(r1)

r2 = random.randint(-10, -2)
print(r2)


# Example 4: Generate a Random Float Between 0 and 1
from random import random
print(random())


# Example 5: Randomly Select from List, String, and Tuple
import random

a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))

s = "geeks"
print(random.choice(s))

tup = (1, 2, 3, 4, 5)
print(random.choice(tup))


# Example 6: Select Multiple Unique Random Items
from random import sample

a = [1, 2, 3, 4, 5]
print(sample(a,3))

b = (4, 5, 6, 7, 8)
print(sample(b,3))

c = "45678"
print(sample(c,3))


# Example 7: Shuffle Elements in a List
import random
a = [1, 2, 3, 4, 5]

random.shuffle(a)
print("After shuffle : ")
print(a)

random.shuffle(a)
print("\nSecond shuffle : ")
print(a)