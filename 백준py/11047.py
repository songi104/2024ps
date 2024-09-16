# 백준 11047번 동전 0


N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

ans = 0
tK = K
coins.sort(reverse=True)
for coin in coins:
    n = tK // coin
    ans += n
    tK -= n*coin
print(ans)
