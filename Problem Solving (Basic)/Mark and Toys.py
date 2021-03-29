def maximumToys(prices, k):
    prices.sort()
    res = 0
    for price in prices:
        if price > k:
            break
        res += 1
        k -= price
    return res


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')
