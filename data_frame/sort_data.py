import pandas as pd
import numpy as np

fuel = pd.read_csv("csv_files/fuel.csv",
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
                   low_memory=False)
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NAN
print(fuel.tail())

print(fuel.sort_values(by=['Make', 'Model']).head())
print(fuel.sort_values(by=['Make'], ascending=False).head())
print(print(fuel.sort_values(by=['Make', 'Model'], ascending=[True, False]).head()))
print(fuel.sort_values(by=['Combined MPG (FT1)'], na_position='first').head())
print(fuel.sort_index().head())
