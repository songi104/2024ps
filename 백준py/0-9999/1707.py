# 백준 이분그래프
"""
이번이 1,-1인지에 대해서
이번이 1이면 다음은 vis[next_n] = -1
이런식으로 가다가..
이번이 1인데 next가 1이면 return False
false 받으면 계속 return false


edge case:
1. 만일 그래프가 끊어져있다면? 모든 것에 대해서 돌려야함.
"""



import sys
input = sys.stdin.readline

K = int(input())

def dfs(num):
    stack = [num]
    visited[num] = 1

    while stack:
        # 1. 시작 노드 방문 처리 및 스택에 넣기
        # 2. 탑노드의 주변에 대해서
        #     - 방문하지않았으면 방문처리후 스택에 넣기
        #     - 모두 방문했다면 stack에서 빼기
        top = stack[-1]
        all_vis = True
        if top in graph:
            for n_node in graph[top]:
                if visited[n_node] == 0:
                    visited[n_node] = 1 if visited[top] == -1 else -1
                    stack.append(n_node)
                    all_vis = False
                elif visited[n_node] == visited[top]:
                    return False
        if all_vis:
            stack.pop()
    return True




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
    for i in range(1, V+1):
        if visited[i] == 0:
            res = dfs(i)
        if not res:
            break

    if res:
        print("YES")
    else:
        print("NO")

    # print(visited)
    # print(graph)