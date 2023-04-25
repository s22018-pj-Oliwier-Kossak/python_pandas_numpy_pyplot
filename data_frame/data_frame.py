import pandas as pd

fuel = pd.read_csv("csv_files/fuel.csv", low_memory=False)
print(fuel.tail(10))
print(fuel.head(5))

fuel = pd.read_csv("csv_files/fuel.csv",usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'], low_memory=False,index_col='Model')
print(fuel)
