# U.S. Senate - The file Senate113.txt contains the members of the 113th U.S. Senate that is, the senate prior to the November 2014 election. Each record of the 
# file consists of three fields-name, state, and party affiliation. Some records in the file are as follows:</br>

    # Richard Shelby, Alabama, R
    # Bernard Sanders, Vermont, I
    # Kristen Gillibrand, New York, D

# The file RetiredSen.txt contains the records from the file Senate113.txt for senators who left the Senate after the November 2014 election due to retirement, 
# defeat, death, and resignation. Some records in the file are as follows:

    # John Rockefeller, West Virginia, D
    # Tom Coburn, Oklahoma, R
    # Carl Levin, Michigan, D

# The file NewSen.txt contains records for the senators who were newly elected in November 2014 or who were appointed to fill the seats of senators who left fter 
# November 2014 election. Some records in the file are as follows:

    # Shelly Capito, West Virginia, R
    # Steve Daines, Montana, R
    # Gary Peters, Michigan, D

# (a) - Write a program that uses the three files above to create the file Senate114.txt that contains records (each consisting of three fields) for the members of 
# the 114th senate where the members are ordered by state. Use the file in parts (b), (c), and (d).
# (b) - Write a program that determines the number of senators of each party affiliation.
# (c) - Write a program that determines the number of states whose two senators have the same party affiliation.
# (d) - Write a program that asks the user to input a state, and then displays the two senators from that state.

# Import Library
import pickle

# Define lists
senate113 = [['Jeff Sessions', 'Alabama', 'R'], ['Richard Shelby', 'Alabama', 'R'], ['Mark Begich', 'Alaska', 'D'], ['Lisa Murkowski', 'Alaska', 'R'], ['Jeff Flake', 'Arizona', 'R'], ['John McCain', 'Arizona', 'R'], ['Mark Pryor', 'Arkansas', 'D'], ['John Boozman', 'Arkansas', 'R'], 
    ['Dianne Feinstein', 'California', 'D'], ['Barbara Boxer', 'California', 'D'], ['Mark Udall', 'Colorado', 'D'], ['Michael Bennet', 'Colorado', 'D'], ['Chris Murphy', 'Connecticut', 'D'], ['Richard Blumenthal', 'Connecticut', 'D'], 
    ['Tom Carper', 'Delaware', 'D'], ['Chris Coons', 'Delaware', 'D'], ['Bill Nelson', 'Florida', 'D'], ['Marco Rubio', 'Florida', 'R'], ['Saxby Chambliss', 'Georgia', 'R'], ['Johnny Isakson', 'Georgia', 'R'], ['Mazie Hirono', 'Hawaii', 'D'], ['Brian Schatz', 'Hawaii', 'D'], 
    ['Jim Risch', 'Idaho', 'R'], ['Mike Crapo', 'Idaho', 'R'], ['Dick Durbin', 'Illinois', 'D'], ['Mark Kirk', 'Illinois', 'R'], ['Joe Donnelly', 'Indiana', 'D'], ['Dan Coats', 'Indiana', 'R'], ['Tom Harkin', 'Iowa', 'D'], ['Chuck Grassley', 'Iowa', 'R'], 
    ['Pat Roberts', 'Kansas', 'R'], ['Jerry Moran', 'Kansas', 'R'], ['Mitch McConnell', 'Kentucky', 'R'], ['Rand Paul', 'Kentucky', 'R'], ['Mary Landrieu', 'Louisiana', 'D'], ['David Vitter', 'Louisiana', 'R'], 
    ['Angus King', 'Maine', 'I'], ['Susan Collins', 'Maine', 'R'], ['Benjamin Cardin', 'Maryland', 'D'], ['Barbara Mikulski', 'Maryland', 'D'], ['Elizabeth Warren', 'Massachusetts', 'D'], ['Ed Markey', 'Massachussets', 'D'], ['Debbie Stabenow', 'Michigan', 'D'], ['Carl Levin', 'Michigan', 'D'], ['Amy Klobuchar', 'Minnesota', 'D'], 
    ['Al Franken', 'Minnesota', 'D'], ['Roger Wicker', 'Mississippi', 'R'], ['Thad Cochran', 'Mississippi', 'R'], ['Claire McCaskill', 'Missouri', 'D'], ['Roy Blunt', 'Missouri', 'R'], ['Jon Tester', 'Montana', 'D'], ['John Walsh', 'Montana', 'D'], 
    ['Deb Fischer', 'Nebraska', 'R'], ['Mike Johanns', 'Nebraska', 'R'], ['Dean Heller', 'Nevada', 'R'], ['Harry Reid', 'Nevada', 'D'], ['Jeanne Shaheen', 'New Hampshire', 'D'], ['Kelly Ayotte', 'New Hampshire', 'R'], ['Bob Menendez', 'New Jersey', 'D'], ['Cory Booker', 'New Jersey', 'D'], ['Martin Heinrich', 'New Mexico', 'D'], 
    ['Tom Udall', 'New Mexico', 'D'], ['Kristen Gillibrand', 'New York', 'D'], ['Chuck Schumer', 'New York', 'D'], ['Kay Hagan', 'North Carolina', 'D'], ['Richard Burr', 'North Carolina', 'R'], ['Heidi Heitkamp', 'North Dakota', 'D'], ['John Hoeven', 'North Dakota', 'R'], 
    ['Sherrod Brown', 'Ohio', 'D'], ['Rob Portman', 'Ohio', 'R'], ['Jim Inhofe', 'Oklahoma', 'R'], ['Tom Coburn', 'Oklahoma', 'R'], ['Jeff Merkley', 'Oregon', 'D'], ['Ron Wyden', 'Oregon', 'D'], 
    ['Bob Casey Jr.', 'Pennsylvania', 'D'], ['Pat Toomey', 'Pennsylvania', 'R'], ['Sheldon Whitehouse', 'Rhode Island', 'D'], ['Jack Reed', 'Rhode Island', 'D'], ['Lindsey Graham', 'South Carolina', 'R'], ['Tim Scott', 'South Carolina', 'R'], ['Tim Johnson', 'South Dakota', 'D'], ['John Thune', 'South Dakota', 'R'], 
    ['Bob Corker', 'Tennessee', 'R'], ['Lamar Alexander', 'Tennessee', 'R'], ['Ted Cruz', 'Texas', 'R'], ['John Cornyn', 'Texas', 'R'], ['Orrin Hatch', 'Utah', 'R'], ['Mike Lee', 'Utah', 'R'], ['Bernie Sanders', 'Vermont', 'I'], ['Patrick Leahy', 'Vermont', 'D'], ['Tim Kaine', 'Virginia', 'D'], ['Mark Warner', 'Virginia', 'D'], 
    ['Maria Cantwell', 'Washington', 'D'], ['Patty Murray', 'Washington', 'D'], ['Joe Manchin', 'West Virginia', 'D'], ['Jay Rockefeller', 'West Virginia', 'D'], ['Tammy Baldwin', 'Wisconsin', 'D'], ['Ron Johnson', 'Wisconsin', 'R'], ['John Barrasso', 'Wyoming', 'R'], ['Mike Enzi', 'Wyoming', 'R']]

retiredSen = [['Mark Begich', 'Alaska', 'D'], ['Mark Pryor', 'Arkansas', 'D'], ['Mark Udall', 'Colorado', 'D'], ['Saxby Chambliss', 'Georgia', 'R'], ['Tom Harkin', 'Iowa', 'D'], ['Mary Landrieu', 'Louisiana', 'D'], ['Carl Levin', 'Michigan', 'D'], ['John Walsh', 'Montana', 'D'], ['Mike Johanns', 'Nebraska', 'R'], 
    ['Kay Hagan', 'North Carolina', 'D'], ['Tom Coburn', 'Oklahoma', 'R'], ['Tim Johnson', 'South Dakota', 'D'], ['Jay Rockefeller', 'West Virginia', 'D']]

newSen = [['Dan Sullivan', 'Alaska', 'R'], ['Tom Cotton', 'Arkansas', 'R'], ['Cory Gardner', 'Colorada', 'R'], ['David Perdue', 'Georgia', 'R'], ['Joni Ernst', 'Iowa', 'R'], ['Bill Cassidy', 'Louisiana', 'R'], ['Gary Peters', 'Michigan', 'D'], ['Steve Daines', 'Montana', 'R'], ['Ben Sasse', 'Nebraska', 'R'], 
    ['Thom Tillis', 'North Carolina', 'R'], ['James Lankford', 'Oklahoma', 'R'], ['Mike Rounds', 'South Dakota', 'R'], ['Shelley Moore Capito', 'West Virginia', 'R']]


# Create files
f1 = open("senate113.txt", 'wb')
pickle.dump(senate113, f1)
f1.close()

f2 = open("RetiredSen.txt", 'wb')
pickle.dump(retiredSen, f2)
f2.close()

f3 = open("NewSen.txt", 'wb')
pickle.dump(newSen, f3)
f3.close()


# -----A------ #


def mainA():
    sen113, retSen, newMem = readFiles()
    remaining113 = compare113(sen113, retSen)
    sen114 = newSenate(remaining113, newMem)
    senate114 = createSen114(sen114)
    
    return senate114

# Open file
def readFiles():
    rf1 = open("senate113.txt", 'rb')
    sen113 = pickle.load(rf1)
    rf1.close()

    rf2 = open("Retiredsen.txt", 'rb')
    retSen = pickle.load(rf2)
    rf2.close()

    rf3 = open("NewSen.txt", 'rb')
    newMem = pickle.load(rf3)
    rf3.close()

    return sen113, retSen, newMem

# Remove retired senators from nested list
def compare113(sen113, retSen):
    i = 0
    l = len(retSen) - 1

    while i <= l:
        if retSen[i] in sen113:
            num = sen113.index(retSen[i])
            sen113.pop(num)
            i += 1
        else:
            i += 1
    
    remaining113 = sen113

    return remaining113

# Add new senators to remainging senators list to create 114th senate and sort by state
def newSenate(remaining113, newMem):
    newMemTot = len(newMem)
    sen114 = remaining113
    i = 0

    for i in range(newMemTot):
        sen114.append(newMem[i])

    sen114.sort(key = lambda x: x[1])

    return sen114
    
# Create new senate 114 file
def createSen114(sen114):
    f = open("senate114.txt", 'wb')
    pickle.dump(sen114, f)
    f.close()

    r = open("senate114.txt", 'rb')
    senate114 = pickle.load(r)
    r.close()

    return senate114


# -----B------ #


def mainB():
    mainA()
    senate114 = mainA()
    democrat, republican, independant = partyCount(senate114)
    partyOutput(democrat, republican, independant)

# Count number of senators per party
def partyCount(senate114):
    democrat = 0
    republican = 0
    independant = 0
    l = len(senate114)
    i = 0

    for i in range(l):
        if 'D' in senate114[i]:
            democrat += 1
        elif 'R' in senate114[i]:
            republican += 1
        elif 'I' in senate114[i]:
            independant += 1
    
    return democrat, republican, independant

# Display output
def partyOutput(democrat, republican, independant):
    print("Party Affiliations")
    print("  Republican: {0}\n  Democrat: {1}\n  Independant: {2}\n".format(republican, democrat, independant))


# -----C------ #


def mainC():
    mainB()
    senate114 = mainA()
    sameParty = sameAffiliation(senate114)
    statesOutput(sameParty)

# Count states where senators are the same party
def sameAffiliation(senate114):
    sharedParty = 0
    l = len(senate114) - 1
    i = 0

    for i in range(l):
        if senate114[i][1] == senate114[i + 1][1]:
            sharedParty += 1

    sameParty = sharedParty / 2

    return int(sameParty)

def statesOutput(sameParty):
    print("Number of states whose two senators have the same party affiliation: {0}\n".format(sameParty))


# -----D------ #


def mainD():
    mainC()
    senate114 = mainA()
    state = userState()
    num = stateNum(state)
    senator1, senator2 = stateCount(num, senate114)
    senatorOutput(state, senator1, senator2)

# Request user enter a state and converts to title case
def userState():
    state = input("Enter a state: ")
    state = state.title()

    return state

# Finds index number based on user input
def stateNum(state):
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
        "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", 
        "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
        "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    num = states.index(state)
    num = num * 2

    return num

# Finds nested lists containing state
def stateCount(num, senate114):
    stateCount = 0
    senators = []
    l = len(senate114)
    i = 0

    senator1 = senate114[num][0]
    senator2 = senate114[num + 1][0]

    return senator1, senator2

# Output senator names for user selected state
def senatorOutput(state, senator1, senator2):
    print("Enter the name of a state: {0}".format(state))
    print("{0}\n{1}".format(senator1, senator2))


mainD()
