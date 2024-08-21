# 1939번 중량제한 binary search
"""
이분탐색으로 해보자..
어떤 최대, 최소를 찾는 거고
그 때 bfs 돌려보는거야..

graph)
len = N+1
graph[1] = [(2,3)] // 1번과 2번 섬이 3의 제한으로 연결


1. 0부터 중량제한 max까지
2. bfs 돌린다
    mid인 트럭이 움직인다고 생각하자. 즉, w > mid여야한다.
    이 때 end에 도착할 수 있으면 ans 교체하고 start 늘려보기
    end에 도착할 수 없다면 end를 왼쪽으로
"""

from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리
N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
# print(graph)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

f1, f2 = map(int, input().split())
# print(graph)


def bfs(limit):
    q = deque([f1])
    visited = [False]*(N+1)
    visited[f1] = True
    while q:
        now = q.popleft()
        # print('now', now)
        for nxt, w in graph[now]:
            if not visited[nxt] and w >= mid:
                q.append(nxt)
                visited[nxt] = True
    return visited[f2]


# 2. 이분탐색 + bfs
start = 0
end = 1e9
ans = 0
while start <= end:
    mid = int((start+end)//2)
    arrived = bfs(mid)
    if arrived:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
