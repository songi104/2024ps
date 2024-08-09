

"""
이동조건: graph<=lv 이동할 수 있음
먹는조건: graph <lv 먹을 수 있음
제일 가까운 물고기를 먹고
가장 위, 가장 왼쪽
lv이랑 물고기 개수를 똑같이 먹으면 lv 업
while 문 (종료조건: 먹을 물고기가 없을 때)

1. 세팅을 하고
2. while True:
    if (먹을 물고기가 없다면): break
    물고기를 먹고
    시간을 계산하고
    레벨 조건
3. print(ans)
"""

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
    visited[y][x] = True
    time = [[0]*N for _ in range(N)]

    can_eat = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy+y, dx+x
            if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx] and graph[ny][nx] <= lv:
                # print(ny, nx)
                time[ny][nx] = time[y][x] + 1
                q.append((ny, nx))
                visited[ny][nx] = True
                if 0 < graph[ny][nx] < lv:
                    can_eat.append((time[ny][nx], ny, nx))

    if len(can_eat) == 0:
        return False

    can_eat.sort(key=lambda x: (x[0], x[1], x[2]))
    res, y, x = can_eat[0]  # 걸린시간, y좌표, x좌표
    return res, y, x


for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            y, x = i, j
            graph[i][j] = 0


ans = 0
lv = 2
exp = 0
while True:

    bfs_result = bfs(y, x)
    # bfs 돌려서 제일 가까운 물고기를 찾고
    # y, x 좌표 바꾸고
    # graph도 바꾸고
    # 걸리는 시간 계산
    # print(bfs_result)
    if not bfs_result:
        break

    # 물고기를 먹고
    # 시간을 계산하고
    res, y, x = bfs_result
    graph[y][x] = 0
    ans += res

    # 레벨 조건
    exp += 1
    if (lv == exp):
        lv += 1
        exp = 0


print(ans)
