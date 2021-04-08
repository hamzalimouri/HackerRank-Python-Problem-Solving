def howManyGames(p, d, m, s):
    count = 0
    res = 0
    while count + p <= s:
        res += 1
        count += p
        p -= d
        if p < m:
            p = m
    return res


if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(str(answer) + '\n')
