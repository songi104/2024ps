# 백준 1446번 지름길
"""
입력
N D (지름길<=12, 고속도로길이<=10000)
N개의 줄 시작위치 도착위치 지름길 길이

그냥 한 번 update 쫙 하고 다시 update하는거야..
dp = [i for i in range(D+1)]

일단 edge에 대해서 update한다.
"""

import sys
input = sys.stdin.readline
N, D = map(int, input().split())
edges = []
for _ in range(N):
    s, e, w = map(int, input().split())
    if e > D:
        continue
    edges.append((s, e, w))

edges.sort()

# print(edges)
dp = [i for i in range(D+1)]
# edge에 대한 update
for s, e, w in edges:
    for i in range(D+1):
        if i == e:
            dp[i] = min(dp[i], dp[s]+w)
        elif i != 0:
            dp[i] = min(dp[i], dp[i-1]+1)
print(dp[D])
