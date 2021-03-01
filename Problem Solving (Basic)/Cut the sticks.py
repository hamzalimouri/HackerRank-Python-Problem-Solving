def cutTheSticks(arr):
    l = len(arr)
    res = []
    while l:
        res.append(l)
        m = min(arr)
        arr = [i - m for i in arr if i - m > 0]
        l = len(arr)
    return res


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
