# 백준 9663번 N-Queen
"""
1. 아이디어
전부 돌릴 건데.. 
visited = [False]*N -> y에 대해서..

"""


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = True
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = False


N = int(input())
ans = 0

v1 = [False]*N
v2 = [False]*(2*N)
v3 = [False]*(2*N)

dfs(0)
print(ans)
