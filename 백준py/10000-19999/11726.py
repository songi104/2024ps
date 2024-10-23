# 백준 2xn 타일링

N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

if N == 1:
    print(1)
    exit()

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007

print(dp[N])