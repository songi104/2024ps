# 백준 순열사이클
"""
tlst: 계속 담아서..

"""
T = int(input())
N = int(input())

for _ in range(T):
    lst = list(map(int, input().split()))
    vis = [0]*(N+1)
    res = 0
    for i in range(1, N+1):
        if not vis:
            dfs(i)
    print(res)

def dfs(tlst):
    if len(tlst) and tlst[0] == tlst[-1]:
        res += 1
        return
    
    
    
    