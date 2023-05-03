import pandas as pd

fuel = pd.read_csv("csv_files/fuel.csv",
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
                   low_memory=False)
print(fuel.head())
print(fuel.info(memory_usage="deep"))
fuel["Year"] = fuel["Year"].astype('int')
print(fuel.info(memory_usage="deep"))
print(fuel["Make"].value_counts())
fuel["Make"] = fuel["Make"].astype('category')
fuel["Class"] = fuel["Make"].astype('category')
fuel["Model"] = fuel["Make"].astype('category')
fuel["Fuel Type"] = fuel["Make"].astype('category')
print(fuel.info(memory_usage="deep"))
fuel['Combined MPG (FT1)'] = fuel['Combined MPG (FT1)'].astype('float')
print(fuel.info(memory_usage="deep"))
