#!/bin/python3
import math


def workbook(n, k, arr):
    res = 0
    page = 1
    i = 0
    for i in arr:
        temp = math.ceil(i / k)
        for j in range(1, temp):
            if (j - 1) * k < page <= j * k:
                res += 1
            page += 1
        if (temp - 1) * k < page <= i:
            res += 1
        page += 1
    return res


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(str(result) + '\n')
