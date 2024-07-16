# 백준 2178번 미로찾기

import sys

N, M = map(int, sys.stdin.readline().split())
graph = [ ['0']*M for _ in range(N) ]
visited = [ [False]*M for _ in range(N) ]
for n in range(N):
    graph[n] = list(sys.stdin.readline().rstrip())
print(graph)

global result
result = []


def dfs(graph, i, j, cnt):
    cnt += 1
    ds = [(1,0), (-1,0), (0,1), (0,-1)]
    visited[i][j] = True
    print(f'현재위치 {i},{j}')
    for dy, dx in ds:
        ny = i + dy
        nx = j + dx
        
        # 범위 초과
        if (ny >= N or ny < 0 or nx >= M or nx < 0): continue

        if (visited[ny][nx]==True) : continue 
        elif (graph[ny][nx] == '1'):
            #print(f'{ny},{nx}로 이동합니다')
            
            cnt = dfs(graph, ny, nx, cnt)
            if ((ny == N-1) and (nx == M-1)):
                result.append(cnt)
                print(f'{cnt} 추가합니다')
                return cnt
            
            
    return cnt


dfs(graph, 0, 0, 0)
print((result))