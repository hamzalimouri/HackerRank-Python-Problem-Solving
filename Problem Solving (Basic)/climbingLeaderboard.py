def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    j = len(ranked) - 1
    res = []
    for i in player:
        while j >= 0:
            if i < ranked[j]:
                break
            j -= 1
        res.append(j + 2)
    return res


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
