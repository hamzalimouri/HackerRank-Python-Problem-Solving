def chocolateFeast(n, c, m):
    w = n // c
    res = w
    while w >= m:
        temp = (w // m)
        res += temp
        w = w % m + temp
    return res


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        print(str(result) + '\n')
