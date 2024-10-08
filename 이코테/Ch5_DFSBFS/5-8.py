# dfs

def dfs(graph=list, v=int, visited=list):
    visited[v] = True
    print(v, end=' ')

    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*len(graph)
# print(visited)
dfs(graph, 1, visited)
