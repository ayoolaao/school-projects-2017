def digiSum(n):
    if n < 10:
        x = n
        return x
    else:
        # x = n % 10
        # y = digiSum(n // 10)
        #
        # x = x + y

        # return x

        return (n % 10) + digiSum(n // 10)


def main():
    number = 900
    print(digiSum(number))


main()
