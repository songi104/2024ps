# 백준 알고리즘 수업 깊이우선탐색1

N, M, R = map(int, input().split())
graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

for k in graph:
    graph[k].sort()

vis = [0]*(N+1)
vis[R] = 1
stack= [R]
cnt = 2
while stack:
    now = stack[-1]
    all_visited = True
    if now in graph:
        for next in graph[now]:
            if not vis[next]:
                stack.append(next)
                vis[next] = cnt
                cnt +=1
                all_visited = False
                break
    if all_visited:
        stack.pop()

for s in vis[1:]:
    print(s)