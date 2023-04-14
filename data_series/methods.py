import pandas as pd
import numpy as np
from matplotlib import pyplot

cities = ['Shanghai', 'Beijing', 'Istanbul']
population = [24183300, 20794100, 15030000]

citypop = pd.Series(index=cities,data=population)
print(citypop)
print(citypop.sum())
print(citypop.mean())
print(citypop.size)
print(citypop.count())
print(citypop.index)
print(citypop.values)