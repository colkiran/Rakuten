
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as csvFile:
    emp_details = csv.reader(csvFile)
    # colNames = next(emp_details)
    # print(*colNames)
    emp_table = PrettyTable(next(emp_details))

    for rec in emp_details:
        # print(*rec)
        emp_table.add_row(rec)

print(emp_table)

