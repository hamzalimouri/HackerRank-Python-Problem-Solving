def designerPdfViewer(h, word):
    res = 0
    new_word = set(word)

    for letter in new_word:
        i = ord(letter) - ord("a")
        res = max(res, h[i])

    return res * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
