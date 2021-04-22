def happyLadybugs(b):
    for c in set(b.replace("_", "")):
        if b.count(c) == 1:
            return "NO"
    if "_" not in b:
        for i in range(1, len(b) - 1):
            if b[i - 1] != b[i] and b[i + 1] != b[i]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result + '\n')
