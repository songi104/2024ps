# 백준 1012번 유기농 배추

import sys
from collections import deque


def bfs(graph, v):
    queue = deque([v])
    #print('queue:', queue)

    dss = [(1,0), (-1,0), (0,1), (0,-1)]
    while len(queue):
        i, j = queue.popleft()
        for dy, dx in dss:
            ny = i+dy
            nx = j+dx

            if (0<=ny<N and 0<=nx<M and graph[ny][nx]==1):
                graph[ny][nx] = 0 
                queue.append((ny,nx)) 




T = int(sys.stdin.readline())
result_list = []

for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split()) # 가로길이 M, 세로길이 N
    ground = [ [0]*M for _ in range(N) ]
    #visited = [ [False for n in range(M)] for m in range(N) ]
    
    for k in range(K):
        i, j = map(int, sys.stdin.readline().split())
        ground[j][i] = 1

    #print(ground)
    
    # bfs로 맵 돌기
    result = 0
    for i in range(N):
        for j in range(M):
            if (ground[i][j] == 1): 
                ground[i][j] = 0
                bfs(ground, (i,j))
                result += 1

    print(result)
    
