class Employee:
    def __init__(self, name, rateOfPay, hoursWorked):
        self._name = name 
        self._rateOfPay = rateOfPay
        self._hoursWorked = hoursWorked

class SalariedEmployee(Employee):
    def calcPay(rateOfPay):
        totPay = rateOfPay

        return totPay

class HourlyEmployee(Employee):
    def calcPay(rateOfPay, hours):
        totPay = hours * rateOfPay

        return totPay


def payroll():
    listEmp = []
    userInput(listEmp)

def cont(listEmp):
    decision = input("Do you want to continue (Y/N)?: ")
    decision = decision.title()

    if decision == 'Y':
        print("Do you want to continue (Y/N)?: {}".format(decision))
        userInput(listEmp)
    else:
        print("Do you want to continue (Y/N)?: {}".format(decision))
        result(listEmp)

def userInput(listEmp):
    name = input("Enter employees's name: ")
    name = name.title()
    print("Enter employees's name: {}".format(name))

    classification = input("Enter employee's classification (Salaried or Hourly): ")
    classification = classification.title()
    print("Enter employee's classification (Salaried or Hourly): {}".format(classification))

    hours = int(input("Enter the number of hours worked: "))
    print("Enter the number of hours worked: {}".format(hours))
    rateOfPay = 0

    if classification == 'Salaried':
        rateOfPay = int(input("Enter weekly salary: "))
        print("Enter weekly salary: {}".format(rateOfPay))
        rateOfPay = SalariedEmployee.calcPay(rateOfPay)
    else:
        rateOfPay = int(input("Enter hourly wage: "))
        print("Enter hourly wage: {}".format(rateOfPay))
        rateOfPay = HourlyEmployee.calcPay(rateOfPay, hours)

    user = [name, classification, hours, rateOfPay]
    listEmp.append(user) 
        
    cont(listEmp)

def result(listEmp):
    numSalaried = 0
    totalPayroll = 0
    totalHours = 0
    l = len(listEmp)

    for i in range(l):
        totalHours += listEmp[i][2]
        totalPayroll += listEmp[i][3]

        if listEmp[i][1] == 'Salaried':
            numSalaried += 1

    for i in range(l):
        print("{0}: ${1:,.2f}".format(listEmp[i][0], listEmp[i][3]))
    print("Number of employees: {0}".format(l))
    print("Number of salaried employees: {0}".format(numSalaried))
    print("Total payroll: ${0:,.2f}".format(totalPayroll))
    print("Average number of hours worked per employee: {0:.2f}".format(totalHours / l))



payroll()
