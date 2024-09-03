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
"""

N, K = map(int, input().split())
dp = [0]*(K+N)
dp[0] = 1
dp[1] = 1  # 1!
mod = 1000000000

if K > N:
    print(0)
else:
    for i in range(2, K+N):
        dp[i] = (i*dp[i-1]) % mod
        if dp[i] == 0:
            print(i)
    print(dp[K+N-1], dp[N], dp[K-1])
    res = int((dp[K+N-1]/(dp[N]*dp[K-1])) % (mod))
    print(res)
