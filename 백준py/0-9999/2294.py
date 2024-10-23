# 백준 2294번 동전2
"""
서로 다른 가치의 동전들을 사용해서(개수상관 ㄴㄴ)
사용한 동전 최소개수 출력
불가할시 -1 출력

1. greedy 큰 것부터 넣으면 어떨까? -> 이런 문제에서는 불가하다
2. brute force -> 시간제한 있다

입력에서 거를 것
- K보다 큰 코인
- 이미 있는 코인
"""


N, K = map(int, input().split())
coins = []
for _ in range(N):
    c = int(input())
    if c in coins or c > K:
        continue
    coins.append(c)
#print(coins)

import sys
INF = sys.maxsize
#print(INF)
dp = [INF]*(K+1)
dp[0] = 0

# dp 채우기
for i in range(1, K+1):
    for coin in coins:
        if coin > i:
            continue
        dp[i] = min(dp[i], dp[i-coin]+1)
#print(dp)
if dp[K] == INF:
    print(-1)
else: print(dp[K])
