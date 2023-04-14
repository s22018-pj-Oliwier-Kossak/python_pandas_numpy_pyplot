import pandas as pd
import numpy as np
from matplotlib import pyplot

days = [1,2,3,4,5]
amount = [1,5,20,450,700]

pyplot.plot(days,amount)
pyplot.show()

pyplot.plot(days,amount,'bs')
pyplot.show()

months = np.arange(1,13)
income = [x*3+100 for x in months]

pyplot.plot(months,income,'go')
pyplot.show()

costs = [50+x*10 for x in months]

pyplot.plot(months,costs,'ro',months,income,'go')
pyplot.show()

x = np.arange(-5,5,0.1)
pyplot.plot(x,pow(2,x))
pyplot.xlabel("x")
pyplot.ylabel('x^2')
pyplot.show()