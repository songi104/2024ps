# 백준 2606번 바이러스
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def dfs(v, stack=[]):
    result = 1
    stack.append(v)
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            result += dfs(node, stack)

    return result

result = dfs(1)
print(result-1)
