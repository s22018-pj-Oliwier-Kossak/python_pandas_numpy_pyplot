import pandas as pd

read_csv = pd.read_csv("csv_files/StackOverflowDeveloperSurvey.csv", usecols=["Salary"], squeeze=True)
salary = read_csv.dropna()
print(salary.head())
print(len(salary))
print(min(salary))
print(max(salary))
salary_list = list(salary.head())
print(salary_list)
listSalarySorted = sorted(salary)
print(listSalarySorted)
print(listSalarySorted[:5])
