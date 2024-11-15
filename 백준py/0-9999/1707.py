# 백준 이분그래프
"""
이번이 1,-1인지에 대해서
이번이 1이면 다음은 vis[next_n] = -1
이런식으로 가다가..
이번이 1인데 next가 1이면 return False
false 받으면 계속 return false

"""



import sys
input = sys.stdin.readline

K = int(input())

def dfs(num):
    now = visited[num]
    if num in graph:
        next_nodes = graph[num]
        for n_node in next_nodes:
            if visited[n_node] == 0: # 방문 안함
                visited[n_node] = 1 if now == -1 else -1
            elif visited[n_node] == now:
                return False



for _ in range(K):
    V, E = map(int, input().split())
    
    graph = {}
    for i in range(E):
        a, b = map(int, input().split())
        
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    visited = [0]*(V+1)
    res = dfs(1)
    if res:
        print("YES")
    else:
        print("NO")

    print(graph)