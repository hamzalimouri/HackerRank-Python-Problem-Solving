import math


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


def lcmList(a):
    res = a[0]
    for i in a[1:]:
        res = lcm(res, i)
    return res


def gcdList(a):
    res = a[0]
    for i in a[1:]:
        res = math.gcd(res, i)
    return res


def getTotalX(a, b):
    lcm_a = lcmList(a)
    gcd_b = gcdList(b)
    res = 0
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            res += 1
    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
