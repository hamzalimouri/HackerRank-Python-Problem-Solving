from functools import cmp_to_key


def cmp_bigint(x, y):
    n = len(x)
    m = len(y)
    if n == m:
        if x < y:
            return -1
    if n < m:
        return -1
    return 1


def bigSorting(unsorted):
    return sorted(unsorted, key=cmp_to_key(cmp_bigint))


if __name__ == '__main__':
    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print('\n'.join(result))
