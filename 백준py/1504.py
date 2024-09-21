# 백준 1504번 특정한 최단 경로
"""
-특이사항
방향성이 없음 -> 모든 edge에 s,e에 다 추가해줘야함
1에서 N으로 가는 최단경로를 구해야함


-입력
N E 800, 2e5
E줄 s,e,w
A B (A,B를 거쳐야함)


1. 아이디어
3번의 다익스트라

tw: A->B 가는 최단경로
dist1 : 1에서 출발하는 경로들
distN : N에서 출발하는 경로들

dist1[A] + distN[B] vs dist1[B]+distN[A] 중에 작은 거 선택해서 tw 더하면 됨.

2. 자료구조
def dijk(start):
    return dist
tw = dijk(A)[B]

3. 시간복잡도
3*NlgE (N:800 E:2e5)
24e2*5lg20
12*e3lg20 ~= 12000*5 ~= 60000
"""

# 1. 입출력 처리
import heapq
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))
    edges[v].append((w, u))

A, B = map(int, input().split())


# 2. 다익스트라 정의

INF = sys.maxsize


def dijk(start):
    global edges
    tdist = [INF]*(N+1)
    tdist[start] = 0
    hq = [(0, start)]

    while hq:
        ew, eu = heapq.heappop(hq)
        if ew != tdist[eu]:
            continue

        for nw, nv in edges[eu]:
            if nw+ew < tdist[nv]:
                tdist[nv] = nw+ew
                heapq.heappush(hq, (ew+nw, nv))

    return tdist

# 3. 다익스트라 3번


tw = dijk(A)[B]
dist1 = dijk(1)
distN = dijk(N)

# 4. 비교 후 결과 출력
if tw == INF or dist1[A] == INF or dist1[B] == INF or distN[A] == INF or distN[B] == INF:
    res = -1
else:
    res = tw + min(dist1[A]+distN[B], dist1[B]+distN[A])
print(res)
