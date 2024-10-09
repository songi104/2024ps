# 백준 소수 찾기
"""
N <= 100
1000^(100)
"""
N = int(input())
numbers = list(map(int, input().split()))
prime = [True]*(1001)
prime[1] = False

# 에라토스테네스의 체
for i in range(2, 32):
    j = 2
    while True:
        if i*j > 1000:
            break
        prime[i*j] = False
        j += 1

ans = 0
for n in numbers:
    if prime[n]:
        ans += 1

print(ans)
