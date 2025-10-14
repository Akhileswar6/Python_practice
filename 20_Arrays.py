import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(type(a))

# Element wise operations
print(a*2)

# Multi-dimensional array
res = np.array([[1,2],[2,5]])
print(res*2)

arr = np.array([2,4,3,4],dtype=int)
print(arr)
print(arr.dtype)

print(arr[2])

# Append elements to an array
new_arr = np.append(arr,[58,90])
print(new_arr)


arr1 = np.array([1,2,3,4])
for i in range(len(arr1)):
    print(arr[i], end=" ")

arr2 = np.array([1,2,3])
ab = np.insert(arr2,1, 4)
print(ab)


# Operations on Array

# 1. Append() Method
import array
 
# initializing array with array values and signed integers
arr = array.array('i', [1, 2, 3]) 

# printing original array
print ("The new created array is :",end=" ")
for i in range (0, 3):
    print (arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range (len(arr)):
    print (arr[i], end=" ")



# 2. Insert() Method
import array
 
# initializing array with array values and signed integers
arr = array.array('i', [1, 2, 3]) 

# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, 3):
    print (arr[i], end=" ")

arr.insert(2, 5)

print("\r")

# printing array after insertion
print ("The array after insertion is : ", end="")
for i in range (len(arr)):
    print (arr[i], end=" ")



# 3. Pop() Method
import array
 
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print("\r")
 
# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2))
 
# printing array after popping
print ("The array after popping is : ",end="")
for i in range (len(arr)):
    print (arr[i],end=" ")



# 4. Remove() Method
import array
 
arr= array.array('i',[1, 2, 3, 1, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1
arr.remove(1)
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (len(arr)):
    print (arr[i],end=" ")



# 5. Index() Method
import array
  
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
 
print("\r")
 
# using index() to print index of 1st occurrence of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))



# 6. Reverse() Method
import array
  
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
 
print("\r")
 
#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range(len(arr)):
    print (arr[i],end=" ")