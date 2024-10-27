# 백준 RGB거리 2
"""
입력
N
N줄 (R, G, B로 칠하는 비용)

번갈아서 칠하되 끝과 끝도 같으면 안 된다.
백트래킹으로 될 것 같아요~

def dfs(num, tlst, cost)
"""

import sys
input = sys.stdin.readline

N = int(input())
lst = [0]
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
#print(lst)

INF = sys.maxsize
def dfs(num, tlst, cost):
    if num == N+1:
        # 종료조건 : 만약 1과 N이 같으면 그냥 종료
        if tlst[0] == tlst[-1]:
            return INF
        #print(cost, tlst)
        return cost

    # tlst[-1]에 따라서 RGB 부르기
    if num == 1:
        # RGB 전부
        tres = []
        tres.append(dfs(num+1, [0], lst[num][0]))
        tres.append(dfs(num+1, [1], lst[num][1]))
        tres.append(dfs(num+1, [2], lst[num][2]))
    else:
        tres = []
        for color in [0,1,2]:
            if color != tlst[-1]:
                tres.append(dfs(num+1, tlst+[color], cost+lst[num][color]))
    
    return min(tres)

res = dfs(1, [], 0)
print(res)
