# 백준 7576번 토마토 구현 3
# Index ERROR ㅜㅜ

from collections import deque
import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

MAX = 1000 + 3
# 입력 처리
M, N = map(int, input().split())
graph = [[-1]*(N+2) for _ in range(M+2)]
for i in range(N):
    graph[i+1][1:M+1] = list(map(int, input().split()))

for i in range(len(graph)):
    print(graph[i])


def bfs(queue):
    while queue:
        y, x = queue.popleft()
        now = graph[y][x]
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if graph[ny][nx] == 0:
                # visited[ny][nx] == True
                graph[ny][nx] = now + 1
                queue.append((ny, nx))


queue = deque([])
for y in range(N+2):
    for x in range(M+2):
        if graph[y][x] == 1:
            queue.append((y, x))
bfs(queue)


result = 0
max_value = 0
for i in range(N):
    if 0 in graph[i]:
        result = -1
        break
    max_value = max(max_value, max(graph[i]))
if result != -1:
    result = max_value - 1


print(result)
