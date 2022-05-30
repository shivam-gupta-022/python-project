#NumPy program to find the nth element of a specified array.

import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
n=int(input("Enter the position of element you want to print: "))
e1 = x.flat[n-1]
print("Forth e1ement of the array:")
print(e1)
