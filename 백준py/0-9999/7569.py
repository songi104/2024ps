# 백준 토마토 7569번
"""
입력
M N H (가로, 세로, 높이)
N개의 줄 토마토 x H번(가장 밑부터)
1-익은, 0-익지않은, -1빈칸

출력
모두 익을 때까지 최소 며칠이 걸리는지
저장될떄까지 모두 익어있다면 0
모두 익지못한다면 -1


1. 자료구조
graph: 토마토 저장.
tomatoes: 토마토 있는 곳 저장한 deque


def bfs(tomatoes):
    global graph
    q = deque(tomatoes)

    return True/False (if 변한 게 없으면 False)

while :
    change = bfs(): # 변한 게 없으면 더 못하는건지 check
    if all 1:
        if no_change:
            
        else:
            print(res)
        break
    res += 1
bfs를 돌리고
bfs몇번 돌리는지 
"""

from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
for h in range(H):
    graph[h] = [list(map(int, input().split())) for _ in range(N)]
# print(graph)

# tomato 있는 곳 넣기
tomatoes = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 1:
                tomatoes.append((h, i, j))

# print(tomatoes)


def bfs(graph, tomatoes):
    q = deque(tomatoes)
    print(q)
    visited = [[[False]*M for _ in range(N)] for _ in range(H)]
    for tmt in tomatoes:
        h, i, j = tmt
        visited[h][i][j] = True

    while q:
        h, y, x = q.popleft()

        for dh in [+1, -1, 0]:
            nh = h + dh
            if dh == 0 and 0 <= nh < H:
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny = y+dy
                    nx = x+dx
                    if 0 <= ny < N and 0 <= nx < M and graph[nh][ny][nx] == 0 and not visited[nh][ny][nx]:
                        # tmt에 추가
                        graph[nh][ny][nx] = graph[h][y][x]+1
                        visited[nh][ny][nx] = True
                        q.append((nh, ny, nx))
            elif 0 <= nh < H:
                if graph[nh][y][x] == 0 and not visited[nh][y][x]:
                    visited[nh][y][x] = True
                    graph[nh][y][x] = graph[h][y][x]+1
                    q.append((nh, y, x))
            else:
                continue
            # print(graph)
    # print('===')
    # print(graph)
    # print(new_tmt)
    # print(graph)
    return graph


def check(graphs):
    for graph in graphs:
        for line in graph:
            for n in line:
                if n == 0:
                    return False

    return True


if check(graph):  # 다 익어있음
    print(0)
else:
    graph = bfs(graph, tomatoes)

ans = -1
for box in graph:
    for line in box:
        for n in line:
            if n == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(line))
print(ans-1)
