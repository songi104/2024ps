# 백준 2667번 단지 번호 붙이기
"""
bfs를 한 번 불러서
queue에 들어갈 때마다 cnt 증가시키고
bfs 종료될 때 result에 cnt를 추가

출력:
result.sort()
len(result)
for r in result: print(r)

"""



# 1. 입력
import sys
N = int(input())
graph = []
for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())
#print(graph)
visited = [[False]*N for _ in range(N)]

# 2. bfs 정의
from collections import deque
ds = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = True
    cnt = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in ds:
            ny = y + dy
            nx = x + dx

            if (0<=ny<N and 0<=nx<N) and graph[ny][nx] == '1' and not visited[ny][nx]:
                queue.append((ny,nx))
                cnt += 1
                visited[ny][nx] = True

    result.append(cnt)






# 3. for 문 돌기
result = []

for y in range(N):
    for x in range(N):
        for dy, dx in ds:
            ny = y + dy
            nx = x + dx

            if (0<=ny<N and 0<=nx<N) and graph[ny][nx] == '1' and not visited[ny][nx]:
                bfs(ny, nx)


# 결과 출력
result.sort()
print(len(result))
for r in result: print(r)