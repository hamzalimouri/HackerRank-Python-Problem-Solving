# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ar = [0, 0]
    for i in range(3):
        if a[i] < b[i]:
            ar[1] += 1
        elif a[i] > b[i]:
            ar[0] += 1
    return ar


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
