def makingAnagrams(s1, s2):
    u = set(s1).union(set(s2))
    res = 0
    for i in u:
        res += abs(s1.count(i) - s2.count(i))
    return res


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(str(result) + '\n')
