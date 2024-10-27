# 백준 ACM Craft
"""
W를 지으면 승리한다
dp를 0으로 하면 시간초과가 나고
-1로 하면 시간초과가 안 난다.
=> 건물 시간이 0도 가능하기 때문에
조건에 의해서 dp를 계속계속 불러오기 때문이다!!!!
"""
import sys
input = sys.stdin.readline

def solve(t):
    if dp[t] != -1:
        return dp[t]

    # 존재하지 않으면..
    if t in rules:
        M = 0
        for prev in rules[t]:
            M = max(M, solve(prev) + times[t])
        dp[t] = M
    else:
        dp[t] = times[t]

    return dp[t]



T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int,input().split()))
    rules = {}
    for _ in range(K):
        X, Y = map(int,input().split()) # x 지은 다음에 y 지을 수 있음
        if Y in rules:
            rules[Y].append(X)
        else:
            rules[Y] = [X]
    W = int(input()) 
    dp = [-1]*(N+1)
    print(solve(W))