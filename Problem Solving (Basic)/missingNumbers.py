def missingNumbers(arr, brr):
    res = []
    for x in set(brr):
        if brr.count(x) > arr.count(x):
            res.append(x)
    return res


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
