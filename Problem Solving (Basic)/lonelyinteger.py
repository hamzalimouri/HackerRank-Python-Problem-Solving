def lonelyinteger(a):
    for i in set(a):
        if a.count(i) == 1:
            return i


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result))
