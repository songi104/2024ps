# 백준 1463번 1로 만들기

import sys
N = int(input())

dp = [0]*(N+1)
for i in range(1, N+1):
    if 3*i <= N:
        if dp[3*i] == 0:
            dp[3*i] = dp[i] + 1
        else:
            dp[3*i] = min(dp[3*i], dp[i]+1)

    if 2*i <= N:
        if dp[2*i] == 0:
            dp[2*i] = dp[i] + 1
        else:
            dp[2*i] = min(dp[2*i], dp[i]+1)

    if i+1 <= N:
        if dp[i+1] == 0:
            dp[i+1] = dp[i] + 1
        else:
            dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[N])
