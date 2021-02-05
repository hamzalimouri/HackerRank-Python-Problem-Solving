NUMBERS = "0123456789"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    d = {'n': 0, 'l': 0, 'u': 0, 's': 0}
    for i in password:
        if i in NUMBERS:
            d['n'] += 1
        elif i in LOWER_CASE:
            d['l'] += 1
        elif i in UPPER_CASE:
            d['u'] += 1
        else:
            d['s'] += 1
    res = 0
    for _, i in d.items():
        if i == 0:
            res += 1
    if len(password) < 6:
        return max(6 - len(password), res)
    return res


if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')
