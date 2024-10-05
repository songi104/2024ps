# 백준 12865번 평범한 배낭
"""
입력
N K (100, 100000)
N줄 각 물건의 무제 W V

출력
배낭에 넣을 물건들의 가치합 최대값
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
print(items)

dp = [0]*(K+1)

for w, v in items:
    for value in range(K, v-1, -1):
        dp[value] = min(dp[value], dp[value-v]+w)


print(dp[K])
