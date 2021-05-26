def luckBalance(k, contests):
    contests.sort(reverse=True)
    res = 0
    for contest in contests:
        if contest[1] == 0:
            res += contest[0]
        elif k > 0:
            res += contest[0]
            k -= 1
        else:
            res -= contest[0]
    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result))
