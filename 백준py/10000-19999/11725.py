# 백준 11725번 트리의 부모 찾기
"""
graph는 인접리스트 사용

1. 아이디어
dfs 사용하자.
다음 node에 대해서 not visited일 경우
result에 now로 update

2. 자료구조
graph: int[] 인접리스트
result: int[] 결과저장
visited: int[] F/T

3. 시간복잡도
dfs일때 N에 대한 시간복잡도..겠지뭐
O(N) <= 100000 ㄱㄴ

"""

import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)


# dfs 부분


def dfs(now):
    visited = [False]*(N+1)
    result = [0]*(N+1)

    visited[now] = True
    stack = [now]

    while stack:
        now = stack.pop()
        for child in graph[now]:
            if not visited[child]:
                visited[now] = True
                result[child] = now
                stack.append(child)

    return result


result = dfs(1)

for i in range(2, N+1):
    print(result[i])
