class SavingsAccount:
    def __init__(self, name, balance):
        self._name = name 
        self._balance = balance 
    
    def makeDeposit(self, balance, deposit):
        endBalance = balance + deposit

        return endBalance

    def makeWithdrawal(self, balance, withdraw):
        if balance >= withdraw:

            endBalance = balance - withdraw

            return endBalance

        else:
            trigger = False

            return trigger

            

def transaction():
    name = userName()
    actionAmount(name)


def userName():
    name = input("Enter person's name: ")
    name = name.title()

    print("Enter person's name: {0}".format(name))
    print("D = Deposit, W = Withdrawal, Q = Quit")

    return name

def actionType():
    action = None
    action = str(input("Enter D, W, or Q: "))
    action = action.title()

    print("Enter D, W, or Q: {0}".format(action))

    return action

def actionAmount(name):
    carryOn = True
    balance = 0

    while carryOn == True:
        action = actionType()
        if action == 'D':
            deposit = int(input("Enter amount to deposit: "))

            print("Enter amount to deposit: {0}".format(deposit))

            balance = SavingsAccount.makeDeposit(name, balance, deposit)

            print("Balance: ${0}".format(balance))

            pass

        elif action == 'W':
            totBalance = balance
            withdraw = int(input("Enter amount to withdraw: "))

            print("Enter amount to withdraw: {0}".format(withdraw))

            balance = SavingsAccount.makeWithdrawal(name, balance, withdraw)

            if type (balance) == int:
                print("Balance: ${0}".format(balance))

            else:
                print("Insufficient funds, transaction denied.")
                balance = totBalance
                print("Balance: ${0}".format(balance))

            pass

        else:
            print("End of transaction. Have a good day {0}.".format(name))
            carryOn == False   

            return carryOn     


transaction()
