# 백준 15652번 N과 M (4)

N, M = map(int, input().split())


def dfs(num, tlst):
    if num == M:
        print(*tlst)
        return

    last = 1
    if tlst:
        last = tlst[-1]

    for i in range(last, N+1):
        dfs(num+1, tlst+[i])


dfs(0, [])
