# 백준 알고리즘 수업 - 깊이 우선 탐색 2

from collections import defaultdict
N, M, R = map(int, input().split())
import sys
sys.setrecursionlimit(10**5)

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort(reverse=True)

def dfs(i):
    global cnt
    vis[i] = cnt
    cnt += 1

    for n_node in graph[i]:
        #print(n_node)
        if vis[n_node] == 0:
            dfs(n_node)

vis = [0]*(N+1)
cnt = 1
dfs(R)
print(*vis[1:], sep="\n")