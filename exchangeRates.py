# Exchange Rates - The text file Exchrate.txt gives information about the currencies of 49 major countries. The first eight lines of the file are as follows:

    # America, Dollar, 1
    # Argentina, Peso, 8.405692
    # Australia, Dollar, 1.070835
    # Austria, Euro, 0.760488
    # Belgium, Euro, 0.760488
    # Brazil, Real, 2.237937
    # Canada, Dollar, 1.0086126
    # Chile, Peso, 591.4077

# Each line of the file gives the name of a country, the name of its currency, and the number of units of the currency that were equal to one American dollar 
# (called the exchange rate). For instance, one American dollar is equal to 591.4077 Chilean pesos. Use the text file Exchrate.txt in parts (a), (b), and (c).

    # (a) - Write a program that requests the name of a country as input and then displays the name of its currency and its exchange rate.
    # (b) - Write a program that displays the names of the countries in ascending order determined by the number of units that can be purchased for one American dollar.
    # (c) - Write a program that requests the names of two countries and an amount of money, and then converts the amount from the first country's currency to the 
    # equivalent amount in the second country's currency.
    

# Import library
import pickle

# Define list
exchrate = [['America', 'Dollar', 1], ['Argentina', 'Peso', 8.405692], ['Australia', 'Peso', 1.070835], ['Austria', 'Euro', 0.760488], ['Belgium', 'Euro', 0.760488], ['Brazil', 'Real', 2.237937], ['Canada', 'Dollar', 1.0086126], ['Chile', 'Peso', 591.4077]]

# Create files
f = open("Exchrate.txt", 'wb')
pickle.dump(exchrate, f)
f.close()


# -----A------ #


def mainA():
    exchrate = fileOpen()
    country = userInputCountry()
    currency, rate = countryCurrency(country, exchrate)
    outputCountryCurrency(country, currency, rate)
    mainB()
    mainC()

# Open & read file
def fileOpen():
    rf = open("Exchrate.txt", 'rb')
    exchrate = pickle.load(rf)
    rf.close()

    return exchrate

# Requests user input
def userInputCountry():
    country = input("Enter the name of a country: ")

    country = country.title()

    return country

# Returns the currency & exchange rate for the country
def countryCurrency(country, exchrate):
    l = len(exchrate)
    currency = ""
    i = 0
    rate = 0

    for i in range(l):
        if country in exchrate[i]:
            currency = exchrate[i][1]
            rate = exchrate[i][2]

    return currency, rate

# Prints the output for the user input
def outputCountryCurrency(country, currency, rate):
    print("Enter the name of a country: {0}".format(country))
    print("Currency: {0}".format(currency))
    print("Exchange rate: {0}".format(rate))


# -----B------ #


def mainB():
    exchrate = fileOpen()
    order = countryOrder(exchrate)
    outputCountryOrder(order)

# Return list of countries in order by purchasing power
def countryOrder(exchrate):
    order = sorted(exchrate, key = lambda x: int(x[2]))

    return order

# Output the countries list
def outputCountryOrder(order):
    l = len(order)
    i = 0

    for i in range(0, l):
        print(order[i][0])


# -----C------ #


def mainC():
    exchrate = fileOpen()
    countryOne, countryTwo, amount = multipleInputs()
    conversionAmount, countryOneCurrency, countryTwoCurrency = currencyConversion(exchrate, countryOne, countryTwo, amount)
    outputConversion(countryOne, countryOneCurrency, countryTwo, countryTwoCurrency, amount, conversionAmount)

def multipleInputs():
    countryOne = input("Enter name of first country: ")
    countryTwo = input("Enter name of a second country: ")
    amount = input("Amount of money to convert: ")

    countryOne = countryOne.title()
    countryTwo = countryTwo.title()

    return countryOne, countryTwo, amount

def currencyConversion(exchrate, countryOne, countryTwo, amount):
    l = len(exchrate)
    i = 0
    countryOneCurrency = ""
    countryTwoCurrency = ""
    countryTwoRate = 0

    for i in range(l):
        if countryOne in exchrate[i]:
            countryOneCurrency = exchrate[i][1]

    for i in range(l):
        if countryTwo in exchrate[i]:
            countryTwoCurrency = exchrate[i][1]
            countryTwoRate = exchrate[i][2]

    conversionAmount = float(amount) * countryTwoRate

    return conversionAmount, countryOneCurrency, countryTwoCurrency

def outputConversion(countryOne, countryOneCurrency, countryTwo, countryTwoCurrency, amount, conversionAmount):

    print("Enter the name of first country: {}".format(countryOne))
    print("Enter name of second country: {}".format(countryTwo))
    print("Amount of money to convert: {}".format(amount))
    print("{0} {1} from {2} equals {3:,} {4} from {5}".format(amount, countryOneCurrency, countryOne, conversionAmount, countryTwoCurrency, countryTwo))

mainA()
