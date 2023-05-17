
# sys.path - is a list variable

import sys

sys.path.append("c:/delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as gm

gm.greet("Dhoni")
emp1 = gm.Employee("Mike", 75000)
emp1.get_details()