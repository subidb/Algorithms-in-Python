def lcs(x, y, i=None, j=None):
    if i == -1 or j == -1:
        return 0
    elif x[i] == y[j]:
        return 1 + lcs(x, y, i-1, j-1)
    else:
        return max(lcs(x, y, i-1, j), lcs(x, y, i, j-1))



def lcs_topdown(x, y, i, j, c):
    if i == 0 or j == 0:
        return 0

    if c[i-1][j-1] != -1:
        return c[i-1][j-1]

    if x[i-1] == y[j-1]:
        c[i-1][j-1] = 1 + lcs_topdown(x, y, i-1, j-1, c)
        return c[i-1][j-1]

    else:
        c[i-1][j-1] = max(lcs_topdown(x, y, i-1, j, c), (lcs_topdown(x, y, i, j-1, c)))

    return c[i-1][j-1]


def lcs_bottomup(x, y):
    # find the length of the strings
    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


str1 = "abcbdabseraddddqweq44"
str2 = "bdcabaabpvfdvddwqewqeii404"

tab = [[-1] * 1000 for _ in range(1000)]


ans2 = lcs_topdown(str1, str2, len(str1), len(str2), tab)
print(ans2)
 

ans3 = lcs_bottomup(str1, str2)
print(ans3)

