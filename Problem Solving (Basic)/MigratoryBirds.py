from collections import Counter


def migratoryBirds(arr):
    count = Counter(arr)
    temp, j = count[1], 1
    for i in range(2, 6):
        if temp < count[i]:
            temp = count[i]
            j = i
    return j


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')
