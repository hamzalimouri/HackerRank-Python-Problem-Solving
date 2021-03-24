def beautifulTriplets(d, arr):
    res = 0
    for i in arr:
        if i + d in arr and i + 2 * d in arr:
            res += 1
    return res


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')
