def superReducedString(s):
    r = ""
    for i in s:
        if r == "" or i != r[-1]:
            r += i
        else:
            r = r[:-1]
    if len(r) == 0:
        return "Empty String"
    return r


if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result + '\n')
