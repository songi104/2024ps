# 백준 15686번 치킨배달
"""
1. 아이디어
NxN 도시가 있다. 빈칸, 치킨집, 집 중 하나다.
r,c는 1부터 시작한다.
치킨거리: 집과 가장 가까운 치킨집 사이의 거리
각각의 집은 치킨거리가 있다.
도시의 치킨 거리는 모든 치킨 거리의 합
거리는 가로+세로

치킨집 중 M개를 고르고 나머지는 폐업시킨다.
이 때 치킨거리가 가장 작게 되도록하는 프로그램 작성.

N >=50, M<=13
N개의 줄 도시정보(0-빈칸, 1-집, 2-치킨집)

"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
chickens = []
homes = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

# print(homes)
# print(graph, chickens)


def cal(tlst):
    # 모든 home에 대해서
    # tlst의 모든 store에 대해서 거리 구한다음에
    # min을 결과에 더한다.
    res = 0
    for home in homes:
        # print('home', home)
        td = 2*N
        for store in tlst:
            dist = abs(home[0]-store[0])+abs(home[1]-store[1])
            td = min(dist, td)
        res += td

    return res


def dfs(n, tlst):
    global distances
    # print(n, tlst)
    if n == len(chickens) or len(tlst) == M:
        distances.append((cal(tlst)))
        return

    # 선택
    dfs(n+1, tlst+[chickens[n]])

    # 안 선택
    dfs(n+1, tlst)


distances = []
dfs(0, [])
print(min(distances))
