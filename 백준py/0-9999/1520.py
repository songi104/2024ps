# 백준 1520번 내리막길
"""
dfs 돌려서 하면 되지않나?
백트래킹 쓰면될 것 같음.
"""

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dp = [[-1]*M for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(i, j):
    global graph
    global d

    if i == N-1 and j == M-1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for dy, dx in d:
        ny = i+dy
        nx = j+dx
        # print(ny, nx)
        if 0 <= ny < N and 0 <= nx < M and (graph[ny][nx] < graph[i][j]):
            dp[i][j] += dfs(ny, nx)

    return dp[i][j]


print(dfs(0, 0))
