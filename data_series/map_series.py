import pandas as pd
import random
dict = {"symbol PYT001 ": "Airbus 320",
        "symbol PYT002" :"Boeing 737",
        "symbol PYT003" :"Airbus 321"}

aircrafts = pd.Series(dict)
print(aircrafts)

flightsList = []

for i in range(100):
    rand = random.randint(0,2)
    flightsList.append(aircrafts[rand])
print(flightsList[:5])

flights = pd.Series(flightsList)
print(flights)
flights_aircrafts = flights.map(aircrafts)
print(flights_aircrafts)