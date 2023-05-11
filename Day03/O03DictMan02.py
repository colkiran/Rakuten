
print("keys".center(40, "-"))
player = {'name': 'rahul', 'runs': 80, 'age': 32, 'oppn': 'Newzeland', 'venue': 'Auckland', 'year': 2002}
print(f"player :{player}")

k = player.keys()
print(f"keys :{k}")
print("-" * 40)

for k in player.keys():
    print(k, "=>", player[k])

print("values".center(40, "-"))
player = {'name': 'rahul', 'runs': 80, 'age': 32, 'oppn': 'Newzeland', 'venue': 'Auckland', 'year': 2002}
print(f"player :{player}")

v = player.values()
print(f"values :{v}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")
print(type(cities))

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")
res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("pop".center(40, "-"))
player = {'name': 'rahul', 'runs': 80, 'age': 32, 'oppn': 'Newzeland', 'venue': 'Auckland', 'year': 2002}
print(f"player :{player}")

res = player.pop('age')
print(f"res: {res}")

res = player.pop('venue')
print(f"res: {res}")

# res = player.pop()
# print(f"res: {res}")

print(f"player :{player}")

print("popitem".center(40, "-"))

player = {'name': 'rahul', 'runs': 80, 'age': 32, 'oppn': 'Newzeland', 'venue': 'Auckland', 'year': 2002}
print(f"player :{player}")

res = player.popitem()
print(f'res: {res}')

res = player.popitem()
print(f'res: {res}')

print(f"player :{player}")

print("setdefault".center(40, "-"))
player = {'name': 'sehwag', 'runs': 130, 'oppn': 'Pak'}
print(f"player :{player}")
player.setdefault('year', 2001)
player.setdefault('venue', 'islamabad')
player.setdefault('name', 'Yuvraj')
player.setdefault('runs', 10)

print(f"player :{player}")