# 백준 11050번 이항계수 1
"""
아이디어 1. for 문 이용
아이디어 2. d
"""
N, K = map(int, input().split())

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i][0] = 1
    for k in range(1, i+1):
        # print(k)
        dp[i][k] = dp[i-1][k-1]+dp[i-1][k]
    # print(i, dp)
print(dp[N][K])
