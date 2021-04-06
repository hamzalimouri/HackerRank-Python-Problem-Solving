import math


def squares(a, b):
    temp = math.ceil(math.sqrt(a))
    res = 0
    while temp ** 2 <= b:
        res += 1
        temp += 1
    return res


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(str(result) + '\n')
