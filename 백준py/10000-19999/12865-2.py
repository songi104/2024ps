# 백준 12865번 평범한 배낭
"""
dp를 줄여보자
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0]*(K+1)

for w, v in items:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

print(dp[K])
