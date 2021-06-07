def jimOrders(orders):
    dic = {i: orders[i][0] + orders[i][1] for i in range(len(orders))}
    return [k + 1 for k, _ in sorted(dic.items(), key=lambda item: item[1])]


if __name__ == '__main__':
    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(' '.join(map(str, result)))
