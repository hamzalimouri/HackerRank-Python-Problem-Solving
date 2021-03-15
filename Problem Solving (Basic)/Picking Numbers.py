from collections import Counter


def pickingNumbers(a):
    counter = Counter(a)
    res = 0
    for key in sorted(set(a)):
        res = max(res, counter[key] + counter[key + 1])
    return res


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
