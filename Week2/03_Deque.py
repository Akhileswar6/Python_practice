# A deque stands for Double-Ended Queue
from collections import deque

de = deque(["name","age","DOB"])
print(de)

# Operations on deque 
dq = deque([1,2,3,4,5])
print(dq)

# Adding elements
dq.append(6)                      # add to the right end
print("After append: ",dq)

dq.appendleft(0)                  # add to the left end
print("After appendleft: ",dq)


# Removing elements
dq.pop()                          # remove from the right end
print("After pop: ",dq)

dq.popleft()                      # remove from the left end
print("After popleft: ",dq)

dq.remove(3)                      # remove a specific element
print("After remove: ",dq)


# Adding multiple elements
dq.extend([7,8,9])                # add multiple elements to the right end
print("After extend: ",dq)

dq.extendleft([-1,-2,-3])          # add multiple elements to the left end
print("After extendleft: ",dq)


# Rotating elements
dq.rotate(1)                      # rotates deque n steps to the right 
print("After rotating: ",dq)

dq.rotate(-2)
print("Negative rotating: ",dq)   


# length
print("Length: ",len(dq))


# inserting and removing at specific positions
dq.insert(2,10)
print("After inserting: ",dq)

dq.remove(10)
print("After removing:",dq)


# Accessing elements
print(dq[0])
print(dq[-1])


# Reverse 
dq.reverse()
print("Reverse: ",dq)


# Counting
dq.count(1)
print("Count: ",dq)

# clear
dq.clear()
print("After clear:",dq)

