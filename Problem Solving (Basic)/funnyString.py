def funnyString(s):
    a = [ord(x) for x in s]
    b = [ord(x) for x in s[::-1]]
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) != abs(b[i] - b[i + 1]):
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result + '\n')
