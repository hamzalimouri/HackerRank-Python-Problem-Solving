def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(simpleArraySum(ar))
