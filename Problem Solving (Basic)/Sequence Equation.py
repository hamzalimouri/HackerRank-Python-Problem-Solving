def permutationEquation(p):
    res = []
    for i in range(1, len(p) + 1):
        d = p.index(i) + 1
        res.append(p.index(d) + 1)
    return res


if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))
    print('\n')
