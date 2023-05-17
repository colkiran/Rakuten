
# import sys
#
# for pth in sys.path:
#     print(pth)

import gurgaon.mymodule as gm
from gurgaon.mymodule import Employee

gm.greet("Virat Kholi")
emp1 = Employee("John", 35000)
emp1.get_details()