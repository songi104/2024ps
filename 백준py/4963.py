from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]:
            ny, nx = dy+y, dx+x
            if (0 <= ny < h and 0 <= nx < w) and not visited[ny][nx] and graph[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = True


while True:
    w, h = map(int, input().split())

    if w*h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    # print(graph)
    visited = [[False]*w for _ in range(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(y, x)
                ans += 1

    print(ans)
