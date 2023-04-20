import pandas as pd

surveys = pd.read_csv("csv_files/StackOverflowDeveloperSurvey.csv",usecols=["Salary"],squeeze=True)
surveys.dropna(inplace=True)
print(surveys)
print(surveys.count())

surveysIncrease = surveys*1.03
print(surveysIncrease)

surveysAfterIncrease = surveysIncrease + surveys
print(surveysAfterIncrease)

surveysTime = pd.read_csv("csv_files/StackOverflowDeveloperSurvey2018.csv",usecols=["HoursOutside"],low_memory=False,squeeze=True)
surveysTime.dropna(inplace=True)
print(surveysTime.value_counts())
surveysTime = surveysTime.apply(lambda x: x.upper())
print(surveysTime)

def change_description(string_value):
    if string_value == "LESS THAN 30 MINUTES":
        return 'LESS THAN 30 MINUTES'
    else:
        return string_value
print(surveysTime.apply(change_description))

