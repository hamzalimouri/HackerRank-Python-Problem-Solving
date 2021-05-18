def anagram(s):
    if len(s) % 2:
        return -1
    l = len(s) // 2
    res = 0
    for x in set(s[l:]):
        temp = s[l:].count(x) - s[:l].count(x)
        res += temp if (temp > 0) else 0
    return res


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result))
