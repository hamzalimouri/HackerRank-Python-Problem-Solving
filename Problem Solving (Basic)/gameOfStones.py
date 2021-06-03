def gameOfStones(n):
    return 'First' if n % 7 >= 2 else 'Second'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        print(result)
