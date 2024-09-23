# 백준 1238번 파티
"""
N개의 마을이 있음. X마을에서 파티 할거야. M개의 다리가 있다.
오는 길, 가는 길 다를 수도 있다.
다익스트라 두 번 돌리면 되지 않나?

입력
N, M, X
M줄동안 s, e, t

출력
가장 오래 걸리는 학생의 소요 시간

1. 아이디어
다익스트라 2번

- 가는 길 계산하기
for i in range(1, N+1):
    if i == X: 넘겨
    다익스트라 돌리고 tdist에 저장한다.
    dist1[i] = tdist[X]


2. 자료구조
dist1 = [] : 가는 길, 모든 마을 -> X (dfs)
dist2 = [] : 오는 길, X -> 모든 마을


3. 시간복잡도
N*다익스트라 + 다익스트라 = N다익스트라
다익스트라 : ElogV -> E2lgV
E = 1e3
V = 1e4
E2lgV = 1e6*4*lg10 ~= 1e7 약 천만
"""

# 입력 처리
import heapq
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M, X = map(int, input().split())

edges = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split())
    edges[s].append((t, e))

# print(edges)

INF = sys.maxsize


# 다익스트라 dist1
dist1 = [INF]*(N+1)
dist1[X] = 0

for i in range(1, N+1):
    if i == X:
        continue
    tdist = [INF]*(N+1)
    tdist[i] = 0

    # 다익스트라
    hq = [(0, i)]
    while hq:
        ew, eu = heapq.heappop(hq)  # 시작할 가중치, 시작점 eu
        if ew != tdist[eu]:
            continue

        for nw, nv in edges[eu]:
            if ew + nw < tdist[nv]:
                tdist[nv] = ew+nw
                heapq.heappush(hq, (ew+nw, nv))

    dist1[i] = tdist[X]

# 다익스트라 dist2
dist2 = [INF]*(N+1)
dist2[X] = 0
hq = [(0, X)]

while hq:
    ew, eu = heapq.heappop(hq)
    if ew != dist2[eu]:
        continue
    # print(ew, eu)
    for nw, nv in edges[eu]:
        if ew+nw < dist2[nv]:
            dist2[nv] = ew+nw
            heapq.heappush(hq, (ew+nw, nv))

# print(dist2)


# dist1+dist2하고 최댓값
dist = [0]*(N+1)
for i in range(1, N+1):
    dist[i] = dist1[i] + dist2[i]

print(max(dist))
