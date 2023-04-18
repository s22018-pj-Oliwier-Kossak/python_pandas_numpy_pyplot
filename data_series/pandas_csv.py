import pandas as pd

read_csv = pd.read_csv('csv_files/StackOverflowDeveloperSurvey.csv', usecols=['FormalEducation'])
print(read_csv)
print(type(read_csv))
print(read_csv.head())

read_csv2 = pd.read_csv('csv_files/StackOverflowDeveloperSurvey.csv', usecols=['FormalEducation'], squeeze=True)
print(read_csv2)
print(type(read_csv2))
print(read_csv2.tail(10))

allInfo = pd.read_csv('csv_files/StackOverflowDeveloperSurvey.csv')
data_series_country = pd.Series(allInfo['Country'])
print(data_series_country)
print(data_series_country.head())

filterOnlyUSA = data_series_country == "United States"
print(filterOnlyUSA)


print(data_series_country.where(filterOnlyUSA).dropna())

