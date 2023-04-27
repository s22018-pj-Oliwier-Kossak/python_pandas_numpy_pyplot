import pandas as pd

read_csv = pd.read_csv("csv_files/fuel.csv",low_memory=False,usecols=[ 'Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'])
print(read_csv.info())
print(read_csv.dtypes)
print(read_csv.dtypes.value_counts())
print(read_csv['Make'].value_counts().head(10))
print(read_csv.index)
print(read_csv.columns)
print(read_csv.values)
print(read_csv.axes)
print(read_csv.shape)
print(read_csv.count())
print(len(read_csv))