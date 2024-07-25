# 백준 10026번 적록색약

from collections import deque
import sys
sys.stdin = open('python/input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리
N = int(input())
graph = []
graph_blind = []
for _ in range(N):
    line = input().rstrip()
    graph.append(str(line))  # 이거 딥카피인가?
    graph_blind.append(line.replace('G', 'R', line.count('G')))

# print(graph)
# print(graph_blind)

# 2. BFS, BFS_색약


def bfs(y, x, visited):
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = True
    color = graph[y][x]

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < N and 0 <= nx < N) and graph[ny][nx] == color and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))


def bfs_blind(y, x, visited_blind):  # ? 근데 visit을 주든 안 주든 차이가 없는거같은데 뭔가 다른가
    queue = deque([])
    queue.append((y, x))
    visited_blind[y][x] = True
    color = graph_blind[y][x]

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < N and 0 <= nx < N) and graph_blind[ny][nx] == color and not visited_blind[ny][nx]:
                visited_blind[ny][nx] = True
                queue.append((ny, nx))


result = 0
result_blind = 0
visited = [[False]*N for _ in range(N)]
visited_blind = [[False]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x, visited)
            result += 1
        if not visited_blind[y][x]:
            bfs_blind(y, x, visited_blind)
            result_blind += 1


# 3. 결과 출력
print(result, result_blind)
