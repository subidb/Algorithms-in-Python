def reverselist(list1, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(list1) - 1
    if start >= end:
        return
    list1[start], list1[end] = list1[end], list1[start]
    reverselist(list1, start + 1, end - 1)


list1 = [1, "sadsa", 2, 3]
reverselist(list1)
print(list1)

str1 = "abc"
list2 = []
for i in str1:
    list2.append(i)
#
str1rev = ""

reverselist(list2)
for item in list2:
    str1rev += item

print(str1rev)
