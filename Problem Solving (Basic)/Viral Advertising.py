import math


def viralAdvertising(n):
    res = 0
    p = 5
    for i in range(n):
        f = math.floor(p / 2)
        res += f
        p = f * 3
    return res


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')
