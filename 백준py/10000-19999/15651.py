# 백준 N과 M (3)
"""
1부터 N까지 중에 M개를 고른다
같은 수 여러번 골라도 됨
dfs(num, tlst):

1번 숫자로 뭘 고를래? for i in range(1, N+1):
len(tlst) == M 되면 return
"""


N, M = map(int, input().split())


def dfs(tlst):

    if len(tlst) == M:
        print(*tlst)
        return
    
    for i in range(1, N+1):
        dfs(tlst+[i])

dfs([])
