# 백준 12865번 평범한 배낭
"""
입력
N K (100, 100000)
N줄 각 물건의 무제 W V

출력
배낭에 넣을 물건들의 가치합 최대값

i번째 물건을 넣을까? 말까?
안넣을때는 위에서 가져오고, 넣을때는 j-w에서 가져온다
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
# print(items)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = items[i-1]
    for j in range(1, K+1):
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]


print(dp[N][K])
