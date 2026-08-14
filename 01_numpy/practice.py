# ==========================================
# NumPy Practice
# ==========================================

import numpy as np

# Q1 - Create arrays
arr = np.arange(10)

# Q2 - Inspect attributes
print(arr.shape, arr.ndim, arr.dtype)

# Q3 - Reshape array
matrix = arr.reshape(2, 5)

# Q4 - Boolean indexing
print(arr[arr > 5])

# Q5 - Element-wise arithmetic
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)

# Q6 - Statistics
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

# Q7 - Broadcasting
matrix = np.arange(12).reshape(3,4)
print(matrix + 10)

# Q8 - Sorting & Argsort
random_array = np.array([7,2,9,1,5])

print(np.sort(random_array))
print(np.argsort(random_array))

# Q9 - Matrix Multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(np.dot(A,B))

# Q10 - Transpose
print(A.T)