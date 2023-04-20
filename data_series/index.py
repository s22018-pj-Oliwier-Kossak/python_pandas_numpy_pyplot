import pandas as pd

fortune500 = pd.read_csv("csv_files/Fortune_500_2017.csv",usecols=["Rank","Title"],squeeze=True,index_col="Rank")
print(fortune500.head(10))
print(fortune500.tail(20))

forutne5001 = pd.read_csv("csv_files/Fortune_500_2017.csv",usecols=["Employees","Title"],squeeze=True,index_col="Title")
print(forutne5001)
print(forutne5001["Facebook"])
print(forutne5001["Apple"])
print(forutne5001["Apple":"IBM"])
