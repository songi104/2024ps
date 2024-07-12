# 음료수 얼려먹기
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range(N)]


def dfs(x, y):
    # 종료조건 1
    if x < 0 or y < 0 or x >= M or y >= M:
        return False

    # 탐색
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
