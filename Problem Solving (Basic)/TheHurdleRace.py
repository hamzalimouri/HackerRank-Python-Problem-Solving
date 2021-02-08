def hurdleRace(k, height):
    m = max(height)
    return 0 if m < k else m - k


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result) + '\n')
