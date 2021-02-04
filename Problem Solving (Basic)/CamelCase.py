def camelcase(s):
    res = 0
    if s:
        res += 1
        for i in s[1:]:
            if "A" <= i <= "Z":
                res += 1
    return res


if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(str(result) + '\n')
