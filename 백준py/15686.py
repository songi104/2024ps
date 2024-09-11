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
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
    chickens.append((i, line.count(2)))

print(graph, chickens)


def cal(tlst):
    pass


def dfs(n, tlst):
    global distances

    if n == len(chickens) - 1 or len(tlst) == M:
        distances.append(cal(tlst))
        return

    # 선택

    # 안 선택


distances = []
dfs(0, [])
print(min(distances))
