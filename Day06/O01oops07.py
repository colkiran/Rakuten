# Magic Methods

from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
       return f"Name is {self.name} and Salary is {self.salary} "

    # automatically overrides the not equal operator
    def __eq__(self, other):
        return self.salary == other.salary

    # automatically overrides the less than operator
    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Jack", 50000)
emp2 = Employee("Kevin", 55000)
# emp1.get_detials()

print("-" * 40)
print(str(emp1))            # str is an operator
print(emp1)                 # it implicitly call __str__ method

print("-" * 40)
print(emp1 == emp2)         # by default compares the addresses

if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
print(emp1 > emp2)

if emp1 < emp2:
    print("{} salary of {} is less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is not less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
print(emp1 >= emp2)