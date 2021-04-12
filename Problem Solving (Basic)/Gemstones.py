def gemstones(arr):
    res = 0
    s = set(arr[0])
    for c in s:
        count = 0
        for st in arr[1:]:
            if c in st:
                count += 1
        if count == len(arr) - 1:
            res += 1
    return res


if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    print(str(result) + '\n')
