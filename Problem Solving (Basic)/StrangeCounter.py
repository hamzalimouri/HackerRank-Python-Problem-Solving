def strangeCounter(t):
    i = 0
    k = 0
    while k < t:
        k += 3 * (2 ** i)
        i += 1
    return k - t + 1


if __name__ == '__main__':
    t = int(input())

    result = strangeCounter(t)

    print(str(result) + '\n')
