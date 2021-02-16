def jumpingOnClouds(c, k):
    res = 100
    i = k % n
    res -= c[i] * 2 + 1
    while i:
        i = (i + k) % n
        res -= c[i] * 2 + 1
    return res


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result) + '\n')
