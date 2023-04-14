import pandas as pd
import numpy as np
from matplotlib import pyplot

days = [x for x in range(8)]
data_series = pd.Series(days)
print(data_series)
free_days={1:False,
           2:False,
           3:False,
           4:False,
           5:False,
           6:True,
           7:True}
data_series_freedays = pd.Series(free_days)
print(data_series_freedays)
