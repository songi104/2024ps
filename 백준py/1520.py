# 백준 1520번 내리막길
"""
확통 경우의수랑
graph 뽑고 bfs랑 합치면 될 듯


"""

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
print(graph)

dp = [[-1]*N for _ in range(M)]
dp[0][0] = 1

# dfs


def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = y


dfs(0, 0)
print(dp[M-1][N-1])
