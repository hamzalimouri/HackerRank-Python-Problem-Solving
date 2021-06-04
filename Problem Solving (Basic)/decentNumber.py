def decentNumber(n):
    num_3 = n // 3
    num_5 = (n - 3 * num_3) // 5
    while num_3 != -1 and ((num_3 * 3) + (num_5 * 5)) != n:
        num_3 -= 1
        num_5 = (n - 3 * num_3) // 5
    if num_3 != -1:
        print('5' * num_3 * 3 + '3' * num_5 * 5)
    else:
        print('-1')


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
