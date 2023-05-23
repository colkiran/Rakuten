
import pandas as pd

a = [1, 7, 2]

ser1 = pd.Series(a)
print(ser1)

print("-" * 40)

ser2 = pd.Series(a, index=["x", "y", "z"])
print(ser2)

print(f"ser2['y'] :{ser2['y']}")

print("-" * 40)
calories = {'day1':450, 'day2':150, 'day3':580, 'day4':250, 'day5': 230 }
ser3 = pd.Series(calories, index=['day1', 'day2', 'day3', 'day4', 'day5'])
print(ser3)
