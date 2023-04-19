import pandas as pd

countries_series = pd.read_csv("csv_files/StackOverflowDeveloperSurvey.csv",squeeze=True,usecols=["Country"]).dropna()
print("Spain" in countries_series.values)
print("Wonderland" in countries_series.values)
print(1 in countries_series.index)
