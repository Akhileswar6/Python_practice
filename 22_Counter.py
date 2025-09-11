from collections import Counter

val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
val1 = ["a","d","g","h","i","i","a"]
ctr = Counter(val1)
print(ctr)

# Creating a Counter
ctr1 = Counter([1,1,3,3,4,6])
ctr2 = Counter({1:2,2:3,3:2})
ctr3 = Counter("hello")
print(ctr1)
print(ctr2)
print(ctr3)

# Accessing Counter Elements
ctr = Counter([1,2,2,3,3,3])
print(ctr[1])
print(ctr[2])
print(ctr[3])
print(ctr[5])

# Updating counters
ctr4 = Counter([2,3,4,5,1,2])
ctr4.update([2,2,3,1])
print(ctr4)

# Counter Methods
# 1.elements()
ctr5 = Counter([1, 9, 2, 3, 3, 3])
items = list(ctr5.elements())
print(items)

# 2.most_common()
ctr6 = Counter([1, 2, 2, 3, 3, 3,3,4,4,4,4,4,4])
common = ctr6.most_common(2)
print(common)

# 3.subtract()
ctr7 = Counter([1, 2, 2, 3, 3, 3])
ctr7.subtract([2,3])
print(ctr7)

# Arithmetic Operations on Counters
ctr8 = Counter([1,2,3,2])
ctr9 = Counter([1,2,3,5])
print(ctr8 + ctr9)
print(ctr8 - ctr9)
print(ctr9 & ctr9)
print(ctr8 | ctr9)