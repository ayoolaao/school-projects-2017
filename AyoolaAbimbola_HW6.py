# Ayoola Abimbola


'''
List of functions:
    index(fname, letter) - accepts filename and letter as args
    rollDice() and crap()
    STUDENT()
'''

### Problem 1

from string import punctuation


def index(fname, letter):
    totalLines = len(open(fname, 'r').readlines()) - 1
    infile = open(fname, 'r')

    wordCount = 0
    lineNumber = 0

    storageDict = {}
    letter = letter.lower()

    space = ' ' * len(punctuation)
    transTable = str.maketrans(punctuation, space)

    while lineNumber <= totalLines:
        line = infile.readline()
        line = line.lower()
        line = line.translate(transTable)
        lineNumber += 1
        line = line.split()

        for word in line:
            if word[0] == letter:
                if word not in storageDict:
                    wordCount += 1
                    storageDict[word] = [lineNumber]
                else:
                    wordCount += 1
                    storageDict[word] = storageDict[word] + [lineNumber]

    infile.close()

    for key, value in sorted(storageDict.items()):
        value = set(value)
        value = list(value)
        value = sorted(value)
        print('{:20}{}'.format(key, str(value)[1:-1]))

    print()
    print('There are {} lines in the book.'.format(lineNumber))
    print('There are {} words that begin with "{}".'.format(wordCount, letter))

    return
'''
#filename = 'Pride_and_Prejudice.txt'
filename = 'The_Tempest.txt'
let = 'a'
index(filename, let)
'''


### Problem 2

from random import randint


def rollDice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1 + die2


def crap():
    status = {
        'I win': (7, 11),
        'I lose': (2, 3, 12)
    }

    initialRoll = rollDice()
    print(initialRoll)

    for k, v in status.items():
        if initialRoll in v:
            print(k)
            return

    status['I win'] = initialRoll
    status['I lose'] = 7

    while True:
        # print(status)
        roll = rollDice()
        print(roll)

        for k, v in status.items():
            if roll == v:
                print(k)
                return


#crap()


### Problem 3

def STUDENT():
    studentRecords = {}

    while True:
        firstName = input('First name: ')
        if firstName == '':
            break

        lastName = input('Last name: ')
        if lastName == '':
            lastName = input('Last name is required. (return again to quit program):')
            if lastName == '':
                break

        name = (lastName, firstName)

        if name in studentRecords:
            update = input('{} has ID {}. Update? (y or n): '.format(name, studentRecords[name]))
            if update == 'y' or update == 'Y' or update == 'yes' or update == 'YES' or update == 'Yes':
                studentRecords[name] = input('Student ID: ')
            else:
                continue
        else:
            studentID = input('Student ID: ')
            if len(studentID) != 7:
                studentID = input('Re-enter Student ID (must be 7-digits): ')
                if studentID == '':
                    break
            studentRecords[name] = studentID

    print('\nContents of dictionary:')
    if studentRecords == {}:
        print('There is no record')
    else:
        for k, v in studentRecords.items():
            print('{}, {} has studentID {}'.format(k[0], k[1], v))

    return


#STUDENT()
