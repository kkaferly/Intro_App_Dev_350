# Fuel Economy - A fuel-economy study was carried out for five models of cars. Each car was driven 100 miles, and then the model of the car and the number of 
# gallons used were placed in a line of the file Mileage.txt. Table 5.11 shows the data for the entries of the file. Write a program to display the models and their 
# average miles per gallon in decreasing order with respect to mileage. See Fig. 5.51. The program should create a dictionary of five items, with a key for each 
# model, and a two-tuple for each value. Each two-tuple should be of the form (number of test vehicles for the model, total number of gallons used by the model.)

# Import library
import pickle

# Define list
mileage = [['Prius', 2.1], ['Camry', 4.1], ['Sebring', 4.2], ['Mustang', 5.3], ['Accord', 4.1], ['Camry', 3.8], ['Camry', 3.9], ['Mustang', 5.2], ['Accord', 4.3], ['Prius', 2.3], ['Camry', 4.2], ['Accord', 4.4]]

# Create files
f = open("Mileage.txt", 'wb')
pickle.dump(mileage, f)
f.close()


# ------------ #


def main():
    mileageList = readFile()
    cars = carsDict(mileageList)
    makes, mileages = makeMileage(cars)
    carOutput(makes, mileages)

# Open and read mileage file
def readFile():
    rf = open("Mileage.txt", 'rb')
    mileageList = pickle.load(rf)
    rf.close()

    return mileageList

# Seperate distinct cars and mileage
def carsDict(mileageList):
    cars = {}
    for i in mileageList:
        if cars.get(i[0],0) == 0:
            cars[i[0]] = (1, i[1])
        else:
            count, mileage = cars[i[0]]
            count += 1
            mileage += i[1]
            cars[i[0]] = (count, mileage)

    return cars

# Calculate the average mileage per gallon per car
def makeMileage(cars):
    makes=[]
    mileages=[]

    for i in cars:
        makes.append(i)
        m = cars[i]
        mileages.append(round(m[0] * 100 / m[1], 2))

    mileagesMakes = zip(mileages, makes)
    makes = [x for y, x in sorted(mileagesMakes)]
    mileages.sort()

    makes = makes[::-1]
    mileages = mileages[::-1]

    return makes, mileages

# Print output
def carOutput(makes, mileages):
    print('Model'.ljust(10), 'MPG')

    for i, x in zip(makes, mileages):
        print(i.ljust(10), '{0:0.2f}'.format(x))   

main()
