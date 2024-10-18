# 백준 18352번 특정 거리의 도시 찾기
"""
입력
N M K X

출력
X에서 시작해서 거리가 K인 도시 오름차순 한 줄에 하나씩 출력

X에서 시작한 모든 거리 계산하면 된다.
hq 이용시 시간 복잡도 ElogV


1. 입출력 처리
2. 다익스트라
3. 결과list 처리
"""
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append((1, b))


def dijk():
    dist = [INF]*(N+1)
    dist[X] = 0
    hq = [(0, X)]

    while hq:
        w, v = heapq.heappop(hq)

        if dist[v] != w:
            continue

        for nw, nv in edges[v]:
            if dist[v] + nw < dist[nv]:
                dist[nv] = dist[v]+nw
                heapq.heappush(hq, (dist[nv], nv))

    return dist


dist = dijk()
no_print = True
for i in range(N+1):
    if dist[i] == K:
        print(i)
        no_print = False

if no_print:
    print(-1)
