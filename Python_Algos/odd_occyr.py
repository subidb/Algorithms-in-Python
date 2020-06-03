lst1 = [1, 3, 5, 6, 3, 5, 6, 7]


dic = dict()
for i in lst1:
    dic[i] = 0

for i in lst1:
    if i:
        dic[i] += 1

for obj in dic:
    if dic[obj] % 2 != 0:
        print(obj)

print()
# print(dic)
def getOddOccurrence(arr):
    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res


arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print(lst1)
print(getOddOccurrence(lst1))

print(5 ^ 3)
