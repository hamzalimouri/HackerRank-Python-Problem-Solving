def quickSort(arr):
    p = arr[0]
    l = []
    r = []
    e = [p]
    for i in arr[1:]:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
        else:
            e.append(i)
    return l + e + r


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(' '.join(map(str, result)))
