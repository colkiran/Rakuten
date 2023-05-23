
"""
Broadcasting
------------
Broadcasting is a powerful mechanism that allows numpy to work
with arrays of different shape when performing arithmetic operations
"""

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(x)
print(x.shape)

print("-" * 40)
v = np.array([1, 0, 1])
print(v)
print(v.shape)

print("-" * 40)
y = np.empty_like(x)
print(y)

# we will add the vector v to each row of the matrix x
# storing the result in the matrix y

# add the vector v to each row of matrix x with a explicit loop
print("-" * 40)

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)

# looping like this for a large array might be expensive

print("-" * 40)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1)) # stack 4 copies of v on top of each other
print(vv)

y = x + vv
print(y)

print("-" * 40)

# Now broadcasting allows us to perform this computation without actually
# creating multiple copies of v
# we will add the vector v to each row of the matrix x,
# storing the result in y

y = x + v
print(y)


'''
Broadcasting two arrays together follows these rules:

If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
The arrays can be broadcast together if they are compatible in all dimensions.
After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension

'''