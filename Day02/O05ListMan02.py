
# count, clear, index

l1 = [1, 2, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("count".center(40, "-"))
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(40, "-"))
print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3)+1))
print("3 :", l1.index(3, l1.index(3, l1.index(3)+1)+1))

print("clear".center(40,"-"))
l1.clear()
print(f"l1 :{l1}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy
l2 = l1                  # shallow copy - copies the address along with the data
print(f"l2 before :{l2}")
l2.extend([6, 7, 8, 9])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 40)
l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")

l4 = l3.copy()                  # deep copy - only data is copied
print(f"l4 before :{l4}")
l4.insert(1, 15)
l4.insert(3, 25)
l4.insert(5, 35)

print(f'l4 after :{l4}')
print(f"l3 after :{l3}")

print("=" * 40)
l5 = [5, 10, 15, 20, [1, 2, 3, 4, 5], 25]
print(f"l5 before :{l5}")

l6 = l5.copy()          # deep copy
print(f"l6 before :{l6}")

l6[4].extend([6, 7, 8])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 40)
from copy import deepcopy
l7 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l7 before :{l7}")

l8 = deepcopy(l7)           # deepcopy
print(f"l8 before :{l8}")

l8[4].insert(1, "a")
l8[4].insert(3, "b")
l8[4].insert(5, "c")
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

