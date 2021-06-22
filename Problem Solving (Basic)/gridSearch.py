def gridSearch(G, P):
    len_g = len(G)
    len_p = len(P)
    i = 0
    while i < len_g:
        if P[0] in G[i]:
            j = 0
            c = 1
            while j + len(P[0]) <= len(G[0]):
                index = G[i][j:].find(P[0])
                if index == -1:
                    break
                for k in range(1, len_p):
                    if index == G[i + k][j:].find(P[k]):
                        c += 1
                    else:
                        break
                j += index + 1
                if c == len_p:
                    return 'YES'
        i += 1
    return 'NO'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
