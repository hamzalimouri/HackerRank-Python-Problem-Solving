def beautifulDays(i, j, k):
    res = 0
    for n in range(i, j + 1):
        x = int(str(n)[::-1])
        if abs(n - x) % k == 0:
            res += 1
    return res


if __name__ == '__main__':
    i, j, k = [int(x) for x in input().split()]

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')
