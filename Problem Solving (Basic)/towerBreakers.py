def towerBreakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(str(result))
