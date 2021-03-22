def runningTime(arr):
    res = 0
    for i in range(len(arr)):
        j = i - 1
        while (j >= 0) and (arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            i = j
            j -= 1
            res += 1
    return res


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    print(str(result) + '\n')
