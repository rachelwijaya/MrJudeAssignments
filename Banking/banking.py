#15 OCTOBER 2019
#Object Oriented Programming Paradigm
class Account:  #name classes starting with a capital letter, naming convention
    __balance = 0 #making it private

    def __init__(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt < self.__balance:
            self.__balance -= amt
            return True
        else:
            return False


class Customer:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__account = self.setAccount

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccount(self):
        return self.__account

    def setAccount(self, acct):
        self.__account = acct

class Bank:
    __customers = ""
    customerList = []
    __numCustomers = 0
    __bankName = ""

    def __init__(self, bankName):
        self.__bankName = bankName
        self.__numCustomers = len(customerList)
        self.__customers = myCustomer
        self.__customerList = []

    def bankName(self):
        return self.__bankName

    def addCustomer(self,myCustomer):
        customerList.append(myCustomer)

    def numofCustomers(self):
        return self.__numCustomers

    def getCustomer(self, myCustomer):
        return customerList.index(myCustomer)

#myCustomer.setAccount(Account(500))

def bankerMenu():
    print("----------------BANKER MENU----------------")
    print("1. Add new customer")
    print("2. Customer's index")
    print("3. Get number of customers")
    print("4. Exit")
    choice = input("Which option would you like? ")

    loop = True
    while loop:
        if choice == 1:
            try:
                firstName = str(input("Enter first name: "))
                lastName = str(input("Enter last name: "))
            except TypeError:
                print("Please try again.")
                bankerMenu()
            else:
                myCustomer = Customer(firstName, lastName)
                myCustomer.addCustomer(myCustomer)

        elif choice == 2:
            try:
                index = int(input("Enter index number: "))
            except TypeError:
                print("enter a number")
                bankerMenu()
            else:
                Bank.getCustomer(index)
        elif choice == 3:
            Bank.numofCustomers()
        elif choice == 4:
            loop = False
        else:
            print("Try again.")
            bankerMenu()
def customerMenu():
    print("----------------CUSTOMER MENU----------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Which option would you like? ")
    loop = True
    while loop:
        if choice == 1:
            deposit = int(input("Enter the amount you would like to deposit: "))
            myFC.Account.deposit(deposit)
        elif choice == 2:
            withdraw = int(input("Enter the amount you would like to withdraw: "))
            myFC.Account.withdraw(withdraw)
        elif choice == 3:
            print(myFC.Account.getBalance())
        elif choice == 4:
            loop = False


myFC = Customer("Rachel", "Wijaya")
myFC.setAccount(Account(5000))
#print(myFC.getAccount().getBalance())
#myAccount = Account(5000)
#myAccount.withdraw(100)
def main():
    bankName = str(input("Enter name of bank: "))
    print("Welcome to " + bankName + "!")
    person = input("Are you a customer or an employee?")
    person = person.lower()
    if person == "employee":
        bankerMenu()
    elif person == "customer":
        customerMenu()
    else:
        print("Please make sure your input is correct.")
        main()

main()