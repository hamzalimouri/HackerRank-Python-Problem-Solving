def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(len(ar) - 1):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                res += 1
    return res


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')
