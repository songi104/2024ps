# 백준 안전 영역
"""
1. bfs 풀이
비의 양 1-100에 대해서
res = max(res, bfs())
잠긴 곳은 다 visited
잠기지 않은 곳에 대해서 (not visited)
bfs 한 번 돌릴 때마다 res += 1

- 시간복잡도:
N = 100 -> bfs 약 N2 = 10000
rain 100 -> rain * N2 = 1000000
가능

2. dfs 풀이
잠긴 곳은 다 visited
잠기지 않은 곳에 대해서 (not visited)
dfs 한 번 돌릴 때마다
"""

import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


from collections import deque
def bfs(i, j, visited):
    q = deque([(i,j)])
    visited[i][j] = True
    
    dy = (1,-1,0,0)
    dx = (0,0,1,-1)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

    return visited


def solve(visited):
    res = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                visited = bfs(i,j,visited)
                res += 1

    return res

res = 0
for rain in range(0, 101):
    visited = [[False]*N for _ in range(N)]

    # 잠긴 곳 visit 처리
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                visited[i][j] = True

    res = max(solve(visited), res)

print(res)