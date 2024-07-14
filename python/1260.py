# 백준 1260번 DFS와 BFS

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited_bfs = [False]*(N+1)
visited_dfs = [False]*(N+1)
#print(visited_bfs)


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

# graph 정렬
for _ in range(len(graph)):
    graph[_].sort()

def dfs(graph, v, stack=[]):
    """
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. - 스택의 최상단 노드에 방문하지않은 인접노드가 있으면 그 인접노드를 스택에 넣고 방문처리를 한다.
       - 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    3. 2번을 계속 반복한다.
    """
    stack.append(v)
    visited_dfs[v] = True
    print(v, end=' ')

    next_nodes = graph[v]
    for node in next_nodes:
        if not visited_dfs[node]:
            dfs(graph, node, stack)


def bfs(graph, v):
    # 1. 시작 노드를 큐에 넣고 방문처리한다
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        # 2. 노드 하나를 꺼낸다
        now = queue.popleft()
        print(now, end=' ')

        # 3. 방문하지않은 주변 노드를 큐에 넣고 방문처리

        if (graph[now]):
            graph[now].sort()
            next = graph[now]
        else: continue
        for n in next:
            if not visited_bfs[n]:
                queue.append(n)
                visited_bfs[n] = True

dfs(graph, V)  
print()
bfs(graph, V)

#print(graph)