def bonAppetit(bill, k, b):
    s = sum(bill) - bill[k]
    r = s // 2
    diff = b - r
    if diff:
        print(diff)
    else:
        print("Bon Appetit")


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
