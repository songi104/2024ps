from copy import deepcopy
import sys
from collections import deque

sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
visited = [[False]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))
    # print(graph[_])

# 1. 0에 대해서 벽 3개 세우기
# 1-a. 가능한 부분을 pos에 넣고
pos = []
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            pos.append((y, x))

# 바이러스 있는 부분은 queue에 담아놓기
queue = deque([])
for y in range(N):
    for x in range(M):
        if graph[y][x] == 2:
            queue.append((y, x))
            visited[y][x] = True


def bfs(origin_queue, origin_graph, origin_visited):
    queue = deepcopy(origin_queue)
    graph = deepcopy(origin_graph)
    visited = deepcopy(origin_visited)
    while queue:
        y, x = queue.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y+dy, x+dx
            if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == 0 and not visited[ny][nx]:
                graph[ny][nx] = 2
                visited[ny][nx] = True
                queue.append((ny, nx))

    # graph에 대해서 안전영역 세고 max return
    result = 0
    for line in graph:
        result += line.count(0)
    return result


# print(pos)

result = 0
# 1-b. pos에 대해서 조합 구상해서 벽 세우기.
# print(f'벽을 세울 수 잇는 곳은 {len(pos)}개입니다.')
count = 0
for i in range(2, len(pos)):
    for j in range(1, i):
        for k in range(j):
            ty_i, tx_i = pos[i]
            graph[ty_i][tx_i] = 1
            ty_j, tx_j = pos[j]
            graph[ty_j][tx_j] = 1
            ty_k, tx_k = pos[k]
            graph[ty_k][tx_k] = 1

            # bfs 이용해 바이러스 퍼트리기
            safe = bfs(queue, graph, visited)
            count += 1
            # print(f'bfs 바깥에서 {graph}')

            # 그래프 원상복구
            ty_i, tx_i = pos[i]
            graph[ty_i][tx_i] = 0
            ty_j, tx_j = pos[j]
            graph[ty_j][tx_j] = 0
            ty_k, tx_k = pos[k]
            graph[ty_k][tx_k] = 0

            # 결과에서 안전영역 세고 max 결정하기
            result = max(safe, result)

            # if count == 3:
            #     break

print(result)
