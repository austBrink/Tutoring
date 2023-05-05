import sqlite3


conn = sqlite3.connect('cities.db')

# city id, city name, population 

namesByPop = conn.execute('''
    SELECT CityName FROM Cities ORDER BY Population
''')

for row in namesByPop:
   print ("ID = ", row[0])
   print ("CITY NAME = ", row[1])
   print ("POPULATION = ", row[2] )


namesByPopDesc = conn.execute('''
    SELECT CityName FROM Cities ORDER BY Population DESC
''')

for row in namesByPopDesc:
   print ("ID = ", row[0])
   print ("CITY NAME = ", row[1])
   print ("POPULATION = ", row[2] )

namesSortedByNames = conn.execute('''
    SELECT CityName FROM Cities ORDER BY CityName
''')

for row in namesSortedByNames:
   print ("CITY NAME = ", row[0])

totalPopulationOfCities = conn.execute('''
    SELECT SUM(Population) as populationSum FROM Cities
''')

for row in totalPopulationOfCities:
   print("POPULATION SUM = ", row[0])

averagePopulation = conn.execute('''
    SELECT ( SUM(Population) / COUNT(Population) ) as populationAverage FROM Cities
''')

getMaxPopulationCity = conn.execute('''
    SELECT CityName FROM Cities WHERE Population = (SELECT MAX(Population) FROM Cities)
''')

getMinPopulationCity = conn.execute('''
    SELECT CityName FROM Cities WHERE Population = (SELECT MIN(Population) FROM Cities)
''')



