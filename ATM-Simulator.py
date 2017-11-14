# Ayoola Abimbola


'''
List of functions:
startup(fname)
getUser(proceed, dictionary)
menu(name)
getAmount()
deposit(balance)
withdraw(balance)
balance(name, balance):
main()
'''

### Problem 2

def startup(fname):
    accountsDB = {}

    while True:
        try:
            infile = open(fname, 'r')
        except FileNotFoundError:
            print('Cannot get to the file')
            return

        try:
            for line in infile:
                userData = line[:-1].split(',')
                accountsDB[userData[0]] = [userData[1], userData[2], float(userData[3])]
            infile.close()
            return True, accountsDB
        except IndexError:
            print('Invalid data format')
            return False, accountsDB
        except:
            return False, accountsDB


### Problem 3
def getUser(proceed, dictionary):
    pinCode = input('Welcome -- Please enter pin code: ')

    for pin, user in dictionary.items():
        if pin == pinCode:
            return user, proceed
        else:
            pass
    print('Incorrect pin')
    return None, False


### Problem 4
def menu(name):
    print('\n{}:\n1: Deposit\n2: Withdrawal\n3: Check Bal\n4: Quit\n'.format(name))

    while True:
        try:
            option = int(input('Enter number: '))

            if option in [1, 2, 3, 4]:
                return option
            else:
                print('Number must be between 1 - 4')
        except ValueError:
            print('Only digits from 1 - 4 allowed')


### Problem 6
def getAmount():
    while True:
        try:
            amount = float(input('Amount: '))
            return amount
        except ValueError:
            print('Please enter valid amount.')


### Problem 5
def deposit(balance):
    amount = getAmount()
    newBalance = balance + amount
    print('Your new balance is ${}\n'.format(round(newBalance, 2)))
    return newBalance


### Problem 7
def withdraw(balance):
    # amount = getAmount()
    while True:
        amount = getAmount()
        newBalance = balance - amount
        if newBalance >= 0:
            print('Your new balance is ${}'.format(round(newBalance, 2)))
            return newBalance
        else:
            print('\nInsufficient funds to complete the transaction\n\nPlease enter new amount to withdraw.')


### Problem 8
def balance(name, balance):
    print('Hi {}! Your current balance is ${}'.format(name, round(balance, 2)))


### Problem 1
def main():
    proceed, dictionary = startup('accounts.csv')  # DB reader and Dict maker

    if proceed is False:
        print('Unable to read data file')
        return

    user, proceed = getUser(proceed, dictionary)  # User data saved here
    if proceed is False:
        return

    firstName = user[0]  # User first name
    lastName = user[1]  # User last name
    fullName = firstName + lastName
    balanceDB = user[2]  # User account balance

    while True:  # User options called here
        option = menu(firstName)
        if option == 1:
            newBalance = deposit(balanceDB)
            balanceDB = newBalance
        elif option == 2:
            newBalance = withdraw(balanceDB)
            balanceDB = newBalance
        elif option == 3:
            balance(fullName, balanceDB)
        else:
            print('Goodbye')
            return


#main()
