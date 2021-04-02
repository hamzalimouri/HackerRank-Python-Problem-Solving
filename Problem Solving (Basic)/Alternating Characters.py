def alternatingCharacters(s):
    res = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            res += 1
    return res


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result))
