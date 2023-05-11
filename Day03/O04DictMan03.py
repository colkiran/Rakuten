
print("items".center(40,"-"))
# extract keys and values from the dictionary same time

emp = {
    'emp1': {'name': 'Mark', 'age': 45, 'desig': 'director', 'dept': 'finance', 'sal': 345000},
    'emp2': {'name': 'Tina', 'age': 45, 'desig': 'VP', 'dept': 'Mkt', 'sal': 300000},
    'emp3': {'name': 'Micheal', 'age': 35, 'desig': 'TL', 'dept': 'Testing', 'sal': 135000}
}

print(f"emp :{emp}")
print("=" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("=" * 40)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))

emp1 = {'name': 'Mark', 'age': 45, 'desig': 'director', 'dept': 'finance', }
emp2 = {'name': 'Tina', 'age': 45, 'desig': 'VP', 'sal': 300000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("copy".center(40, "-"))
emp1 = {'name': 'Mark', 'age': 45, 'desig': 'director', 'dept': 'finance'}
print(f"emp1 before :{emp1}")

emp2 = emp1             # shallow copy - copies the address along with data
print(f"emp2 before :{emp2}")

print("-" * 40)
emp2['loc'] = 'Hyderabad'
emp2['sal'] = 350000
print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 40)

emp1 = {'name': 'Mark', 'age': 45, 'desig': 'director', 'dept': 'finance'}
print(f"emp1 before :{emp1}")

print(f"emp1 before :{emp1}")
emp2 = emp1.copy()                  # Deep copy - only data gets copied
print(f"emp2 before :{emp2}")

print("-" * 40)
emp2['loc'] = 'Hyderabad'
emp2['sal'] = 350000
print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 40)

emp1 = {'name': 'Mark', 'age': 45, 'desig': {'IBM': 'Trainee', 'Tesco': 'Sr.SE', 'TCS': 'PM', 'Dell': 'director'}, 'dept': 'finance'}
print(f"emp1 before :{emp1}")

emp2 = emp1.copy()
print(f"emp2 before :{emp2}")

print("-" * 40)
emp2['desig']['wipro'] = 'MGR'
emp2['desig']['itc'] = 'sr MGR'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 40)

emp1 = {'name': 'Mark', 'age': 45, 'desig': {'IBM': 'Trainee', 'Tesco': 'Sr.SE', 'TCS': 'PM', 'Dell': 'director'}, 'dept': 'finance'}
print(f"emp1 before :{emp1}")

from copy import deepcopy
emp2 = deepcopy(emp1)
print(f"emp2 before :{emp2}")

print("-" * 40)
emp2['desig']['wipro'] = 'MGR'
emp2['desig']['itc'] = 'sr MGR'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print('clear'.center(40, "-"))
emp1 = {'name': 'Mark', 'age': 45, 'desig': {'IBM': 'Trainee', 'Tesco': 'Sr.SE', 'TCS': 'PM', 'Dell': 'director'}, 'dept': 'finance'}
print(f"emp1 before :{emp1}")

emp1.clear()
print(f"emp1 :{emp1}")
