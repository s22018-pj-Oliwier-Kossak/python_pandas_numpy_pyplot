import pandas as pd
import numpy as np
import random
from matplotlib import pyplot

data_as_float_list = [random.random() for x in range(10000)]
data_float_series = pd.Series(data_as_float_list)

print(data_float_series.size)
print(data_float_series.nbytes)
print(data_float_series.shape)
print(data_float_series.axes)
print(data_float_series.index)
print(data_float_series.is_unique)

data_as_string_list = [str(random.random()) for x in range(10000)]
data_string_series = pd.Series(data_as_string_list)
print(data_string_series.size)
print(data_string_series.nbytes)
print(data_string_series.shape)



