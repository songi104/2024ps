# 백준 1916번 최소비용 구하기
"""
N개의 도시, M개의 버스, A에서 B까지 가는 최소 비용찾기

입력
N
M
M줄 s, e, w
A, B

출력
최소비용

1. 아이디어
A에서 다익스트라 (근데 A->B.. bfs로 풀 수 있나?)

2. 자료구조
dist -> 결론 dist[B]
edges : 인접 리스트

3. 시간복잡도
ElogV -> NlogM
1e3*lg(1e5)
1e3*5lg10 -> 15000

"""

import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력 처리

N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    edges[s].append((w, e))
# print(edges)

A, B = map(int, input().split())

# 다익스트라
# - hq에 넣기
# - while hq 동안
#     - 꺼내서 주변 탐색
#     - dist랑 다르면 패스
#     - 만일 더 작은 값이면 update, hq에 넣기

INF = sys.maxsize
dist = [INF] * (N+1)
dist[A] = 0
hq = [(0, A)]

while hq:
    ew, eu = heapq.heappop(hq)

    if ew != dist[eu]:
        continue

    for nw, nv in edges[eu]:
        if ew+nw < dist[nv]:
            heapq.heappush(hq, (ew+nw, nv))
            dist[nv] = ew+nw

print(dist[B])
