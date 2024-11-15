# 백준 감시
"""
cctvs 안에 있는 cctv를 회전 1,2,3,4한다.
그리고 bfs를 돌려서 사각지대 업뎃.
최소 사각지대를 찾는다.

2. 자료구조
cvs = cctv 위치가 저장되어있음
rotations = cctv별로 몇번 회전인지 있음 0,1,2,3
1번 cctv에 대해서 생각해보자
dy = (0,1,0,1)
dx = (1,0,-1,0)
ny = y + dy


uy = [[1,0,0,0], # 1번 cv
[0,1,0,1] #2번 cv
[1,0,0,1]]
uny = y + uy[tp][i]
dny = y + dy[tp][i]


2번 cctv에 대해서 생각해보자
dy = (0,1,0,1)
dx = ()

dfs(num,rotations)
# 종료조건: num==len(cvs)
return bfs()
"""

"""
갑자기 생각난 방법인데
rt = [1,1,0,0] # 3번 cv
dy = (0,1,0,1)
dx = (1,0,-1,0)

uy = uy - rt[0]
rx = rx + rt[1]
dy = dy + rt[2]
lx = lx - rt[3]

이렇게 하니까
for i in range(4):
    uy = uy - rt[(i+0)%4]
    rx = rx + rt[(i+1)%4]
    dy = dy + rt[(i+2)%4]
    lx = lx - rt[(i+3)%4]

그럼 i = 0 일 때는 0,1,2,3
1일 때는 1,2,3,0

"""


import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
#print(graph)

cvs = []
for i in range(N):
    for j in range(M):
        if 1<=graph[i][j]<=5:
            cvs.append((i,j))
print(cvs)

rt = [1, 1, 0, 0]  # 3번 cv

rotations = [(1,0,0,0), (1,0,1,0), (1,1,0,0), (1,1,1,0), (1,1,1,1)]
dy = (0, 1, 0, 1)
dx = (1, 0, -1, 0)
#for i in range(4):
#    print(rt[tp][(i+0) % 4], rt[(i+1) % 4], rt[(i+2) % 4], rt[(i+3) % 4])
from copy import deepcopy
from collections import deque

"""
for i in range(4):
    dy[i]*rotations[(i+tlst[k])%4]

"""

def calculate(tlst):
    rotations = [(0), (1, 0, 0, 0), (1, 0, 1, 0), (1, 1, 0, 0),
                 (1, 1, 1, 0), (1, 1, 1, 1)]
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    t_graph = deepcopy(graph)

    for k in range(len(cvs)):
        print(f"{k}번째 cctv에 대해서 q 돌려요")
        vis = [[False]*M for _ in range(N)]
        i, j = cvs[k]
        tp = graph[i][j]
        q = deque([(i,j)])
        vis[i][j] = True
        cnt = 0
        while q:
            cnt += 1
            y, x = q.popleft()
            for i in range(4):
                print(f"y방향으로 {dy[i]*rotations[tp][(i+tlst[k]) % 4]}, x방향으로 {dx[i]*rotations[tp][(i+tlst[k]) % 4]}")
                ny = y + dy[i]*rotations[tp][(i+tlst[k]) % 4]
                nx = x + dx[i]*rotations[tp][(i+tlst[k]) % 4]
                if 0<=ny<N and 0<=nx<M and not vis[ny][nx]:
                    print(ny, nx)
                    if t_graph[ny][nx] == 6:
                        vis[ny][nx] = True
                        continue
                    vis[ny][nx] = True
                    t_graph[ny][nx] = tp
                    q.append((ny, nx))
                    for line in t_graph:
                        print(line)
                    print("---")
                            
            
            # print("---")
            # if cnt == 3:
            #     break

    # dfs 버전
    """
    stack에 넣고
    위에를 보고 
    """



    # 0을 다 세
    res = 0
    for i in range(N):
        for j in range(M):
            if t_graph[i][j] == 0:
                res += 1

    return res

def dfs(num, tlst):
    if num == len(cvs):
        print("caluc")
        return calculate(tlst) # 계산함수
    
    t_res = N*M
    # 이번 cv를 4번 돌려줍니다
    for i in range(4):
        print(f"{num} cv를 {i} 돌렸어요")
        tlst[num] = i
        t_res = min(t_res, dfs(num+1, tlst))

    return t_res


res = N*M
res = min(res, dfs(0,[0]*len(cvs)))
print(res)

# cctv는 cctv를 통과할 수 있다
# edge: cv가 없음. or cv만 있음