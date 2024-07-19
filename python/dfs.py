graph = [[],
         [3],
         [9, 8],
         [5, 1],
         [],
         [3, 7, 6],
         [5],
         [5, 9],
         [2, 5, 9],
         [7, 8]]

visited = [False]*len(graph)
visited[0] = True
# visited = [[False] for _ in range(len(graph))]


print(graph, visited)

# def part


def dfs_stack(graph, visited, start):
    # 1. 시작을 stack에 넣고 방문 처리
    stack = []
    print(start)
    stack.append(start)
    visited[start] = True

    # 2. stack top 노드에 대해 방문하지 않은 주변노드가 있으면
    while stack:
        stack_top = stack[-1]
        nodes = graph[stack_top]
        alone = True
        for node in nodes:
            if visited[node] == False:
                stack.append(node)
                print(node)
                visited[node] = True
                alone = False  # 방문하지 않은 주변노드가 있다
                break
        if alone:  # 방문하지 않은 주변노드가 없었다면
            stack.pop()


dfs_stack(graph, visited, 1)
visited = [False]*len(graph)

# 오름차순 탐색 조건 추가
print('--오름차순--')
for line in graph:
    line.sort()
dfs_stack(graph, visited, 3)
visited = [False]*len(graph)


# Recursive 이용
print('--recursive--')


def dfs_rec(start, stack):
    # 1. 현재 노드를 stack에 넣고 방문처리
    visited[start] = True
    stack.append(start)
    print(start)

    # 2. 현재 노드의 주변 노드에 대해서 방문하지 않은 것이 있다면 1번수행
    nodes = graph[start]
    for node in nodes:
        if visited[node] == False:
            dfs_rec(node, stack)

    # 모두 방문시에는 꺼내주기
    stack.pop()


dfs_rec(3, [])
