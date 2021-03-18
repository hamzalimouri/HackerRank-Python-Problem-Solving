def minimumDistances(a):
    for d in range(1, n):
        for i in range(n - d):
            if a[i] == a[i+d]:
                return d
    return -1


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
