# 백준 2206번 벽 부수고 이동하기
"""
1. 벽이 있는 곳을 walls에 넣는다
2. 벽을 하나 부순다
3. bfs를 돌려서 최솟값 update (초기값 INF)
4. res에 따라 -1 또는 res 출력
=> 시간복잡도 O(N4)
bfs를 한 번만 돌려야한다!!
새로운 파일 ㄱㄱ
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
#print(graph)

walls = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == "1":
            walls.append((i,j))

#print(walls)

INF = sys.maxsize
res = INF
from collections import deque

def bfs(t_graph):
    q = deque([(0,0)])
    vis = [[False]*M for _ in range(N)]
    #print(t_graph)

    while q:
        cy, cx = q.popleft()
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny = cy + dy
            nx = cx + dx
            if (0<=ny<N and 0<=nx<M and not vis[ny][nx] and t_graph[ny][nx] =="0"):
                t_graph[ny][nx] = str(int(t_graph[cy][cx]) + 1)
                vis[ny][nx] = True
                q.append((ny, nx))

    return INF if t_graph[N-1][M-1] == "0" else int(t_graph[N-1][M-1]) + 1
                
from copy import deepcopy

for w_i, w_j in walls:
    t_graph = deepcopy(graph)
    t_graph[w_i][w_j] = "0"
    res = min(res, bfs(t_graph))

if res == INF:
    print(-1)
else:
    print(res)