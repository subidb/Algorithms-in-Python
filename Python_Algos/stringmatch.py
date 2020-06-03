def search(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            print("patterntern found at index ", i)


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i+j] != pattern[j]:
                break
            j += 1
        if j == m:
            print(i)


if __name__ == '__main__':
    text1 = "AABAACAADAABAAABAA"
    pattern1 = "AABA"
    search(pattern1, text1)

    print()
    naive_search(text1, pattern1)
#