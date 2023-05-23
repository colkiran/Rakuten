
import pandas as pd

# creating a dataframe from a CSV file
moviesDF = pd.read_csv("MovieData.csv", index_col="Title")

# viewing the data from the dataframe
print(moviesDF)

# by default it prints the top 5 rows
print(moviesDF.head())

# by default it prints the bottom 5 rows
print(moviesDF.tail())

print(moviesDF.head(10))

print(moviesDF.tail(2))

print("\n", "-" * 40, "\n")

print(moviesDF.info())

print("\n", "-" * 40, "\n")

print(moviesDF.shape)

# Handling duplicates

print("\n", "-" * 40, "\n")

tempDF = moviesDF._append(moviesDF)
print(tempDF.shape)


print("\n", "-" * 40, "\n")
tempDF = tempDF.drop_duplicates()
print(tempDF.shape)

print("\n", "-" * 40, "\n")
tempDF = moviesDF._append(moviesDF)
print(f"Shape before :{tempDF.shape}")
tempDF.drop_duplicates(inplace=True, keep=False)
print(f"Shape after  :{tempDF.shape}")

"""
keep = first
keep = last
false = drop all duplicates
"""

