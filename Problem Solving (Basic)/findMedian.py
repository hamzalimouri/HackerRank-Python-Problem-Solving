import math


def findMedian(arr):
    return sorted(arr)[math.ceil(len(arr) / 2) - 1]


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(str(result) + '\n')
