
import csv

colNames = ['Empid', 'EmpName', 'Age', 'Dept', 'Salary']

data = [
['501', 'Jack', '28', 'HR', '65000'],
['235', 'Jill', '34', 'FIN', '35000'],
['150', 'John', '26', 'AC', '25000'],
['325', 'Jai', '21', 'DEV', '55000'],
['450', 'Guru', '38', 'DEV', '85000'],
['182', 'Sita', '32', 'PRC', '75000'],
['297', 'Gita', '36', 'SUP', '60000']
]

with open("result.csv", "w", newline="") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(colNames)
    for row in data:
        writer.writerow(row)

