
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))
print("-" * 40)

print(x)
print(v)

# produced a rank 1 array as a result
print(x.dot(v))
print(np.dot(x, v))

print("-" * 40)
print(x)
print()
print(y)

# produced a rank 2 array as a result
print(x.dot(y))

print("-" * 40)
a = np.array([[2, 2], [3, 3]])
b = np.array([[4, 4], [5, 5]])

print(a)
print()
print(b)

print(a.dot(b))
