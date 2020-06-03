def string_reverse(string):
    list1 = list(string)
    j = len(list1)-1
    i = 0
    while i <= j:
        list1[i], list1[j] = list1[j], list1[i]
        i += 1
        j -= 1

    str2 = ''.join(list1)
    return str2


def string_reverse_rec(list1, start=None, end=None):
    # list1 = list(string)
    if start is None:
        start = 0
    if end is None:
        end = len(list1)-1
    if start >= end:
        return
    list1[start], list1[end] = list1[end], list1[start]
    string_reverse_rec(list1, start+1, end-1)


def reverselist(string, start=None, end=None):
    list1 = list(string)
    if start is None:
        start = 0
    if end is None:
        end = len(list1) - 1
    if start >= end:
        return
    list1[start], list1[end] = list1[end], list1[start]
    reverselist(list1, start + 1, end - 1)


if __name__ == '__main__':
    print(string_reverse("xyzzyuy"))

    list_1 = [1, 3, 5, "SS", 2]
    string_reverse_rec(list_1)
    print(list_1)



# x = "YYYxcv"
# y = x[::-1]
# print(y)

