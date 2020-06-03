def recur_fib(x):
    if x < 0:
        print("incorrect input")
        return
    if x in [0, 1]:
        return x
    return recur_fib(x-1) + recur_fib(x-2)


def itr_fib(x):
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a


def fib_dp(n):
    cache = {0: 1, 1: 1, 2: 1}
    if n in cache:
        return cache[n]
    tmp = fib_dp(n-1) + fib_dp(n-2)
    cache[n] = tmp
    return tmp


def fib_dp2(n):
    lst = [None]*(n+1)
    if n in [0, 1]:
        return n
    lst[0], lst[1] = 0, 1
    for i in range(2, len(lst)):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[n]


print(recur_fib(20))
print(itr_fib(20))
print(fib_dp(20))
print(fib_dp2(20))


def recr_powr(val, n):
    if n == 1:
        return val
    return val * recr_powr(val, n - 1)


def itr_powr(val, n):
    x = 1
    for _ in range(n):
        x = val * x
    return x


print(recr_powr(3, 5))
print(itr_powr(2, 5))
