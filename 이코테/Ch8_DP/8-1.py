import time


def fibo1(x):
    if x == 1 or x == 2:
        return 1
    return fibo1(x-1) + fibo1(x-2)


k = 20
start = time.time()
fibo1(k)
end = time.time()
print(f'fibo1(recursibe)({k}):', end-start)


memo = [0]*200


def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if memo[x] != 0:
        return memo[x]
    memo[x] = fibo2(x-1) + fibo2(x-2)
    return memo[x]


k = 100
start = time.time()
fibo2(k)
end = time.time()
print(f'fibo2(memo)({k}):', end-start)


# fibo 3: 반복문 이용
d = [0]*200
d[1] = 1
d[2] = 1


def fibo3(x):
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
    return d[i]


print(fibo3(k))
