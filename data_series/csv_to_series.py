import pandas as pd

salary_series = pd.read_csv("csv_files/StackOverflowDeveloperSurvey.csv",usecols=["Salary"],squeeze=True).dropna()

print(salary_series)

print(salary_series.sort_values())
salary_series.sort_values(inplace=True,ascending=False)
print(salary_series.head())
print(salary_series)

max_salaries = salary_series.sort_values(ascending=False)
print(max_salaries.head(100))

min_salaries = salary_series.sort_values(ascending=True)
print(min_salaries.head(100))

average_value = sum(max_salaries) /len(max_salaries )
print("average ",average_value)

