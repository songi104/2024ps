# 백준 알고리즘 수업 깊이 우선 탐색 1
"""
이렇게 된 거 stack말고 재귀로 구현해보겠다...
"""
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# print = sys.stdout.write


N, M, R = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in graph:
    graph[k].sort()



def dfs(start, cnt):
    # 1. 방문했다면 return
    # 2. 방문하지 않았다면 기록해주고
    # 3. next_node에 대해서 재귀
    if vis[start] != 0:
        return cnt
    
    vis[start] = cnt
    cnt += 1
    for n_node in graph[start]: # 작동이유: defaultdict
        cnt = dfs(n_node, cnt)

    return cnt

    

vis = [0]*(N+1)
dfs(R,1)
for i in range(1, N+1):
    print(vis[i])