
class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech = ['C', 'C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'NodeJS']

    def __str__(self):
        return self.__name + " " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Kevin")
print(emp1)
# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Ricard"
print(emp1)