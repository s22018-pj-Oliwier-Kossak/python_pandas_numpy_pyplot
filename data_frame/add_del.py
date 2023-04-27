import pandas as pd

read_csv = pd.read_csv("csv_files/fuel.csv",low_memory=False,usecols=['Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'])
read_csv['Combined KPL'] = read_csv['Combined MPG (FT1)']*1.609 / 3.78
print(read_csv.head())

read_csv.insert(loc=5,column='liters per km',value=100/read_csv[ 'Combined KPL'])
print(read_csv.head())

del read_csv['Combined KPL']
print(read_csv.head())
