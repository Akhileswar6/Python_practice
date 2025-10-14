# Bisect Algorithm Functions -> The bisect module in Python provides simple and fast (binary search based) functions to search an element in a sorted list.

# • Finding the insertion point (without insertion)
# • Inserting elements at the correct position 

# 1. Finding Insertion Points

# a) bisect.bisect(): Returns the rightmost insertion point for the element. If the element already exists, the insertion point will be after the existing entries.
# syntax -> bisect.bisect(list, num, beg=0, end=len(list))

# b) bisect.bisect_left(): Returns the leftmost insertion point for the element. If the element exists, the insertion point will be before the existing entries.
# syntax -> bisect.bisect_left(list, num, beg=0, end=len(list))

# c) bisect.bisect_right(): Identical to bisect.bisect(), returns the rightmost insertion point.
# syntax -> bisect.bisect_right(list, num, beg=0, end=len(list))

# Example:
import bisect
li = [1, 3, 4, 4, 4, 6, 7] 

print(bisect.bisect(li, 4)) # right
print(bisect.bisect_left(li, 4)) # left
print(bisect.bisect_right(li, 4, 0, 4)) # subright and only works for sublist



# 2. Inserting Elements

# a) bisect.insort(): Inserts the element at the rightmost position. Unlike bisect() functions, this actually modifies the list by inserting the element.
# syntax -> bisect.insort(list, num, beg=0, end=len(list))

# b) bisect.insort_left(): Inserts the element at the leftmost position.
# syntax -> bisect.insort_left(list, num, beg=0, end=len(list))

# c) bisect.insort_right(): Inserts the element at the rightmost position (similar to insort()).
# syntax -> bisect.insort_right(list, num, beg=0, end=len(list))

# Example:
import bisect
l1 = [1, 3, 4, 4, 4, 6, 7]  
l2 = [1, 3, 4, 4, 4, 6, 7]  
l3 = [1, 3, 4, 4, 4, 6, 7]  

bisect.insort(l1, 5) # right
print(l1) 

bisect.insort_left(l2, 5) # left
print(l2)

bisect.insort_right(l3, 5, 0, 4) # subright
print(l3)
