def vowels(s):
    n = len(s)
    v = 'aeiouAEIOU'

    if n == 0:
        c = 0
        return c
    else:
        if s[n-1:n] in v:
            c = 1
        else:
            c = 0
        return c + vowels(s[:n - 1])

        # d = vowels(s[:n-1])
        # c = c + d
        # return c



def vowels2(s):
    n = len(s)
    v = 'aeiouAEIOU'
    if n == 0:
        return 0
    elif s[n-1:n] in v:
        c = 1
    else:
        c = 0
    return c + vowels(s[:n - 1])


def main():
    word = 'My name is'
    print(vowels2(word))


main()
