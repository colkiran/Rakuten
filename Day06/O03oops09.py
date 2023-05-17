
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'NodeJS']

    def __str__(self):
       return f"Name is {self.name} and Salary is {self.salary} \n " \
              f"technologies = {self.tech}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee('Micheal', 65000)
print(emp1)
print("-" * 40)

print(len(emp1))

print("-" * 40)

print([tech for tech in emp1])          # list comprehension
