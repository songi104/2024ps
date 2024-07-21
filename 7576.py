# 백준 7576번 토마토
"""
익은 토마토의 근처에 있는 토마토는 하루가 지나면 영향을 받아 익는다.
창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소일수를 알고싶다.

입력:
M N
N줄 (1: 익토 0: 안익토 -1:토마토x)

출력:
최소날짜( 0이상. 못 익는다면 -1 )


못익은 경우는 어제와 오늘이 똑같다면 -1을 출력


"""

# 1. 입력 처리
import sys
M, N = map(int, sys.stdin.readline().split())
graph = [ []*(M) for _ in range(N) ]
visited = [[False]*(M) for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split())) 

print(graph)


# 2. bfs를 돌려서 토마토 익게 만들기. for day in range(MN)
# 이 때 bfs를 더 이상 돌릴 수 없다면 -1 출력
# -> 하지만 그게 전부 익을만큼 익어서 그런 걸 수도
next_graph = [[]*(M) for _ in range(N)]
result = 0
while True:
    no_bfs = True
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1: 
                bfs(y, x)
                no_bfs = False
    # 그래프 처리
    graph = next_graph
    result += 1

    if no_bfs: 
        result = -1
        break


# 결과 출력
