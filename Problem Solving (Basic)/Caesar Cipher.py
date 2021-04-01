def caesarCipher(s, k):
    res = []
    for i in s:
        if "A" <= i <= "Z":
            res.append(chr(65 + (ord(i) + k - 65) % 26))
        elif "a" <= i <= "z":
            res.append(chr(97 + (ord(i) + k - 97) % 26))
        else:
            res.append(i)
    return "".join(res)


if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')
