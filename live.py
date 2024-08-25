# 백준 2293번 동전 1
"""
dp[i][j] : i번째 동전을 써서 j원을 만드는 경우의 수
dp[i][j] = dp[i-1][j] + dp[i][j-coin]
dp[j] = dp[j] + dp[j-coin]

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# print(coins)

dp = [0]*(K+1)
dp[0] = 1

for i in range(N):
    coin = coins[i]
    for j in range(coin, K+1):
        dp[j] = dp[j] + dp[j-coin]

print(dp[K])
