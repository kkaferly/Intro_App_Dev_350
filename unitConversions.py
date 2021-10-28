# Unit Conversions - Write a program that displays the nine different units of measure; requests the units to convert from, the unit to convert to, 
# and the quantity to be converted; and then displays the converted quantity. Use the file Units.txt to create a dictionary that provides the number of feet for a 
# given unit of length. The first two lines of the file are inches, .083333; furlongs, 660.

# Import library
import pickle

# Create dictionary
units = {"inches" : .083333, "furlongs" : 660, "yards" : 3, "rods" : 16.5, "miles" : 5280, "fathoms" : 6, "meters" : 3.28155, 
    "kilometers" : 3281.5, "feet" : 1}

# Create file
f = open("Units.txt", 'wb')
pickle.dump(units, f)
f.close()

# ------------- #

# Call functions to begin unit conversions
def main():
    units = openFile()
    display(units)
    convertFrom, convertTo, inputFrom = inputs1(units)
    changed = convert(units, convertFrom, convertTo, inputFrom)
    output(convertFrom, convertTo, inputFrom, changed)

# Open file 
def openFile():
    f = open("Units.txt", 'rb')
    units = pickle.load(f)
    f.close()
    
    return units

# Display input options
def display(units):
    print("UNITS OF LENGTH \n{0:10} {1:15} {2:10}\n{3:10} {4:15} {5:10}\n{6:10} {7:15} {8:10}".format(*units))

# Input to be converted from
def inputs1(units):
    convertFrom = input("Units to convert from: ")
    convertTo = input("Units to convert to: ")
    inputFrom = input(f"Enter length in {convertFrom}: ")
    
    return convertFrom, convertTo, inputFrom

# Conversion calculations
def convert(units, convertFrom, convertTo, inputFrom):
    convert = units.get(convertFrom)
    converted = units.get(convertTo)
    changed = (float(convert) * float(inputFrom)) / float(converted)
    
    return changed

def output(convertFrom, convertTo, inputFrom, changed):
    print(f"Units to convert from: {convertFrom} \nUnits to convert to: {convertTo} \nEnter length in {convertFrom}: {inputFrom} \
        \nLength in {convertTo}: {round(changed, 4)}")

# Run
main()
