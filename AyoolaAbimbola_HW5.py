# Ayoola Abimbola
# HW5

'''
List of functions:
    squareQuads(n) - 'n' must always be odd
    squareDiagonals(n) - 'n' must always be odd
    squareTriangle(n) - 'n' must always be odd
    columnSum(lst) - lst must be a multi-dimensional list
    numLoops() - Resolve the number of iterations required to reach '1'. (From a predetremined calculation)
    numLetters() - Returns the percentage of 3-letter words from a series of inputted words by user
'''

### Problem 1

def squareQuads(n):
    n2 = (n // 2)

    if n % 2 == 0:
        print('\'n\' must be an odd number')
        return

    print('Quadrants')

    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == n2) or (i == n - 1) or (j == 0) or (j == n2) or (j == n - 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    return


def squareDiagonals(n):
    if n % 2 == 0:
        print('\'n\' must be an odd number')
        return

    print('Diagonals')

    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == n - 1) or (j == 0) or (j == n - 1) or (i == j) or (i + j == n - 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    return


def squareTriangle(n):
    if n % 2 == 0:
        print('\'n\' must be an odd number')
        return

    print('Inner triangle')

    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == n - 1) or (j == 0) or (j == n - 1) or (i + j <= n - 1) and i != 1 and j != 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    return


### Problem 2

def columnSum(lst):
    for i in lst:
        if len(i) != len(lst):
            print('Number of sublists != length of each sublist. Check your input!')
            return
        
    cSum = []
    for i in range(len(lst)):
        cSum.append(0)

    for row in range(len(lst)):
        for col in range(len(lst)):
            cSum[col] += lst[row][col]
    #print(cSum)
    return cSum


### Problem 3

# Algorithm
# - Define function 'numLoops'
# - Accept user input as int 'z'
# - check if 'z' is not a negative number
# - Loop trough calculations until z == 1 using while & If-Else


def numLoops():
    z = int(input('Enter a positive integer: '))
    c = 0

    if z < 0:
        return 'Input must be a positive integer'

    while z:
        if int(z / 2) == z / 2:
            z = z / 2
            c += 1
        else:
            z = (z * 3) + 1
            c += 1
        if z == 1:
            break
    return 'number of iterations to reach 1 is: ' + str(c)


# Test Data and Results

# Input = 9
# Number of iterations = 19

# Input = 21
# Number of iterations = 7

# Input = 27
# Number of iterations = 111


### Problem 4

def numLetters():
    word = input('Enter a word to begin (return to exit): ')

    if len(word) == 0:
        # return 'At least one word required'
        return 'Exit'

    wordsCount3 = 0
    wordsCountT = 0

    while word:
        if len(word) == 0:
            wordsCountT += 1
            break
        else:
            if len(word) == 3:
                wordsCount3 += 1
                wordsCountT += 1
            else:
                wordsCountT += 1
        word = input('Enter another word (return to exit): ')

    wordPercent3 = round((wordsCount3 / wordsCountT) * 100, 2)
    return 'Percent of 3-letter words is {}%'.format(wordPercent3)



