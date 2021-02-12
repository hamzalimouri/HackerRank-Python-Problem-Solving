def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')
