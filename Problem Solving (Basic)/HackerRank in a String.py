def hackerrankInString(s):
    c = "hackerrank"
    j = 0
    for i in s:
        if j < len(c) and i == c[j]:
            j += 1
            if j == len(c):
                return "YES"
    return "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result + '\n')