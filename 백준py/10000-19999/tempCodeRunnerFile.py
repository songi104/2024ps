# 백준 구슬 탈출 2
"""
가장 먼저 생각난 건 backtracking으로 rlud해서 하기
n, m 이 10 이하로 작으니까 가능할 듯

dy = [1,-1,0,0]
dx = [0,0,1,-1]

dfs(num, d, (ry, rx), (by, bx), graph)
    if num == 10:
        return 11
    # 만약에 ry, rx가 이미 그거인 것도 check
    
    res = 11
    for i in range(4): # rlud
        while true: # 따로따로 update해야함..
            if graph[nrx] == "." and graph[nry]==".":
                nrx += dx[i]
                nry += dy[i]

            if graph[nbx] == "." and graph[nby]==".":
                nbx += dx[i]
                nby += dy[i]

            if graph[nbx] == "O" or graph[nby] == "O":
                return 11
            
            if graph[nrx] == "O" or graph[nry] == "O":
                return num + 1

            if (nby == nry):
                if nby - nry > 0: # b가 더 많이 이동
                    nby -= dy[i]
                else:
                    nry -= dy[i]
            elif (nbx == nrx):
                if nbx - nrx > 0:
                    nbx -= dx[i]
                else:
                    nrx -= dx[i]
                
    
"""

import sys
input =sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
for i in range(N):
    for j in range(M):
        if graph[i][j] == "R":
            ry, rx = i, j
        elif graph[i][j] == "B":
            by, bx = i, j
#print(ry, rx, by, bx)

"""
for 0i in range(4): #rlud, 마지막에 새 위치와 그래프로 dfs
    while True:
        #계속 갈 수 있으면 계속 가기 -> .일 대
        # O라면 뭐가 먼저 도착했냐에 따라 결과 return
        # 벽이면 멈추기
        
        # 만약 위치가 같다면... 조정해주고 나가기

    # 새 위치와 살짝 바꾼 그래프로 dfs, 끝나면 다시 바꾸기

"""
def dfs(num, ry, rx, by, bx, graph):
    if num == 11:
        return 11
    
    res = 11
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    #print(f"{num}에 대해 실시")
    for i in range(4):  # 상하우좌
        #print(f"{i} 방향으로 이동")
        nry, nrx, nby, nbx = ry, rx, by, bx
        stop_b = False
        stop_r = False
        while True:  # 따로따로 update해야함..
            if not stop_r:
                nry += dy[i]
                nrx += dx[i]

            if not stop_b:
                nby += dy[i]
                nbx += dx[i]

            #print(nry, nrx, nby, nbx)

            # 계속 갈 수 있으면 계속 가기 -> .일 대
            
            # O라면 일단멈춤
            if graph[nby][nbx] == "O":
                stop_b = True
            if graph[nry][nrx] == "O": 
                stop_r = True

            # 벽이면 멈추기
            if graph[nby][nbx] == "#": 
                nby -= dy[i]
                nbx -= dx[i]
                stop_b = True
                
            if graph[nry][nrx] == "#":
                nry -= dy[i]
                nrx -= dx[i]
                stop_r = True

            if stop_r and stop_b:
                break

        # 만약 위치가 같다면... 조정해주고 나가기
        if (nby == nry and nbx == nrx):
            if graph[nby][nbx] == "O": # 둘다 빠지면 으악
                return 11
            
            # y가 바뀌는 녀석
            if dy[i] != 0:
                if abs(nby - by) > abs(nry - ry):
                    nby -= dy[i]
                else:
                    nry -= dy[i]
            else:
                if abs(nbx - bx) > abs(nrx - rx):
                    nbx -= dx[i]
                else:
                    nrx -= dx[i]

        # 움직일 수 없으면... 다음꺼
        if (nry == ry and nby ==by and nbx == bx and nrx == rx):
            #print("움직일 수 없네요")
            continue

        if graph[nby][nbx] == "O":
            return 11
        if graph[nry][nrx] == "O":
            return num


        # 새 위치와 살짝 바꾼 그래프로 dfs, 끝나면 다시 바꾸기
        graph[ry][rx] = "."
        graph[by][bx] = "."
        graph[nry][nrx] = "R"
        graph[nby][nbx] = "B"
        res = min(res, dfs(num+1, nry, nrx, nby, nbx, graph))
        graph[ry][rx] = "R"
        graph[by][bx] = "B"
        graph[nry][nrx] = "."
        graph[nby][nbx] = "."

    return res
            

res = 11
res = min(res, dfs(1, ry, rx, by, bx, graph))
if res == 11:
    print(-1)
else:
    print(res)