def kaprekarNumbers(p, q):
    res = []
    for i in range(p, q + 1):
        s = str(i * i)
        if int(s[:len(s) // 2] or 0) + int(s[len(s) // 2:]) == i:
            res.append(i)
    if res:
        print(' '.join(map(str, res)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
