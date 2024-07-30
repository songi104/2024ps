# 백준 2644번 촌수계산

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

# 재귀방식으로


def dfs(stack, graph, visited, result, end):
    while stack:
        if graph[stack[0]]:


stack = [a]
dfs(stack, graph, visited, result, b)

if result[b] == 0:
    print(-1)
else:
    print(result[b])
