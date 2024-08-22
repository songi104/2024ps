# 백준 10026번 적록색약
# 더 줄여보자!

from collections import deque
import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리
N = int(input())
graph = [[-1]*(N+2) for _ in range(N+2)]
graph_blind = [[-1]*(N+2) for _ in range(N+2)]
match = {'R': 0, 'G': 1, 'B': 2}  # 방문한 곳은 -1로 바꾸기
match_blind = {'R': 0, 'G': 0, 'B': 2}

for i in range(N):
    line = input().rstrip()
    graph[i+1][1:N+1] = ([match[s] for s in line])  # 이거 딥카피인가?
    graph_blind[i+1][1:N+1] = ([match_blind[s] for s in line])


# 2. BFS, BFS_색약

def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    color = graph[y][x]
    graph[y][x] = -1

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if graph[ny][nx] == color:
                graph[ny][nx] = -1
                queue.append((ny, nx))


def bfs_blind(y, x):
    queue = deque([])
    queue.append((y, x))
    color = graph_blind[y][x]
    graph_blind[y][x] = -1

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if graph_blind[ny][nx] == color:
                graph_blind[ny][nx] = -1
                queue.append((ny, nx))


result = 0
result_blind = 0


for y in range(1, N+1):
    for x in range(1, N+1):
        if graph[y][x] != -1:
            # print(f'{y} {x} 에서 bfs 돌립니다')
            bfs(y, x)
            result += 1
        if graph_blind[y][x] != -1:
            bfs_blind(y, x)
            result_blind += 1


# 3. 결과 출력
print(result, result_blind)
