# 백준 15683번 감시
"""
cvs: cctvs 좌표
rot: 회전 방향
tlst: cctvs 회전방향을 담음

"""
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [6]*(M+2)
for _ in range(N):
    graph.append([6]+list(map(int, input().split()))+[6])
visited = [[False]*(M+2) for _ in range(N+2)]
cvs = []
for i in range(1, N+2):
    for j in range(1, M+2):
        if 1 <= graph[i][j] <= 5:
            cvs.append((i, j))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
direction = [[], [1], [1, 2], [0, 1], [0, 1, 3], [0, 1, 2, 3]]]

    def cal(tlst):
    # 모든 CCTV에 대해서 처리
    for i in range(CNT):
        si, sj= cvs[i]
        rot= tlst[i]
        tp= cvs[i]

        # type에 따라 방향으로 뻗어나가면서 visited에 표시
        for dr in direction[tp]:
            dr= (dr+rot) % 4
            ci, cj= si, sj
            while True:
                ci, cj= ci+dy[dr], cj+dx[dr]
                if graph[ci][cj] == 6

    pass


    def dfs(n, tlst):
    global ans
    if n == CNT:
        ans= min(ans, cal(tlst))
        return
    dfs(n+1, tlst+[0])  # 0도 회전
    dfs(n+1, tlst+[1])  # 90도 회전
    dfs(n+1, tlst+[2])  # 180도 회전
    dfs(n+1, tlst+[3])  # 270도 회전


    CNT = len(cvs)
    ans = N*M
    dfs(0, [])
    print(ans)
