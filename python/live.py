from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리 및 세팅
N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
# print(graph)

# 2. 벽 3개 세우고
walls = []
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            walls.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))


def bfs(queue, visited, graph):
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            if (0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                graph[ny][nx] = 2
                queue.append((ny, nx))

    result = 0
    for line in graph:
        result += line.count(0)

    return result


# 3. bfs 바이러스 퍼트리고
result = 0
for i in range(2, len(walls)):
    for j in range(1, i):
        for k in range(j):
            y_i, x_i = walls[i]
            y_j, x_j = walls[j]
            y_k, x_k = walls[k]

            temp_graph = [arr[:] for arr in graph]
            temp_graph[y_i][x_i] = 1
            temp_graph[y_j][x_j] = 1
            temp_graph[y_k][x_k] = 1

            temp_virus = deque(virus)
            visited = [[False]*M for _ in range(N)]

            safe = bfs(temp_virus, visited, temp_graph)
            # 4. 안전구역 세기
            result = max(safe, result)


print(result)
