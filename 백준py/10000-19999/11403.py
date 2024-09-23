# 백준 11403번 경로 찾기
"""
가중치 없는 방향 그래프 G.
모든 정점 (i,j)에 대해서 i->j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램

플로이드 쓰는 이유
모든 노드 -> 모든 노드
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i] = [0]+list(map(int, input().split()))
# print(graph)


# 플로이드
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # print(i, j, k)
            if graph[i][k]*graph[k][j] == 1:
                graph[i][j] = 1

for i in range(1, N+1):
    print(*graph[i][1:])
