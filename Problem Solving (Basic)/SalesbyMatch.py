from collections import Counter


def sockMerchant(n, ar):
    c = Counter(ar)
    ans = 0
    for _, i in c.items():
        ans += i // 2
    return ans


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
