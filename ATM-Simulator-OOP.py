# Ayoola Abimbola


'''
OOP version of the ATM homework
'''

class ATM():
    def __init__(self, name=""):
        self.name = name
        self.option = "0"

    def menu(self):
        print('\n{}:\n1: Deposit\n2: Withdrawal\n3: Check Bal\n4: Quit\n'.format(self.name))
        while True:
            option = int(input('Enter number: '))

            if option in [1, 2, 3, 4]:
                return option
            else:
                print('Number must be between 1 - 4')


class Customer:
    def __init__(self, fname="", key=""):
        self.fname = fname
        self.key = key
        self.accountsDB = {}
        self.amount = 0

        infile = open(self.fname, "r")

        for line in infile:
            userData = line[:-1].split(',')
            self.accountsDB[userData[0]] = [userData[1], userData[2], float(userData[3])]
        infile.close()

    def getAccounts(self):
        return self.accountsDB

    def getUser(self):
        return self.accountsDB[self.key]

    def getAmount(self):
        while True:
            try:
                self.amount = float(input('Amount: '))
                return self.amount
            except ValueError:
                print('Please enter valid amount.')

    def deposit(self):
        # key = self.key
        self.accountsDB[self.key][2] += self.amount
        print("Account updated")

    def withdraw(self):
        # key = self.key
        while True:
            if self.accountsDB[self.key][2] - self.amount < 0:
                print('\nInsufficient funds to complete the transaction!!')
                return
            else:
                self.accountsDB[self.key][2] -= self.amount
                print("Account updated")
                return

    def getBalance(self, username=""):
        print("Hi {}! Your current balance is ${:.2f}".format(username, self.accountsDB[self.key][2]))


if __name__ == '__main__':
    pin = input("Enter pin code: ")
    # file = input("Enter file name: ")
    file = "accounts.csv"

    while pin != '':
        user = Customer(file, pin)
        details = user.getUser()
        name = details[0] + " " + details[1]
        runATM = ATM(name)

        while True:
            choice = runATM.menu()
            if choice == 1:
                user.getAmount()
                user.deposit()
            elif choice == 2:
                user.getAmount()
                user.withdraw()
            elif choice == 3:
                user.getBalance(name)
            else:
                print("Goodbye\n")
                break
        pin = input("Enter pin code (return to quit): ")
