# 백준 2606번 바이러스
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        now = queue.popleft()
        if len(graph[now]) == 0: continue
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

bfs(graph, 1, visited)
result = 0
for node in visited:
    if node: result+=1

print(result-1)