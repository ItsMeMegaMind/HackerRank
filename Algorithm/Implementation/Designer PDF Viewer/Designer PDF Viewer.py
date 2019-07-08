def designerPdfViewer(h, word):
    return max([h[ord(i)-97] for i in word])*len(word)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
