def extraLongFactorials(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    print(res)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
