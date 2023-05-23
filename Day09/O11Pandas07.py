
import pandas as pd

moviesDF = pd.read_csv("MovieData.csv", index_col="Title")
print(moviesDF)
print(moviesDF.shape)

print("\n", "-" * 40, "\n")

# column Cleanup
print(moviesDF.columns)

# rename the column names
moviesDF.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_Millions'
}, inplace=True)

print(moviesDF.columns)

print("\n", "-" * 40, "\n")
# convert all column names into lower case
moviesDF.columns = [col.lower() for col in moviesDF.columns]
print(moviesDF.columns)

# How to work with missing Values
print(moviesDF.isnull())

print("\n", "-" * 40, "\n")

# column wise count of missing values
print(moviesDF.isnull().sum())

# Removing NULL Values

tempDF = moviesDF.dropna()
print(tempDF)

print("\n", "-" * 40, "\n")

# drop the columns if it has null values
print(moviesDF.shape)
tempDf = moviesDF.dropna(axis=1)
print(tempDf.shape)

print("\n", "-" * 40, "\n")
print(moviesDF.columns)
print(tempDf.columns)

# Impiutation - its a conventional feature engineering technique used to
# keep valuable data that have null values

print("\n", "-" * 40, "\n")
# print(moviesDF.columns)

revenue = moviesDF['revenue_millions']
print(revenue)

print("\n", "-" * 40, "\n")

rev_mean = revenue.mean()
print(revenue.mean())

# fill all the null values with the mean values
revenue.fillna(rev_mean, inplace=True)

print(moviesDF.isnull().sum())
