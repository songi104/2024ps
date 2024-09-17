# 백준 15650번 N과 M (2)
# 1부터 N까지 중복 없이 M개를 고른 수열

import sys

N, M = map(int, input().split())


def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return

    last = 0
    if tlst:
        last = tlst[-1]

    for i in range(last+1, N+1):
        dfs(n+1, tlst+[i])


dfs(0, [])
