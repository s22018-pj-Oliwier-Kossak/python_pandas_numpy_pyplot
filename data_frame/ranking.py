import pandas as pd

fortune = pd.read_csv("csv_files/Fortune_500_2017.csv", usecols=['Rank','Title','Employees','Profits','Assets'], index_col='Rank')
fortune['RankEmployees']  = fortune['Employees'].rank(ascending=False)
fortune['RankByProfits']  = fortune['Profits'].rank(ascending=False)
print(fortune.head())
print(fortune.nlargest(n=3,columns='Assets'))
print(fortune.nsmallest(n=3,columns='Assets'))