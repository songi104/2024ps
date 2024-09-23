import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력 처리 및 세팅
N, M = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(N):
    graph[_] = input().rstrip().split()
    # print(graph[_])


# 2. 벽을 세울 수 있는 곳, 바이러스 있는 곳 찾아서 기록.
walls = []
virus = ([])
for y in range(N):
    for x in range(M):
        if graph[y][x] == '0':
            walls.append((y, x))
        elif graph[y][x] == '2':
            virus.append((y, x))


def bfs(graph, queue, visited):
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            # print(visited[ny][nx])
            if (0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and graph[ny][nx] == '0':
                graph[ny][nx] = '2'
                queue.append((ny, nx))
                # visited[ny][nx] = True

    safe = 0
    for i in range(N):
        safe += graph[i].count('0')

    return safe


result = 0
# 3. 벽을 3개 세우고(조합) 바이러스를 퍼트린다.
for i in range(2, len(walls)):
    for j in range(1, i):
        for k in range(j):
            temp_graph = [arr[:] for arr in graph]
            temp_virus = deque(virus)
            visited = [[False]*M for _ in range(N)]
            # print(visited)

            y_i, x_i = walls[i]
            y_j, x_j = walls[j]
            y_k, x_k = walls[k]

            temp_graph[y_i][x_i] = 1
            temp_graph[y_j][x_j] = 1
            temp_graph[y_k][x_k] = 1

# 4. 안전영역을 계산하고 max를 업데이트한다.
            safe = bfs(temp_graph, temp_virus, visited)
            result = max(safe, result)


# 5. 결과출력
print(result)
