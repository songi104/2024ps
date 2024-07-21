# 백준 11724번 연결 요소의 개수

import sys


N, M = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(N+1) ]
visited = [False]*(N+1)
visited[0] = True


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
#print(graph[4])


# dfs 풀이
def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        top_node = stack[-1]
        #print('top node:', top_node)
        nodes = graph[top_node]
        alone = True
        for node in nodes:
            if not visited[node]:
                stack.append(node)
                #print(node)
                visited[node] = True
                alone = False
                break
        if alone:
            stack.pop()


result = 0
for idx in range(N+1):
    if visited[idx]: continue
    #print(f'{idx} 방문합니다')
    dfs(idx)
    result += 1

print(result)



# bfs 풀이
from collections import deque


visited = [False]*(N+1)
visited[0] = True

def bfs(start):
    queue = deque([])
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        around = graph[now]
        for node in around:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


result = 0
for idx in range(N+1):
    if visited[idx]: continue
    #print(f'{idx} 방문합니다')
    bfs(idx)
    result += 1
print(result)
