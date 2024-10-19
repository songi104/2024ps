import sys
from collections import deque
input = sys.stdin.readline
h, n, m = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

q = deque([])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

ans = 0


def bfs():
    global q
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and not visited[nz][ny][nx] and graph[ny][ny][nx] == 0:
                q.append((nz, ny, nx))
                graph[nz][ny][nx] = graph[z][y][x] + 1
                visited[nz][ny][nx] = True


for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1 and not visited[z][y][x]:
                visited[z][y][x] = True
                q.append((z, y, x))
print('==')
bfs()
for box in graph:
    for line in box:
        for n in line:
            if n == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(line))

print(ans-1)
