
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'host': 'localhost', 'user': 'root', 'pwd': 'tiger', 'db': 'emp'}
print(f'd2 :{d2}')
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'rahul'), ('age', 30), ('runs', 125), ('oppn', 'sri lanka'), ('year', 2001)])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='sachin', age=32, runs=98, oppn='England', year=1997)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'Sachin', 'runs': 120, 'oppn': 'Bangladesh', 'year': 2005}
print(f"player :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

# iterate - keys
for x in player:
    print(x + "=>" + str(player[x]))

print("-" * 40)
# update
print(f'player :{player}')
player['name'] = 'Sehwag'           # update
player['runs'] = 65                 # update
player['venue'] = 'Chinaswamy'      # new

print(f"player :{player}")

print("-" * 40)
# delete
print(f"player :{player}")

del player['year']
del player['oppn']

print(f"player :{player}")

print("-" * 40)
# print(dir(d1))
print("get".center(40, "-"))

player = {'name': 'Sachin', 'runs': 120, 'oppn': 'Bangladesh', 'year': 2005}
print(f"player :{player}")


res = player.get("name", "Please check the key mentioned........")
print(f"Name :{res}")
# print(f"Venue :{player['venue']}")
res = player.get("venue", "Please check the key mentioned......")
print(f"res :{res}")
