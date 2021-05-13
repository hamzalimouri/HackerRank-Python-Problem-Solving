def closestNumbers(arr):
    arr_set = list(set(arr))
    arr_set.sort()
    c = arr_set[1] - arr_set[0]
    res = [arr_set[0], arr_set[1]]
    for i in range(1, len(arr_set) - 1):
        temp = arr_set[i + 1] - arr_set[i]
        if c > temp:
            c = temp
            res.clear()
            res.append(arr_set[i])
            res.append(arr_set[i + 1])
        elif c == temp:
            res.append(arr_set[i])
            res.append(arr_set[i + 1])

    return res


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(' '.join(map(str, result)))
