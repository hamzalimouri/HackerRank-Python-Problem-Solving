def marsExploration(s):
    res = 0
    for i in range(0, len(s), 3):
        if s[i] != "S":
            res += 1
        if s[i + 1] != "O":
            res += 1
        if s[i + 2] != "S":
            res += 1
    return res


if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(str(result) + '\n')
