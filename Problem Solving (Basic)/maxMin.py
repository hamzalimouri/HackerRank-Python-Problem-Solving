def maxMin(k, arr):
    arr.sort()
    res = arr[k - 1] - arr[0]
    for i in range(1, len(arr) - k + 1):
        res = min(res, arr[k + i - 1] - arr[i])
    return res


if __name__ == '__main__':
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
