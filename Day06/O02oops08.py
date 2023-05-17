
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
       return f"Name is {self.name} and Salary is {self.salary} "

    def __add__(self, other):
        return f"Result of addition is : {self.salary + other.salary}"

    def __sub__(self, other):
        return f"Result of substraction is : {self.salary - other.salary}"

    def __mul__(self, other):
        return f"Result of multiplication is : {self.salary * other.salary}"

    def __truediv__(self, other):
        return f"Result of division is : {self.salary / other.salary}"

    def __floordiv__(self, other):
        return f"Result of division is : {self.salary // other.salary}"


emp1 = Employee("Rahul", 30000)
emp2 = Employee("Kiran", 20000)

print(emp1 + emp2)
print(emp1 - emp2)
print(emp1 * emp2)
print(emp1 / emp2)
print(emp1 // emp2)
# code to overload all arithmetic operators - +, -, *, /, //