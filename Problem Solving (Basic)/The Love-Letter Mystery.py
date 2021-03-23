def theLoveLetterMystery(s):
    res = 0
    if s != s[::-1]:
        l = len(s) // 2
        for i in range(l):
            res += abs(ord(s[i]) - ord(s[i * -1 - 1]))
    return res


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result) + '\n')
