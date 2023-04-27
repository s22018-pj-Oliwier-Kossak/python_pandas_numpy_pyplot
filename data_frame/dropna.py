import pandas as pd
import numpy as np

read_fuel = pd.read_csv("csv_files/fuel.csv", low_memory=False,
                        usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
                        index_col='Vehicle ID')


read_fuel.loc[27705, 'Class'] = np.NaN
read_fuel.loc[26561, 'Class'] = np.NaN
read_fuel.loc[27550, 'read_fuel Type'] = np.NaN
print(read_fuel.head())
read_fuel.dropna(inplace=True,subset=['Class'])
print(read_fuel.head())
read_fuel.dropna(axis=1, inplace=True)
print(read_fuel.head())