from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# print(graph)


def bfs(y, x):
    q = deque([(y, x)])
    visited = [[False]*N for _ in range(N)]
    time = [[0]*N for _ in range(N)]
    visited[y][x] = True

    can_eat = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            if (0 <= ny < N and 0 <= nx < N) and graph[ny][nx] <= lv and not visited[ny][nx]:
                q.append((ny, nx))
                time[ny][nx] = time[y][x] + 1
                visited[ny][nx] = True
                if 0 < graph[ny][nx] < lv:
                    can_eat.append((time[ny][nx], ny, nx))

    if len(can_eat) == 0:
        return False

    # can_eat 정렬
    can_eat.sort(key=lambda x: (x[0], x[1], x[2]))

    res, y, x = can_eat[0]
    return res, y, x  # 새로운 위치


ans = 0
lv = 2
exp = 0

# shark 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            y, x = i, j
            graph[i][j] = 0


while True:
    bfs_result = bfs(y, x)

    # 먹을 수 있는 게 없음
    if not bfs_result:
        break

    time, y, x = bfs_result
    ans += time
    # print(bfs_result)
    graph[y][x] = 0

    # level 로직
    exp += 1
    if (exp == lv):
        lv += 1
        exp = 0


print(ans)
