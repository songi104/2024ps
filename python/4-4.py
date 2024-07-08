# 게임개발
import sys

N, M = map(int, sys.stdin.readline().split())
matrix = []
check = [[0 for _ in range(M)] for _ in range(N)]  # 1이면 가본 곳

x, y, s = map(int, sys.stdin.readline().split())
check[x][y] = 1

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 1
flag = True
while flag:
    for _ in range(4):  # step 1. rotate left
        s = s-1
        if s < 0:
            s = 3

        step = steps[s]
        nx, ny = x+step[0], y+step[1]
        if matrix[nx][ny] == 0 and check[nx][ny] == 0:  # 가보지않음
            result += 1
            x, y = nx, ny
            check[x][y] = 1
            break

        if _ == 3:  # 갈 수 있는 곳이 없음
            nx, ny = x-step[0], y-step[1]
            if matrix[nx][ny] == 1 or check[nx][ny] == 1:
                flag = False
                break
            result += 1

print(result)
