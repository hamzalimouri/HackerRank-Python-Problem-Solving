def toys(w):
    res = 0
    w.sort()
    i = 0
    while i < len(w):
        j = i + 1
        while j < len(w):
            if w[j] > w[i] + 4:
                break
            j += 1
        i = j
        res += 1
    return res


if __name__ == '__main__':
    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    print(str(result) + '\n')
