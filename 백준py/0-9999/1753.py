# 백준 1753번 최단경로
"""
1. 아이디어
한 점에서 다른 모든 정점으로의 최단 경로를 구하는 문제.
한 점 -> 다른 모든 정점 : 다익스트라 이용
dist = [INF] * (V+1)
edge = [ [] for _ in range(V+1) ] : 인접리스트

- 초기값 세팅
- 힙 있으면 힙에서 하나 빼서 주변 노드 update
    - 만약 다르면 continue
    - dist에 있는 기존값보다 작으면 update하고 hq에 넣기
- 출력



2. 시간복잡도

3. 자료구조
"""

import heapq
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

edges = [[] for _ in range(V+1)]
dist = [INF]*(V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))
# print(edges)

# 초기값 세팅
hq = [(0, K)]
dist[K] = 0

while hq:
    ew, eu = heapq.heappop(hq)
    if ew != dist[eu]:
        continue
    # print(ew, eu)
    for nw, nv in edges[eu]:
        # print(nw, nv)
        if ew + nw < dist[nv]:
            dist[nv] = ew+nw
            heapq.heappush(hq, (ew+nw, nv))

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
