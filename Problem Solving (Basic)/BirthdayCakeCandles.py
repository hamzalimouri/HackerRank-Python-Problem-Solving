def birthdayCakeCandles(candles):
    m = candles[0]
    res = 0
    for i in candles:
        if i == m:
            res += 1
        elif i > m:
            m = i
            res = 1
    return res


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')
