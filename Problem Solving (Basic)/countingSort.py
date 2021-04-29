def countingSort(arr):
    tab = [0] * (max(arr) + 1)
    for i in arr:
        tab[i] += 1
    res = []
    for i in range(len(tab)):
        if tab[i]:
            for _ in range(tab[i]):
                res.append(i)
    return res


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
