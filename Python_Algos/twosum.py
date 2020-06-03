def solution(array, target):
    dic = {}
    for i, num in enumerate(array):
        diff = target - num
        if diff in dic:
            return [dic[diff], i]
            # return True
            # return [diff, num]
        else:
            dic[num] = i


arr = [2, 2, 5, 4, 8, 6]
tar = 6
a = solution(arr, tar)
print(a)

def twosum2(lst, target):
    for num in lst:
        diff = target - num
        print(diff, end=" ")
        if diff in lst and diff!=num:
            return True
    return False