import pandas as pd

programmers = pd.read_csv("csv_files/StackOverflowDeveloperSurvey2018.csv",usecols=["ConvertedSalary"],low_memory=False).squeeze()
programmers.dropna(inplace=True)
print(programmers.mean())
print(programmers.median())
print(programmers.std())

fortune500 = pd.read_csv("csv_files/Fortune_500_2017.csv",usecols=["Title","Employees"],index_col="Title").squeeze()
fortune500.dropna(inplace=True)
print(fortune500.idxmax())
print(fortune500["Walmart"])
print(fortune500.idxmin())
print(fortune500.loc[fortune500.idxmin()])


