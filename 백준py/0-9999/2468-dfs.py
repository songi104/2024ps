"""
dfs 풀이
비의 양 0-100에 대해서
    - 잠긴 곳은 다 visited
    - res = max(solve(visited), res)

solve():
    global visited
    not visited에 대해서 dfs 한 번 돌리면 res += 1
"""

import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def solve(visited):
    t_res = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited = dfs(i,j,visited)
                #print(f"{rain}기준 {i},{j}에서 호출")
                t_res += 1

    return t_res

   

def dfs(i, j, visited):
    """
        dfs는 두가지 구현 방법이 있다: stack, 재귀
        stack은 이렇다.
        1. 탐색 시작 노드를 스택에 삽입하고 방문처리
        2. 최상단 노드에 대해서
            - 방문하지 않은 노드가 있으면 그 노드를 스택에 넣고, 방문처리, break
            - 방문하지 않은 노드가 없으면 그 노드를 pop()
        3. 2번을 계속 반복한다
    """

    visited[i][j] = True
    stack = [(i,j)]

    dy = (1,0,-1,0)
    dx = (0,-1,0,1)
    while stack:
        y, x = stack[-1]
        all_visited = True
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = True
                all_visited = False
                break
        if all_visited:
            stack.pop()
    
    return visited



res = 0
for rain in range(0, 101):
    visited = [[False]*N for _ in range(N)]

    # 잠긴 곳 visit 처리
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                visited[i][j] = True

    res = max(solve(visited), res)
    #print(f"rain:{rain}에서 {res}로 update")

print(res)
