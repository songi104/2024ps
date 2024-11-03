"""
한번에 bfs에서 두 개의 vis를 관리
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
#print(graph)

vis = [[[0]*2 for _ in range(M)] for _ in range(N)]
# bfs
from collections import deque
q = deque([(0,0,0)])
vis[0][0][0] = 1
dy = [1,0,-1,0]
dx = [0,1,0,-1]

while q:
    cy, cx, broken = q.popleft()
    
    if (cy == N-1 and cx == M-1):
        print(vis[cy][cx][broken])
        exit()

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if (ny < 0 or ny >= N or nx < 0 or nx>=M): continue
        if vis[ny][nx][broken]: continue
        if graph[ny][nx] == "1" and not broken: # 벽 부수자
            vis[ny][nx][1] = vis[cy][cx][broken] + 1
            q.append((ny,nx,1))
        elif graph[ny][nx] == "1" and broken:
            continue
        elif graph[ny][nx] == "0":
            q.append((ny,nx,broken))
            vis[ny][nx][broken] = vis[cy][cx][broken] + 1
        
print(-1)
              

