# 백준 1987번 알파벳
"""
bfs 돌리면 안 되나?
근데 지금껏 지나온 걸 저장해둬야하기 때문에 
백트래킹이 더 나은 듯

시간초과: list대신 set을 사용.

"""


import sys
input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]



def dfs(y, x, vis):
    # 범위 체크 return len(vis)
    # 할 필요 없는 것 같기도

    # 상하좌우로 가는데 갈 수 있을 때만 간다.
    dy = (1, -1, 0, 0)
    dx = (0, 0, 1, -1)
    cnt = len(vis)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<=ny<R and 0<=nx<C and not graph[ny][nx] in vis):
            vis.add(graph[ny][nx])
            cnt = max(cnt, dfs(ny, nx, vis))
            vis.remove(graph[ny][nx])
    
    return cnt


vis = set(graph[0][0])  # vis의 값이 cnt임
#print(len(vis))
print(dfs(0, 0, vis))