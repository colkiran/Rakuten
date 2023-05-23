
import pandas as pd

data = {
    'cal': [450, 600, 500],
    'dur': [85, 120, 96]
}

df = pd.DataFrame(data)

print(df)

print("-" * 40)
print(df.loc[0])

print("-" * 40)
print(df.loc[[0, 1]])

print("-" * 40)
data = {
    'cal': [450, 600, 500],
    'dur': [85, 120, 96]
}

print("-" * 40)
df1 = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df1)

print(df1.loc['day2'])
