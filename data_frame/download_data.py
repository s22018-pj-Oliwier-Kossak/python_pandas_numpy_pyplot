import pandas as pd

read_csv = pd.read_csv("csv_files/fuel.csv",low_memory=False,usecols= ['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'])

make =read_csv['Make']
print(make)
print(make.value_counts().head())
print(make.loc[1873])
print(read_csv['Combined MPG (FT1)'][1873])
print(read_csv['Combined MPG (FT1)'].idxmax())
shortFuel = read_csv[['Make','Model']]
print(shortFuel.head())