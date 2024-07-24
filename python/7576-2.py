# 백준 7576번 토마토 구현 2

import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

# 입력 처리
M, N = map(int, input().split())
graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))
#print(graph)

from collections import deque
def bfs(queue):
    while queue:
        y, x = queue.popleft()
        now = graph[y][x]
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            ny = y + dy 
            nx = x + dx
            if (0<=ny<N and 0<=nx<M) and graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] == True
                graph[ny][nx] = now + 1
                queue.append((ny, nx))

queue = deque([])
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            queue.append((y,x))
bfs(queue)


result = 0
max_value = 0
for i in range(N):
    #print(graph[i])
    if 0 in graph[i]:
        result = -1
    #    break
    max_value = max(max_value, max(graph[i]))
if result != -1:
    result = max_value -1
    
print(result)