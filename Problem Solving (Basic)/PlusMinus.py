def plusMinus(arr, l):
    p, n = 0, 0
    for i in arr:
        if i < 0:
            n += 1
        elif i > 0:
            p += 1
    print(round(p / l, 6))
    print(round(n / l, 6))
    print(round((l - (n + p)) / l, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
