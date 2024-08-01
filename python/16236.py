# 백준 16236번 아기상어

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# print(graph)

# 1. 세팅


def cal_pos(graph, lv):
    pos = []
    for y in range(N):
        for x in range(N):
            if 1 <= graph[y][x] < lv:
                pos.append((y, x))
    return pos


pos = cal_pos(graph, 2)  # 먹을 수 있는 물고기 위치


def bfs_target(graph, visited, target, y, x):
    q = deque([(y, x)])
    ty, tx = target
    visited[y][x] = True
    time = [[0]*N for _ in range(N)]
    time[y][x] = 0

    while q:
        y, x = q.popleft()
        if ty == y and tx == x:
            size = graph[ty][tx]
            graph[ty][tx] = 0
            return time[ty][tx], size

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y+dy, x+dx
            if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx] and graph[ny][nx] <= lv:
                q.append((ny, nx))
                visited[ny][nx] = True
                time[ny][nx] = time[y][x] + 1

    return time[ty][tx], size  # 먹은 물고기의 size return


# BFS 돌려서 제일 빨리 만난 거(여러개라면 가장 위, 또 여러개라면 가장 왼쪽) 먹고
def bfs(graph, visited, y, x):
    global lv

    q = deque([(y, x)])
    visited[y][x] = True
    time = [[0]*N for _ in range(N)]
    time[y][x] = 0
    can_eat = []
    flag = False
    while q:
        y, x = q.popleft()
        # print(f'현재위치 {y}, {x} : {graph[y][x]}')

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y+dy, x+dx
            if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx] and graph[ny][nx] <= lv:
                q.append((ny, nx))
                visited[ny][nx] = True
                time[ny][nx] = time[y][x] + 1
                if 1 <= graph[ny][nx] < lv:
                    can_eat.append((time[ny][nx], ny, nx))
                    flag = True

    can_eat.sort(key=lambda x: x[2])
    can_eat.sort(key=lambda x: x[1])
    can_eat.sort(key=lambda x: x[0])
    time, y, x = can_eat[0]
    size = graph[y][x]
    graph[y][x] = 0

    return time, size, y, x


lv = 2
exp = 0
result = 0

# 초기위치 설정
y, x = 0, 0
for i in range(N):
    line = graph[i]
    if 9 in line:
        j = line.index(9)
        y, x = i, j
        graph[i][j] = 0

# 2. bfs 돌려서 계산
while True:

    visited = [[False]*N for _ in range(N)]
    if (len(pos) == 0):
        break
    else:
        time, size, y, x = bfs(graph, visited, y, x)
        result += time
        # 레벨업 로직
        exp += 1
        # print(lv, exp)
        if exp == lv:
            lv += 1
            exp = 0
            # print('lv up')

    pos = cal_pos(graph, lv)
    # print(f'lv:{lv} time:{result}')
    for line in graph:
        # print(line)
        pass
# 3. return
print(result)
