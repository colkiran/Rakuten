
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.shape)

print(a[[0, 1 , 2], [0, 1, 0]])

print([a[0, 0], a[1, 1], a[2, 0]])

print("-" * 40)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)

print("-" * 40)
b = np.array([0, 2, 0, 1])
print(b)

print(a[np.arange(4), b])

a[np.arange(4), b] += 10

print("-" * 40)
print(a)
