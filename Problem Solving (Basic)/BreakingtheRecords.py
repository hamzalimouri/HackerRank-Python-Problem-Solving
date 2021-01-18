def breakingRecords(scores):
    i, j, m, M = 0, 0, scores[0], scores[0]
    for score in scores:
        if m > score:
            i += 1
            m = score
        if M < score:
            j += 1
            M = score
    return j, i


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
