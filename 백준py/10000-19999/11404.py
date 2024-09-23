# 백준 11404번 플로이드

"""
플로이드 사용하자!

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

INF = sys.maxsize
N = int(input())
M = int(input())
edges = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    edges[s][e] = min(edges[s][e], w)

for i in range(N+1):
    edges[i][i] = 0

# print(edges)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if edges[i][k] + edges[k][j] < edges[i][j]:
                edges[i][j] = edges[i][k] + edges[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if edges[i][j] == INF:
            print(0, end=' ')
        else:
            print(edges[i][j], end=' ')
    print()
