# 백준 테트리스 게임 4920번
"""
blocks를 1로 표시하고
회전을 0,1,2,3 표시하고

"""


# blocks = [[[1],[1],[1],[1]], 
#           [[1, 1, 1, 1]],
#         [[1,1,0],[0,1,1]], # block2
#         [[0,1],[1,1],[1,0]], 
#         [[1, 1, 1],[0, 0, 1]],[[1, 0, 0],[1, 1, 1]],  # block 3
#         [[1,1],[1,0],[1,0]],[[0,1],[0,1],[1,1]] ,
#         [[0,1,0],[1,1,1]],[[1,0],[1,1],[1,0]], # block 4
#         [[1,1,1],[0,1,0]],[[0,1],[1,1],[0,1]],
#         [[1,1],[1,1]]] # block 5

blocks = [[(0,0), (0,1), (0,2), (0,3)], # block 1
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (0, 1), (1, 0), (1, 2)], # block 2
          [(0, 1), (1, 0), (1, 1), (2, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)], # block 3
          [(0, 0), (0, 1), (1,0), (2,0)],
          [(2, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (1,0), (1,1), (1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],  # block 4
          [(1, 0), (1, 1), (1, 2), (0, 1)],
          [(0, 0), (1, 0), (2, 0), (1, 1)],
          [(0, 1), (1, 1), (2, 1), (1, 0)],
          [(0, 1), (1, 1), (0, 0), (1, 0)]] # block 5
import sys
INF = sys.maxsize
def solve(i, j):
    res = -INF
        
    for block in blocks:
        #print(block)
        cnt = -INF
        for dy, dx in block:
            ny, nx = dy+i, dx+j
            if ny >= N or nx >= N or ny < 0 or nx < 0:
                cnt = -INF
                break
            cnt += graph[ny][nx]
        res = max(cnt, res)
    return res



t = 0
while True:
    t += 1
    N = int(input())
    graph = []
    if (N == 0):
        break
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    res = 0
    for i in range(N):
        for j in range(N):
            res = max(res, solve(i,j))
    print(f'{t}. {res}')

