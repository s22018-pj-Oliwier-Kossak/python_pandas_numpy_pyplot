import pandas as pd


ix = ["do 6", "7-14", "15-17", "18-24", "25-39", "40-59", "60 i więcej"]
val = [14 ,334,312,5823,9491,7486,4343]
accidents = pd.Series(val,ix)
print(accidents )
accidents1000 = accidents .where(accidents  > 1000).dropna()
print(accidents1000)
print(accidents)
print(accidents.filter(items=["do 6", "7-14", "15-17"]))
accidents.where(accidents<1000, inplace=True)
print(accidents.dropna())
