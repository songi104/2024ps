# 백준 2133번 타일채우기
"""
3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수 구하기

입력 N<=30
출력 경우의 수
시간제한 2초
메모리 128MB

홀수일때는 채울 수 없는 듯.
짝수를 생각해보자.
일단 dp[i] = 3*dp[i-2] + 무언가..
i-2에서 3x2 블록을 추가해준 걸 의미한다.

dp[i] = solve(n)
solve(n):
res = 2
for i in range(n-4, 1, -2):
    res += dp[i]*2
res += dp[n-2]*3

"""


N = int(input())
dp = [0]*31
dp[0] = 1
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2]*3
    for j in range(i-4, -1, -2):
        dp[i] += dp[j]*2

print(dp[N])
