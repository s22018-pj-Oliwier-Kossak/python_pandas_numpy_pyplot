import pandas as pd

countries = pd.read_csv("csv_files/countries.csv",usecols=["Symbol","Name"],index_col="Symbol",squeeze=True)
countries.dropna(inplace=True)

toFind = ["BB","AA","BS"]
# print(countries.loc[toFind])
print(countries.reindex(toFind))
print(countries.loc[countries.index.intersection(toFind)])
print(countries.index.intersection(toFind))
