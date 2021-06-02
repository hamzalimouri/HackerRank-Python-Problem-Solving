def maximumPerimeterTriangle(sticks):
    sticks.sort()
    i = len(sticks) - 1
    while i >= 2 and sticks[i - 2] + sticks[i - 1] <= sticks[i]:
        i -= 1
    if i >= 2:
        return sticks[i - 2: i + 1]
    return [-1]


if __name__ == '__main__':
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(' '.join(map(str, result)))
