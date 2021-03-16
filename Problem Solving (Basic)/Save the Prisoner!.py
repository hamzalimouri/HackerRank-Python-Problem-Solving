def saveThePrisoner(n, m, s):
    return (m + s - 2) % n + 1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(str(result) + '\n')
