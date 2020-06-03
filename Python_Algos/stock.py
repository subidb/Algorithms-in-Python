def max_profit(stock_list):
    totalnum = len(stock_list)
    maxdiff = 0

    for i in range(totalnum):
        for j in range(i, totalnum-i):
            diff = stock_list[i+j] - stock_list[i]
            if diff > maxdiff:
                maxdiff = diff

    return maxdiff


def maxDiff(arr):
    arr_size = len(arr)
    max_diff = 0
    min_element = arr[0]

    for i in range(1, arr_size):
        diff = arr[i] - min_element
        if diff > max_diff:
            max_diff = diff

        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff


# stock_list1 = [14, 33, 23, 11, 45, 22, 54, 11, 15]
stock_list1 = [10, 7, 20, 5, 8, 11, 9]

print(max_profit(stock_list1))
print(maxDiff(stock_list1))

