# 백준 17404번 RGB거리 2
"""
for문과 dp로 구현.
근데 1과 n을 어떻게 처리하지?
일단 저장해서 하는 걸로 해보자

"""


import sys
input = sys.stdin.readline

N = int(input())
lst = [0]
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

INF  = sys.maxsize
res = INF
for color in (0,1,2): # 첫번째 color
    # 첫번째 집 색칠
    dp = [[0]*3 for _ in range(N+1)]
    dp[1][color] = lst[1][color]
    dp[1][color-2] = INF
    dp[1][color-1] = INF
    #print(dp[1])

    # 중간 집 색칠
    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lst[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lst[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + lst[i][2]

    # 마지막 집 색칠
    for last in (0,1,2):
        if last != color:
            res = min(res, dp[N][last])        


print(res)
