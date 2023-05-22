
import numpy as np

print("Array".center(40, "-"))
array = np.array([1, 2, 3, 4, 5])

print(f"array :{array}")
print(type(array))
print(array.shape)

print("-" * 40)

print("Matrix".center(40, "-"))
array = np.array(([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
print(array)
print(array.shape)

# numpy will use floating points by default
print("zeros".center(40, "-"))
array = np.zeros((3, 4))
print(array)

print("-" * 40)
# all arrays elements are floating points by default
print("ones float".center(40))
array = np.ones((3, 4))
print(array)

print("-" * 40)
# covert the data type
print("Zero_ints".center(40, "-"))
array = np.zeros((3,4), dtype=int)
print(array)

print("-" * 40)
# pass datatypes to control types
print("Ones Ints".center(4))
array = np.ones((3,4), dtype=int)
print(array)

print("-" * 40)
# fill the desired number
print("fill 5".center(40, "-"))
array = np.full((3, 4), 5.5, dtype=int)
print(array)

print("-" * 40)
# fill random numbers
print("fill 5".center(40,"-"))
array = np.random.random((3, 4))
print(array)

# numpy makes a lot of trivial things easy
print("Accessing using index ", array[1, 1])

# magic of numpy
print("All elements above 0.2 ".center(40, "-"))
print(array > 0.2)

print('All elements above 0.2'.center(40, "-"))
# returns a new array with elements matching criteria
print(array[array > 0.2])

# some of the computation functions

print("sum".center(30, "-"))
print(np.sum(array))

print("Floor".center(40, "-"))
print(np.floor(array))

print("Ceil".center(40, "-"))
print(np.ceil(array))

print("round".center(40, "-"))
print(np.round(array))

print("Arithmetic Operations".center(40, '-'))
first = np.array([1, 2, 3])
second = np.array([2, 4, 6])

print(f"sum  :{first + second}")
print(f"diff :{first - second}")
print(f"prod :{first * second}")
print(f"quot :{first / second}")
print(first + 2)

print("-" * 40)
a = np.arange(5)
print(a)
print(a.dtype)
print(a.shape)

