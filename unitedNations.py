class Nation:
    def __init__(self, name = "", continent = "", population = 0.0, area = 0):
        self._name = name
        self._continent = continent
        self._population = population
        self._area = area

    def setName(self, name):
        self._name = name

    def setContinent(self, continent):
        self._continent = continent

    def setPopulation(self, population):
        self._population = population

    def setArea(self, area):
        self._area = area

    def getName(self):
        return self._name

    def popDen(self):
        popDen = self._population / self._area

        popDen = round(popDen, 2)

        return popDen
        
        
        
import pickle
# import nation

unitedNations = [('Canada', 'North America', 34.8, 3855000), ('France', 'Europe', 66.3, 211209), ('New Zealand', 'Australia/Oceana', 4.4, 103738), 
    ('Nigeria', 'Africa', 177.2, 356669), ('Pakistan', 'Asia', 196.2, 310403), ('Peru', 'South America', 30.1, 496226), ('Ecuador', 'South America', 17.64, 109483), 
    ('Colombia', 'South America', 50.88, 441200), ('Venezuela', 'South America', 28.44, 353841), ('Brazil', 'South America', 212.6, 3288000)]

f = open("UN.txt", 'wb')
pickle.dump(unitedNations, f)
f.close()


# ------A------ #


# Program to create .dat file from UN file and include population density
def populationDensityCalc():
    un = openFile()
    unDict = unDictionary(un)
    createFile(unDict)

# Open UN file
def openFile():
    f = open("UN.txt", 'rb')
    un = pickle.load(f)
    f.close()

    return un

# Create dictionary from file using Nation class
def unDictionary(un):
    unDict = {}

    for entry in un:
        name = entry[0]
        continent = entry[1]
        population = entry[2] * 1000000
        area = entry[3]
        country = Nation(name, continent, population, area)
        unDict[country.getName()] = (continent, population, area, country.popDen())

    return unDict

# Write dictionary to file
def createFile(unDict):
    f = open("unDict.dat", 'wb')
    pickle.dump(unDict, f)
    f.close()


# Initialize program
populationDensityCalc()


# ------B------ #


# Program to provide information on a country based on user input
def countryInfo():
    unDict = openFile()
    country = userInput()
    data = retrieveInfo(unDict, country)
    countryOuput(data)

# Open unDict file
def openFile():
    f = open("unDict.dat", 'rb')
    unDict = pickle.load(f)
    f.close()

    return unDict

# Ask for user input
def userInput():
    country = input("Enter a country: ")
    country = country.title()

    return country

# Find information in the dictionary for the user selected country
def retrieveInfo(unDict, country):
    data = []

    for i, (w, x, y, z) in unDict.items():
        if country in i:
            data = (i, w, x, y, z)

    return data

# Print information from the dictionary based on user input
def countryOuput(data):
    print("Enter a country: {0}".format(data[0]))
    print("Continent: {0}".format(data[1]))
    print("Population: {0:,d}".format(int(data[2])))
    print("Area: {0:,.2f}".format(data[3]))


# Initialize program
countryInfo()


# ------C------ #


# Program to find countries that are in the same continent from the file
def continentInfo():
    unDict = openFile()
    continent = userInput()
    countries = retrieveCountries(unDict, continent)
    continentOutput(continent, countries)

# Open unDict file
def openFile():
    f = open("unDict.dat", 'rb')
    unDict = pickle.load(f)
    f.close()

    return unDict

# Prompts user for continent input
def userInput():
    continent = input("Enter a continent: ")
    continent = continent.title()

    return continent

# Retrieves the countires from the file that share a continent then sorts in descending order
def retrieveCountries(unDict, continent):
    countries = []

    for i, (w, x, y, z) in unDict.items():
        if continent == w:
            data = (i, w, x, y, z)
            data = (i, z)
            countries.append(data)

    countries = sorted(countries, key = lambda x: int(x[1]), reverse = True)
    
    return countries

# Print output for countires on the user provided continent
def continentOutput(continent, countries):
    print("\nEnter a continent: {0}".format(continent))
    for i in countries:
        print(i[0])


# Initialize program
continentInfo()        
