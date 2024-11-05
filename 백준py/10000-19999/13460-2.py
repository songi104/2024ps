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
            elif (nbx == nrx):
                if n
                
    
"""

import sys
input =sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
print(graph)