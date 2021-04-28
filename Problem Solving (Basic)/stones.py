def stones(n, a, b):
    res = set()
    l = n - 1
    i = 0
    while i < n:
        res.add(a * (l - i) + b * i)
        i += 1
    return sorted(res)


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
