def flatlandSpaceStations(n, c):
    c.sort()
    res = max(c[0], n - 1 - c[-1])
    for i in range(1, len(c)):
        res = max(res, (c[i] - c[i - 1]) // 2)
    return res


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result))
