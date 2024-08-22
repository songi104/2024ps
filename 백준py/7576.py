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


import sys
sys.stdin = open("python/input.txt", "r")




# 1. 입력 처리
M, N = map(int, sys.stdin.readline().split())
graph = []
next_graph = []
visited = [[False]*(M) for _ in range(N)]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split())) 
    graph.append(line[:])
    next_graph.append(line[:])

#print(graph)
#print(next_graph)



# 2. bfs를 돌려서 토마토 익게 만들기. for day in range(MN)
# 이 때 bfs를 더 이상 돌릴 수 없다면 -1 출력
# -> 하지만 그게 전부 익을만큼 익어서 그런 걸 수도

result = 0
ds = [(1,0), (-1,0), (0,1), (0,-1)]
lst_y = {i for i in range(N)}
lst_x = {i for i in range(M)}

import copy

while True:
    #print(result)
    #for i in range(len(graph)):
        #print(graph[i])
    no_bfs = True
    new_lst_y = set()
    new_lst_x = set()
    for y in lst_y:
        for x in lst_x:
            #print(f'{y} {x} 입니다')
            for dy, dx in ds:
                ny = y + dy
                nx = x + dx
                if (0<=ny<N and 0<=nx<M) and graph[y][x] == 1 and graph[ny][nx]==0:
                    next_graph[ny][nx] = 1
                    #print(f"{y} {x} 가 {ny} {nx}에 영향줬습니다")
                    #print(f"graph     : {graph[y]}")
                    #print(f"next_graph: {next_graph[y]}")
                    new_lst_y.add(ny)
                    new_lst_x.add(nx)
                    #print(new_lst_y, new_lst_x)
                    no_bfs = False
    
    
    # 그래프 처리
    graph = copy.deepcopy(next_graph)
    lst_y = set(new_lst_y)
    lst_x = set(new_lst_x)
    result += 1

    if no_bfs:
        cant = False
        for line in graph:
            cant = line.count(0)
            if cant : # 다 못 익음 
                result = -1
                break
        if not cant: result -= 1
        break


# 결과 출력
print(result)