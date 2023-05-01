import pandas as pd
import numpy as np

fuel = pd.read_csv("csv_files/fuel.csv", low_memory=False,
                   usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
                   index_col=["Vehicle ID"])

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

print(fuel.head())
print(fuel.fillna(value=-1).head())

replaceRules = {
    "Class": "---",
    "Fuel Type": "---",
    "Combined MPG (FT1)": -1
}

print(fuel.fillna(replaceRules).head())
avgMPG = fuel['Combined MPG (FT1)'].mean()
print(avgMPG)
fuel['Class'].fillna(value='?',inplace=True)
fuel['Fuel Type'].fillna(value='?',inplace=True)
fuel['Combined MPG (FT1)'].fillna(value='?',inplace=True)
print(fuel.head())

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN

fuel['Combined MPG (FT1)'].ffill(inplace=True)
print(fuel.head())
