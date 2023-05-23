
import pandas as pd

data1 = {
    'apples':[3, 4, 1, 6]
}

df1 = pd.DataFrame(data1)
print(df1)
print(df1.shape)
print(type(df1))

print("-" * 40)
data2 = {
    'oranges': [6, 8, 1, 4],
    'grapes': [5, 2, 7, 3]
}

df2 = pd.DataFrame(data2)
print(df2)
print(df2.shape)
