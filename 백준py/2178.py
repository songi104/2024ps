# 백준 2178번 미로찾기

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [['0']*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for n in range(N):
    graph[n] = list(sys.stdin.readline().rstrip())
# print(graph)


result = []


# bfs 정의
df = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(graph, visited, i, j):
    queue = deque([])
    visited[i][j] = True
    queue.append((i, j, 1))

    while queue:
        # print(i, j, cnt)
        i, j, cnt = queue.popleft()
        cnt = cnt+1
        # new_cnt = cnt+1
        for dy, dx in df:
            ny = i + dy
            nx = j + dx
            # print(ny, nx)
            if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == '1' and visited[ny][nx] == False:
                # print(f'{i},{j},{cnt}가 추가되었어요')
                visited[ny][nx] = True
                queue.append((ny, nx, cnt))
            if ny == N-1 and nx == M-1:
                result.append(cnt)

    # 호출
    cnt += 1


# bfs 호출하면 result에 결과저장
bfs(graph, visited, 0, 0)
print(min(result))

"""
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
            
            if ((ny == N-1) and (nx == M-1)):
                result.append(cnt)
                print(f'{cnt} 추가합니다')
                return cnt
            cnt = dfs(graph, ny, nx, cnt)
            
            
    return cnt
"""
