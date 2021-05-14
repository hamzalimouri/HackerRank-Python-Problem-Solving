def countSort(arr):
    res = {}
    l = len(arr) // 2
    for i in range(len(arr)):
        e = arr[i]
        if int(e[0]) not in res:
            res[int(e[0])] = []
        res[int(e[0])].append('-'if i < l else e[1])
    for k in sorted(res.keys()):
        for s in res[k]:
            print(s, end=' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
