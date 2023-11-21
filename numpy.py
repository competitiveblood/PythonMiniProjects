import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
print()

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr_2d)
print()

# Generating an array with a range
arr_range = np.arange(1, 10, 2)  # Start at 1, end at 10 (exclusive), step by 2
print("Array using arange:")
print(arr_range)
print()

# Reshaping an array
arr_reshaped = arr_range.reshape(2, 2)
print("Reshaped Array:")
print(arr_reshaped)
print()

# Performing operations on arrays
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

# Element-wise addition
arr_add = arr_a + arr_b
print("Element-wise addition:")
print(arr_add)
print()

# Element-wise multiplication
arr_mul = arr_a * arr_b
print("Element-wise multiplication:")
print(arr_mul)
print()

# Basic statistics on arrays
print("Statistics:")
print("Mean:", np.mean(arr_a))
print("Max:", np.max(arr_b))
print("Min:", np.min(arr_a))
print("Sum:", np.sum(arr_b))
