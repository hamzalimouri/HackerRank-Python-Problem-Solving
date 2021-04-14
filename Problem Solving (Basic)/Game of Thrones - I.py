def gameOfThrones(s):
    s_set = set(s)
    temp = 0
    for i in s_set:
        if s.count(i) % 2:
            temp += 1
        if temp >= 2:
            return "NO"
    return "YES"


if __name__ == '__main__':
    s = input()

    result = gameOfThrones(s)

    print(result + '\n')
