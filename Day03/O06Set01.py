
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print('-' * 40)
s2 = {1, 2, 3, 'four', 'five', 6.4, 7.0, 8+0j, 9-0j, False, True}
print(f"s2 :{s2}")
print(type(s2))

print('-' * 40)
s1 = {1, 2, 3}
# add, update
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(5)
s1.add(6)

print(f"s1 :{s1}")
# update
s1.update([1, 2, 3])
s1.update([2, 3, 4])
s1.update([5, 6, 7])
s1.update([3, 4, 5])
s1.update([8, 9, 10])
print(f"s1 :{s1}")

print('-' * 40)
# pop, remove, discard

#pop
r1 = s1.pop()
print(f"r1 :{r1}")

r2 = s1.pop()
print(f"r2 :{r2}")

print(f"s1 :{s1}")

# remove
s1.remove(8)
s1.remove(4)
# s1.remove(1)
print(f"s1 :{s1}")

# discard
s1.discard(10)
s1.discard(6)
s1.discard(1)
print(f's1 :{s1}')

print('-' * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")
print('-' * 40)

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")
print('-' * 40)

print(f"A difference B :{A - B}")
print(f"B difference A :{B - A}")
print('-' * 40)

print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

# frozensets - frozen sets are immutable

fs = frozenset({1, 2, 3, 4, 5})
print(f"fs :{fs}")
print(type(fs))
