# 백준 2225번 합분해
"""
0부터 N까지의 정수를 K개 더한다. 그래서 합이 N이 되게 한다.


입력
N, K <= 200

출력
답을 10**9 로 나눈 나머지

kHn을 구하는 문제이다. 중복순열?조합? 암튼.
이걸 식으로 쓰면 (K+N-1)!/(N!*(K-1)!) 이 된다.
facto 만들어서 하면 됨

근데 kCn = k-1Cn-1 + k-1Cn 이기 떄문에
dp[n][k] = dp[n-1][k-1] + dp[n-1][K]
1차원으로 바꾸면
dp[k] = dp[k-1] + dp[k]

우리가 구해야하는 건 K+N-1CN
for i in range(K+N-1):
    for j in range(K):
        dp update

dp[1][:] = [1]*N
dp[2][1] = 



a1 + a2+ a3 + ,,.. + ak = N
kHn = k+n-1Cn

nCk = n-1Ck + n-1Ck-1
dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
dp[j] =dp[j] + dp[j-1]

1. 입력
2. dp 계산하고 나머지 저장
3. dp[k][n] return
dp[k+n-1][n]
dp[k][n]
"""

N, K = map(int, input().split())
dp = [0]*(N+1)
dp[0] = 1
mod = 1000000000

for i in range(1, K+1):
    for j in range(1, N+1):
        dp[j] = (dp[j] + dp[j-1]) % mod

print(dp[N])
