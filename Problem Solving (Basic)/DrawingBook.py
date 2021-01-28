def pageCount(n, p):
    s = n // 2
    d = p // 2
    return min(s - d, d)


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')
