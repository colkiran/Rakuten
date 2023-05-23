
import pandas as pd

df = pd.read_json('emp.json')

print(df.to_string())

print("-" * 40)

data = {
    'duration': {
        '0': 50,
        '1': 65,
        '2': 45
    },
    'pulse': {
        '0': 110,
        '1': 130,
        '2': 94
    },
    'calories': {
        '0': 200,
        '1': 250,
        '2': 180
    }
}

df1 = pd.DataFrame(data)
print(df1)

print("-" * 40)

df2 = pd.read_json("books.json")
print(df2)


