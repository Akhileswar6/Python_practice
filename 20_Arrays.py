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

