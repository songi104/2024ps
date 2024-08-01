# 백준 16946번 벽 부수고 이동하기
# 시간초과로 인해 생각한 다른 풀이

from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
result = []
for _ in range(N):
    line = list(map(int, list(input().rstrip())))
    graph.append(line[:])
    result.append(line[:])

# component 계산하기 with bfs
cnt = 1
component = {}
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt += 1
            q = deque([(i, j)])
            graph[i][j] = cnt
            res = 0
            while q:
                y, x = q.popleft()
                res += 1
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny, nx = dy+y, dx+x
                    if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == 0:
                        q.append((ny, nx))
                        graph[ny][nx] = cnt
            component[cnt] = res


# walls에 집어넣기
walls = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            walls.append((i, j))

# walls마다 주변을 더해서 바꾸기
for wall in walls:
    y, x = wall
    res = 1
    lst = []  # 컴포넌트종류
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = dy+y, dx+x
        if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] >= 2 and not graph[ny][nx] in lst:
            name = graph[ny][nx]
            res += component[name]
            lst.append(name)
    result[y][x] = res % 10

for line in result:
    print(("".join(map(str, line))))
