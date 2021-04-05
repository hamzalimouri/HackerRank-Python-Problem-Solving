def jumpingOnClouds(c):
    res = 0
    i = 0
    while i < len(c) - 1:
        if c[i] == 0:
            if i < len(c) - 2 and c[i + 2] == 0:
                i += 1
            res += 1
        i += 1

    return res


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
