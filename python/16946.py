# 백준 16946번 벽 부수고 이동하기
# 시간초과로 인해 다른 풀이 생각해보기!!!

from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))
# print(graph)

"""
1. 1인 곳을 walls에 집어넣기
2. wall in walls 에 대해서 bfs 돌리고 갈 수 있는 칸 수 res = bfs()
3. res를 answer(graph)에 집어넣기
"""

# walls에 집어넣기
walls = []
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            walls.append((y, x))
# print(walls)


def bfs(graph, visited, y, x):
    # 갈 수 있는 칸 수를 센다. 즉 q에서 popleft 횟수세기
    res = 0
    q = deque([])
    q.append((y, x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        res += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            if (0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and graph[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = True
    return res


for wall in walls:
    # 새로운 graph, visited 만들어서 bfs에 전달
    y, x = wall
    graph[y][x] = 0
    visited = [[False]*M for _ in range(N)]
    res = bfs(graph, visited, y, x) % 10
    graph[y][x] = res

for line in graph:
    print(str(line).replace(', ', '', -1)[1:-1])
