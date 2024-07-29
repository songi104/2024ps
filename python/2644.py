from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = {}
for _ in range(M):
    x, y = map(int, input().split())

    if not x in graph.keys():
        graph[x] = [y]
    else:
        graph[x].append(y)

    if not y in graph.keys():
        graph[y] = [x]
    else:
        graph[y].append(x)

result = [0]*(N+1)
visited = [False]*(N+1)


def bfs(start, end, graph, visited, result):
    q = deque([start])
    visited[start] = True
    cnt = 0

    while q:
        now = q.popleft()
        if now in graph.keys():
            around = graph[now]
        else:
            continue
        for next in around:
            if visited[next]:
                continue
            result[next] = result[now]+1
            visited[next] = True
            q.append(next)


bfs(a, b, graph, visited, result)

if result[b] == 0:
    print(-1)
else:
    print(result[b])
