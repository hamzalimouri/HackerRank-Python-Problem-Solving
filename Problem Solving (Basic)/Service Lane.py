def serviceLane(width, cases):
    res = []
    for case in cases:
        res.append(min(width[case[0]: case[1] + 1]))
    return res


if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    print('\n'.join(map(str, result)))
    print()
