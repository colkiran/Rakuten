
import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

print("-" * 40)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

print("-" * 40)
m = np.array([np.arange(3), np.arange(3)])
print(m)
print(m.shape)

print("-" * 40)
n = np.arange(7, dtype ='d')
print(n)
print(n.dtype)

print("-" * 40)
t = np.dtype('float64')
print(t.char)
print(t.type)

print("-" * 40)
print("float = ", np.dtype('float'))
print("f=", np.dtype('f'))
print("d=", np.dtype('d'))
print("f8", np.dtype('f8'))
print("f2", np.dtype('f2'))
print("f4", np.dtype('f4'))

print("-" * 40)
print(np.sctypeDict.keys())

print("-" * 40)
# use dtype
my_type = np.dtype(
    [('name', str, 40), ('itemscount', np.int32), ('price', np.float32)])
print(my_type)

items = np.array([('sheela', 4, 400), ('munni', 3, 300)], dtype=my_type)
print(items)
print(items.dtype)

print(items[1][0])
print(items[1]['price'])
it = items[1]
print(it)

print(items[0][0])
