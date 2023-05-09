
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.5, 9.0, 10+0j, 11-5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print(f"id(l2[0]) :{id(l2[0])}")
print(f"id(l2[1]) :{id(l2[1])}")
print(f"id(l2[2]) :{id(l2[2])}")
print(f"id(l2[3]) :{id(l2[3])}")
print(f"id(l2[4]) :{id(l2[4])}")

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

l1 = [1, 2, 3, 4, 5]
l1[3] = 3.5
print(f"l1 :{l1}")
# l1[5] = 6
print("-" * 40)
# print(dir(l1))

# functions that is used to add new elements into the list
print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")

l1.append([10, 20, 30, 40, 50])
print(f"l1 :{l1}")
print(f"l1[8][1:3] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = [1, 2, 3, 4, 5]

l2.extend([6, 7, 8, 9])
print(f"l2 :{l2}")

print("insert".center, "-")
l3= [1, 2, 3, 4, 5]
print(f"l3 :{l3}")
l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)
print(f"l3 :{l3}")

# functions that can remove elements from the list - pop, clear, remove
print("POP".center(40, "-"))
l1 = list(range(1, 16))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(3)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l2 = [1, 2, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1,1, 1, 1, 2, 2,1, 2, 3, 1, 1, 1, 1 ,1 , 1, 1, 1 ,1 ,1]

l2.remove(2)
print(f"l2` :{l2}")

print("-" * 40)
while l2.count(1):
    l2.remove(1)

print(f"l2 :{l2}")

