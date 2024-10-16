import numpy as np

# 1. Create a 2D array of zeros
zeros_array = np.zeros((3, 4))
print("Array of Zeros:")
print(zeros_array)

# 2. Create a 2D array of ones
ones_array = np.ones((2, 5))
print("\nArray of Ones:")
print(ones_array)

# 3. Create an array using linspace
linspace_array = np.linspace(0, 1, 5)
print("\nArray Using Linspace:")
print(linspace_array)

# 4. Create a diagonal array
diag_array = np.diag([1, 2, 3])
print("\nDiagonal Array:")
print(diag_array)

# 5. Create an array using logspace
logspace_array = np.logspace(1, 3, 5)
print("\nArray Using Logspace:")
print(logspace_array)
