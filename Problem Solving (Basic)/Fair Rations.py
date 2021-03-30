def fairRations(B):
    s = sum(B)
    if s % 2:
        return "NO"
    else:
        res = 0
        for i in range(len(B)):
            if B[i] % 2:
                B[i] += 1
                B[i + 1] += 1
                res += 2
    return str(res)


if __name__ == '__main__':
    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result + '\n')
