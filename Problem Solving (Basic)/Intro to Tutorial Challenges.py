def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    print(str(result) + '\n')
