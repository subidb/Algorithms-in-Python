def reverse(lst, start, end):
    if start >= end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse(lst, start+1, end-1)


def itr_reverse(str):
    lst = list(str)
    i = 0
    j = len(str)-1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    rev_str = ''.join(lst)
    return rev_str


a = [2, 4, 5, 6, 7]
reverse(a, 0, 4)
print(a)

st = "The big fat Nile river"
print(itr_reverse(st))