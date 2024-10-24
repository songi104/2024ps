# 평범한 배낭 24-10-23
"""
dp[i][j] = max(dp[i-w][j-1] + v, dp[i][j-1])
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [(0,0)] # w, v
for _ in range(N):
    items.append(tuple(map(int,input().split())))

dp = [[0]*(N+1) for _ in range(K+1)]
for i in range(1,K+1):
    for j in range(1,N+1):
        w, v = items[j]
        if i >= w:
            dp[i][j] = max(dp[i-w][j-1]+v, dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]
print(dp[K][N])
