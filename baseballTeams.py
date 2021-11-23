#Baseball - Write a program to use the file to produce a text file containing the information. In the new file, the baseball teams should be in descending order 
#by the percentage of games won.

# Import library
import pickle

# Define dictionary
baseball = {"Baltimore" : {"Won" : 96, "Lost" : 66}, "Boston" : {"Won" : 71, "Lost" : 91}, "New York" : {"Won" : 84, "Lost" : 78}, 
    "Tampa" : {"Won" : 77, "Lost" : 85}, "Toronto" : {"Won" : 83, "Lost" : 79}}

# Create file
cf = open("ALE.txt", 'wb')
pickle.dump(baseball, cf)
cf.close()

# ------------ #

def main():
    teams = readFile()
    newDict = pctCalc(teams)
    teamsSorted = sortList(newDict)
    writeFile(teamsSorted)

# Open & read file
def readFile():
    rf = open("ALE.txt", 'rb')
    teams = pickle.load(rf)
    rf.close()
    return teams

# Calculations
def pctCalc(teams):
    for k in teams:
        percent = "{0:10.4}".format(teams[k]["Won"] / (teams[k]["Won"] + teams[k]["Lost"]))
        teams[k].update(Pct= float(percent))
        newDict = teams
    return newDict

# Sort list
def sortList(newDict):
    teamsSorted = sorted(teams.items(), key = lambda x: x[1]['Pct'], reverse = True)
    return teamsSorted

# Write file
def writeFile(teamsSorted):
    wf = open("ALE2.txt", 'wb')
    pickle.dump(teamsSorted, wf)
    wf.close()


# Run
main()

rfin = open("ALE.txt", 'rb')
final = pickle.load(rfin)
rfin.close()

print(final)
