def countingValleys(steps, path):
    res = 0
    lvl = 0
    for s in path:
        if s == 'U':
            lvl += 1
            if lvl == 0:
                res += 1
        else:
            lvl -= 1
    return res


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result) + '\n')
