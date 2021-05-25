def minimumAbsoluteDifference(arr):
    arr.sort()
    return min([abs(arr[i] - arr[i - 1]) for i in range(1, len(arr))])


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result))
