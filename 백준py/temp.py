"""
1. 아이디어
다익스트라

2. 자료구조
edges : int[][]
dist: int[]


3. 시간복잡도
ElogV: 3e5lg(2e4)

"""

import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())

K = int(input())
edges = [[] for _ in range(V+1)]
# print(edges)
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))

# print(edges)

# 다익스트라
hq = [(0, K)]
INF = sys.maxsize
dist = [INF]*(V+1)
dist[K] = 0

while hq:
    ew, eu = heapq.heappop(hq)
    if ew != dist[eu]:
        continue

    for nw, nv in edges[eu]:
        if nw+ew < dist[nv]:
            dist[nv] = nw+ew
            heapq.heappush(hq, (ew+nw, nv))

# print(dist)


# dist 하나씩 출력
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
