def fibonacciModified(t1, t2, n):
    res = [t1, t2]
    for _ in range(n - 2):
        res.append(res[-2] + res[-1] ** 2)
    return res[n - 1]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    print(result)
