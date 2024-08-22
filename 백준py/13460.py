# 백준 13460번 구슬탈출 2
"""
NxM map에 .#ORB가 있다
우리 목표는 빨간구슬이 O에 가도록 하는 것.
하지만 B가 O에 가면 안 된다.
LRUD로 기울일 수 있고 기울이면 구슬이 멈출때까지 움직인다.

장애물은 움직일 수 없으니 그대로 map에 두고 위치만 q에 넣어서 움직여보자.
"""
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
pos = [[], []]  # R, B의 처음 위치
for i in range(N):
    graph.append(input().rstrip())
    if 'R' in graph[i]:
        j = graph[i].index('R')
        pos[0] = (i, j)
        graph[i] = graph[i].replace('R', '.')
    if 'B' in graph[i]:
        j = graph[i].index('B')
        pos[1] = (i, j)
        graph[i] = graph[i].replace('B', '.')
print(graph, pos)

ans = 11
directions = {'R': (0, 1)}
# 계속 기울여보기
while True:

    for d in ['R']  # ['L', 'R', 'U', 'D']:
    if d == 'R':
        # 더 오른쪽에 잇는 것부터 움직인다
        ry, rx = pos[0]
        by, bx = pos[1]
        dy, dx = directions[d]
        if rx >= bx:
            # rx 먼저 움직이기

            else:
                bx 먼저 움직이기

        # 정해진 곳으로 기울이기
        # 가능하다면 위치 저장

    # if 구멍에 파랑 빠짐 종료

    # if 구멍에 빨강 빠짐 종료
    break

if ans == 11:
    print(-1)
else:
    print(ans)
