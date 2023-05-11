
"""
sort   - sort will sort the original list
sorted - sorted will sort the list and returns a copy of it
"""


print("Sort".center(40, "-"))

l1 = [9, 5, 1, 10, 3, 4, 7, 2, 6, 8]
print(f'l1 :{l1}')
res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)         #descending order
print(f"Descending :{res_desc}")

print(f"list l1 :{l1}")
l1.sort()

print(f"list l1 :{l1}")

print("-" * 40)
l1 = [9, 'zebra', 5, 'apple', 1, 'yellow', 10, 'blue', 3, 'xray', 4, 'white', 7,'green', 2, 'violet', 6, 'red', 8, 'pink', 'cat', 'dog', 'hen', 1098, 198, 19, 2134, 265, 29]
print(f'l1 :{l1}')

print("=" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("=" * 40)
res1 = sorted(res[res.index(1):])
res2 = res[:res.index('zebra')] + res1
print(f"res2 :{res2}")

print("reverse".center(40, "-"))
# reverse and reversed
l1 = [9, 5, 1, 10, 3, 4, 7, 2, 6, 8]
print(f'l1 :{l1}')

print("-" * 40)
res = list(reversed(l1))
print(f"res :{res}")
