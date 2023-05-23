
import pandas as pd

empdf = pd.read_csv("Employee.csv")

print(empdf)

print("-" * 40)

empdf.to_excel("emp.xlsx")
empdf.to_json("emp.json")
