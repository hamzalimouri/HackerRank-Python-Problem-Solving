def maximizingXor(l, r):
    res = 0
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            if i ^ j > res:
                res = i ^ j
    return res


if __name__ == '__main__':
    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    print(str(result))
