"""
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
(1은 바이러스가 퍼질 수 없다!)
벽을 3개 세워서
바이러스 퍼질 수 없는 곳 계산하고
안전영역 최댓값 구하기.

1. 벽 3개 세운다
2. 바이러스들에서 바이러스를 퍼트린다 -> bfs 이용해야겠다
3. 안전영역 계산하고 ans 업데이트
"""

from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(graph)

ans = 0
walls = []
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            walls.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))


def bfs(graph):
    q = deque(virus)
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append((ny, nx))

    return graph


def cal(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


# 1. 벽 3개 세운다
for i in range(len(walls)-2):
    for j in range(i+1, len(walls)-1):
        for k in range(j+1, len(walls)):
            # 벽을 세운다
            ti, tj = walls[i]
            graph[ti][tj] = 1
            ti, tj = walls[j]
            graph[ti][tj] = 1
            ti, tj = walls[k]
            graph[ti][tj] = 1

            # 바이러스를 퍼트리고
            tgraph = deepcopy(graph)
            tgraph = bfs(tgraph)

            # 안전영역 계산하고
            ans = max(ans, cal(tgraph))

            # 다시 원래대로
            ti, tj = walls[i]
            graph[ti][tj] = 0
            ti, tj = walls[j]
            graph[ti][tj] = 0
            ti, tj = walls[k]
            graph[ti][tj] = 0

print(ans)
