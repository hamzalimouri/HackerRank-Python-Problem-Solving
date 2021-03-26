def marcsCakewalk(calorie):
    miles = 0
    calorie.sort(reverse=True)
    for i in range(len(calorie)):
        miles += (calorie[i] * 2 ** i)
    return miles


if __name__ == '__main__':
    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(str(result) + '\n')
