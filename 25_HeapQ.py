# Heap queue - a priority queue algorithm, that allow to quickly access the smallest (min-heap) or largest (max-heap) element.

import heapq

li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print("Heap queue",li)

# Key operations of a heap
# 1. Push an element onto the heap
heapq.heappush(li,4)
print("After pushing: ",li)

# 2. Pop the smallest element from the heap
smallest = heapq.heappop(li)
print("After popping smallest element: ",li)

# 3. Peek at the smallest element without popping it
smallest_peek = li[0]
print("Smallest element (peek): ", smallest_peek)

# 4. Push multiple elements onto the heap
heapq.heappush(li, 6)
heapq.heappush(li, 2)
print("After pushing multiple elements: ", li)


# 5. Pop the smallest element and push a new element
pop_push = heapq.heapreplace(li, 8)
print("After heapreplace (pop and push): ", li)
print("Popped element during heapreplace: ", pop_push)

# 6. Push and pop in one operation
popped_and_pushed = heapq.heappushpop(li, 10)
print("After heappushpop (popped and pushed): ", li)
print("Popped element during heappushpop: ", popped_and_pushed)

# 7. Find the n smallest or largest elements
n_smallest = heapq.nsmallest(2, li)
n_largest = heapq.nlargest(3, li)
print("3 smallest elements: ", n_smallest)
print("3 largest elements: ", n_largest)

# 8. Merging multiple sorted iterables
iter1 = [1, 3, 5]   
iter2 = [2, 4, 6]
merged = heapq.merge(iter1, iter2)
print("Merged sorted iterables: ", list(merged))

