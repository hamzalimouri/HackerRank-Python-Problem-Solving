def balancedSums(arr):
    s = sum(arr)
    l = 0
    for x in arr:
        s -= x
        if l == s:
            return 'YES'
        l += x
    return 'NO'


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
