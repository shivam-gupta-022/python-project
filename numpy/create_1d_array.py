#NumPy program to create one-dimensional array of single, two and three digit numbers.

import numpy as np  
nums = np.arange(1, 21)
print("One-dimensional array of single digit numbers:") 
print(nums)
nums = np.arange(10, 21)
print("\nOne-dimensional array of two digit numbers:") 
print(nums)
nums = np.arange(100, 201)
print("\nOne-dimensional array of three digit numbers:") 
print(nums)
