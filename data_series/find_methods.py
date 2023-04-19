import pandas as pd

countries = pd.read_csv("csv_files/countries.csv",usecols=['Symbol','Name'],index_col='Symbol',squeeze=True)
print(countries.head(20))
print(countries.loc["FR"])
print()
print(countries.iloc[13])
print()
nordic = ["FI","SE","NO"]
print(countries.loc[nordic])