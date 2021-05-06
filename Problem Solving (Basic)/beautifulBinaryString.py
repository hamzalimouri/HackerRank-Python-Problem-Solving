def beautifulBinaryString(b):
    res = 0
    while 1:
        temp = b.find('010')
        if temp == -1:
            break
        res += 1
        b = b[temp + 3:]

    return res


if __name__ == '__main__':
    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    print(str(result))
