# 백준 1389번 케빈 베이컨의 6단계 법칙
"""
케빈 베이컨 수
모든 친구들과의 몇 단계 통해야 알 수 있는지 계산하기

입력
N M (노드<= 100, 간선<= 5000)
M줄 A, B (양방향)

출력
케빈 베이컨 수가 가장 작은 사람을 출력하기

1. 아이디어
- 입력 받기 graph

2. 자료구조
graph int[][] 처음에는 1로 구성되어있다. 자기자신은 할 필요가 없다.
minimum 받을 때에도 다 1이니까 상관 ㄴㄴ
Floyd 돌면서 graph 업데이트 한다.
res는 N+1개의 int를 가진 list로 각각의 행은 i의 케빈베이컨 수.
제일 작은 res의 index 출력

3. 시간복잡도
N3 -> 1e6

"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
INF = sys.maxsize
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0

# Floyd
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# print(graph)
tmin = INF
res = 0

for i in range(1, N+1):
    tsum = sum(graph[i][1:])

    if tsum < tmin:
        tmin = tsum
        res = i
        # print(f'{i}줄의 sum {tmin}')

print(res)
