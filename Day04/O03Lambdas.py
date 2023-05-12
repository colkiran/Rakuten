
def addMe(x, y):
    return x + y

a = addMe

res = a(10, 20)
print(f"res :{res}")

print("-" * 40)
b = lambda x, y: x + y
res = b(100, 200)

print(f"res :{res}")

# lambdas are best used map, filter and reduce
# map - implement the given expression on each value of a given collection
# filter - implement the given expression of each value, but the expression should
#            return a True or False
# reduce - reduce is imported from functools module and as mentioned it reduces the collection to a single value

print("MAP".center(40, "-"))
lst = list(range(1, 11))
print(f"list :{lst}")

squares = list(map(lambda x: x ** 2, lst))
print(f"squares :{squares}")

print("-" * 40)

months = ['dec', 'apr', 'aug', 'feb', 'mar', 'oct', 'sep', 'jan', 'nov', 'jul', 'may', 'jun']
print(f"months :{months}")

from calendar import month_abbr
print(f"Month :{list(month_abbr)}")

srtd_mon =sorted(months,  key = list(map(lambda mth: mth.lower(), list(month_abbr))).index)
print(f"Sorted Months :{srtd_mon}")

print("=" * 40)
print("FILTER".center(40, "-"))
l2 = list(range(1, 16))
print(f'l2 :{l2}')

res = list(filter(lambda x : x %  2 == 0, l2))
print(f"res :{res}")

l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,]

res = list(filter(lambda x: x != 1, l1))
print(f"res :{res}")

print("REDUCE".center(40, "-"))
from functools import reduce

l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = reduce(lambda x, y: x + y, l1)
print(f'res :{res}')

print("-" * 40)
l2 = [9, 1, 5, 10, 3, 8, 4, 2, 7, 8]
print(f"l2 :{l2}")
ln = reduce(lambda x, y: x if x > y else y, l2)
print(f"largest :{ln}")
