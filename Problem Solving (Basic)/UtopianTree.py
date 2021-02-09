def utopianTree(n):
    res = 1
    for i in range(n):
        if i % 2 == 0:
            res *= 2
        else:
            res += 1
    return res


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result) + '\n')
