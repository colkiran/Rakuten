
import numpy as np

x = np.array([[1, 2], [3, 4]])

print(x)
print("-" * 40)

print(np.sum(x))

print("-" * 40)
print(np.sum(x, axis=0))        # compute the sum of each col

print("-" * 40)
print(np.sum(x, axis=1))        # compute the sum of each row
