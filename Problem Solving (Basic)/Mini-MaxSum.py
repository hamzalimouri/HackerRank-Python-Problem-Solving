def miniMaxSum(arr):
    m = min(arr)
    M = max(arr)
    s = sum(arr)
    print(s - M, s - m)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
