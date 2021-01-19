def birthday(s, d, m):
    res = 0
    for i in range(len(s) - m + 1):
        som = 0
        for j in range(m):
            som += s[i + j]
        if som == d:
            res += 1
    return res


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
