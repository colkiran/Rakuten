
gstName = "Sachin"

sports = ['cricket', 'hockey', 'tennis', 'soccer', 'swimming']

runs = {'test': 21500, 'odi': 32350, 't20': 1500}

def greet(gst):
    print(f"Greetings Mr.{gst}, Welcome to the event")

class Employee:

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")
