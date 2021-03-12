def getMoneySpent(keyboards, drives, b, n, m):
    keyboards.sort()
    drives.sort()
    i = 0
    res = -1
    j = m - 1
    while j >= 0:
        while i < n:
            if keyboards[i] + drives[j] > b:
                break
            if keyboards[i] + drives[j] > res:
                res = keyboards[i] + drives[j]
            i += 1
        j -= 1
    return res


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b, n, m)

    print(str(moneySpent) + '\n')
