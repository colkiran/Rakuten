
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'NodeJS']

    def __str__(self):
       return f"Name is {self.name} and Salary is {self.salary} \n " \
              f"technologies = {self.tech}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("Tina", 75000)
print(emp1)
print("-" * 40)

print([tech for tech in emp1])

print("-" * 40)
emp1.append("Python")
print([tech for tech in emp1])

print("-" * 40)
a = emp1[3]
print(f"a :{a}")

a = emp1[6]
print(f"a :{a}")

print([tech for tech in emp1])

print("-" * 40)
emp1[3] = 'EJB'
print([tech for tech in emp1])
