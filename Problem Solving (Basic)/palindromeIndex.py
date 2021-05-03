def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    temp = s[:i] + s[i + 1:]
    if temp == temp[::-1]:
        return i
    temp = s[:j] + s[j + 1:]
    if temp == temp[::-1]:
        return j


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(str(result))
