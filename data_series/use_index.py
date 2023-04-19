import pandas as pd

surveys = pd.read_csv("csv_files/StackOverflowDeveloperSurvey.csv",usecols=["CompanySize"],squeeze=True).dropna()
print(surveys[3])
print(surveys[1:11])
surveys.sort_values(inplace=True)
print(surveys[1:11])
surveys.reset_index(drop=True,inplace=True)
print(surveys[1:11])