def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApples, countOranges = 0, 0
    for apple in apples:
        if s <= apple + a <= t:
            countApples += 1
    for orange in oranges:
        if s <= orange + b <= t:
            countOranges += 1
    print(countApples, countOranges, sep='\n')


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
