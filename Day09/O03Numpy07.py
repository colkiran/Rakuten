
import numpy as np
# transposing a matrix

x = np.array([[1, 2], [3, 4]])
print(x)

print("-" * 40)
print(x.T)

print("-" * 40)
# Note that taking the transpose of a rank 1 array does nothing
y = np.array([1, 2, 3])
print(y)

print("-" * 40)
print(y.T)
