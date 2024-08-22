# 백준 1939번 중량 제한
"""
N개의 섬에 M개의 다리가 있다.
한번에 옮길 수 있는 무게의 최댓값을 구하라..






=> 어떤 트럭에 짐을 싣고 공장1에서 공장2까지
가야한다. 이 때 짐의 최댓값을 구한다고 생각해보자.. 가는 경로에 있는 중량제한이 중요하다.

암튼 문제를 트럭에 짐 싣고 가는걸로 생각해서 풀었어
다들 이거 풀었어??





처음에는,,
모든 경로에 대한 중량제한을 구한다.
이러한 제한들의 최댓값을 구한다.
라고 생각했다.
그니까 경로마다마다 중량제한을암튼 패스





그런데 중량제한이 어쨌든 포인트니까
이거에 맞춰서 생각을 해보면
중량을 제한하고 이에 맞는 경로만 가면 어떨까?라고 생각했다.
(그리고 binary search도 써야하니까,,)



1. 입력을 처리해준다
graph 필요!
2. start=0, end=1e9에 대해서
3. bfs를 돌려서 갈 수 있는지 확인해본다.
    중량제한 w >= mid여야 갈 수 있다.
    갈 수 있다면 ans 바꿔주고, 좀 더 키워보자(start를 오른쪽으로 옮겨보자)
    갈 수 없다면 end 왼쪽으로
"""

from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리
N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
f1, f2 = map(int, input().split())

# 지금 그래프가 어떻게 되어있냐면
# 그래프 길이는 N+1이야
# 왜냐하면 공장이 1부터 시작해서..
# (1,3)을 2의 weight로 연결한다고 치면
# graph[1] = [(3,2)] 이런식으로 들어가있어


# 2. 이진탐색
"""
mid에 대해서 bfs를 돌릴건데..
이 mid가 제한이라고 생각하는거야
그러면 중량제한이 mid보다 클 때는 트럭이 갈 수 있고
중량제한(w)가 mid보다 작으면 트럭이 갈 수 없어
그래서 bfs 돌려서 end point에 도달하면 ans를 업뎃해주는걸로 풀었어
"""
# 이제 bfs로 경로를 구해볼게..


def bfs(limit):
    q = deque([f1])
    visited = [False]*(N+1)
    while q:
        now = q.popleft()
        for node in graph[now]:
            nxt, w = node
            if not visited[nxt] and w >= limit:
                q.append(nxt)
                visited[nxt] = True
    return visited[f2]
# 도달했다면 true 리턴하고 아니면 false 리턴


start = 0
end = 1000000000
ans = 0
while start <= end:
    mid = (start+end)//2
    arrived = bfs(mid)
    if arrived:  # 도착한거 그러니까 mid를 좀 더 올려볼수있음 그리고 ans도 업뎃해야함!
        start = mid + 1
        ans = mid
    else:  # 도착을 못했으니까 mid를 낮춰봐야함..
        end = mid - 1

print(ans)
