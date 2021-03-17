def repeatedString(s, n):
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
