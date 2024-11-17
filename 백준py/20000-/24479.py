# 백준 알고리즘 수업 깊이우선탐색1
from collections import defaultdict
import sys
input = sys.stdin.readline
#print = sys.stdout.write


N, M, R = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in graph:
    graph[k].sort()
print(graph)

vis = [0]*(N+1)
stack = [R]
cnt = 0
while stack:
    top = stack.pop()
    if not vis[top]:
        cnt += 1
        vis[top] = cnt
    for n_node in graph[top]:
        if vis[n_node] == 0:
            vis[n_node]=cnt
            cnt += 1
            stack.append(n_node)


for i in range(1,N+1):
    print((vis[i]))