def catAndMouse(x, y, z):
    d1 = abs(x - z)
    d2 = abs(y - z)
    if d1 == d2:
        return 'Mouse C'
    elif d1 < d2:
        return 'Cat A'
    return 'Cat B'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')
