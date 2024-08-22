# 백준 1939번 중량제한
"""
N개의 섬.

입력
N, M
M개의 줄: A B C (A와 B 사이에 중량제한 C인 다리 존재)
공장있는 섬

모든 경로에 대해서 경로의 중량제한(즉, 경로의 최솟값)의 최대를 구해라.
1. dfs로 모든 경로 탐색
2. 경로 하나에 대해서 min 값을 update 해주고 mins에 저장
3. min의 최대 구하기
-> 근데 너무 어렵다

이분탐색으로 해보자..
어떤 최대, 최소를 찾는 거고
그 때 bfs 돌려보는거야..


"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. 입력처리
N, M = map(int, input().split())
graph = {}
for _ in range(M):
    a, b, c = map(int, input().split())

    if a in graph:
        graph[a].append([b, c, False])
    else:
        graph[a] = [[b, c, False]]

    if b in graph:
        graph[b].append([a, c, False])
    else:
        graph[b] = [[a, c, False]]

start, end = map(int, input().split())

# print(graph)
# 2. dfs 돌면서 mins에 저장


mins = []


def dfs():
    stack = []
    stack.append(start)
    while stack:
        top = stack[-1]
        if top == end:
            # mins.append(limit)
            stack.pop()


def dfs():
    stack = []
    stack.append((start, 0, 0))
    while stack:
        # print(stack)
        top, w, exp = stack[-1]
        if top == end:
            mins.append(exp)
            # print(mins)
            exp -= w
            stack.pop()
            continue

        all_visited = True
        if graph[top]:
            # print(f'{top}에 대한 주변 {graph[top]}')
            for node in graph[top]:
                nxt, w, visited = node
                if not visited:  # 방문하지않음
                    stack.append((nxt, w, min(w, exp)))
                    # print(exp)
                    node[2] = True
                    all_visited = False
                    break

        if all_visited:
            top, w, visited = stack.pop()
            exp -= w


dfs()


# 3. mins 중에 max
print(max(mins))
