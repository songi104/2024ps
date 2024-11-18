# 백준 텀프로젝트
"""
1부터 N까지 쭉 이동한다.. 그러다가 시작이랑 만나는 순간 끝낸다.
int[] vis
만일 dfs에서 방문했으면 안 된다.

dfs(tlst):
    now = tlst[-1]
    if vis[now]:
        return False

    if lst[now] = tlst[0]:
        return True
    
    vis[now] = True
    tres = dfs(tlst+[lst[now]])
    return tres

시간복잡도: N*N -> 10**10
줄여야한다. tlst 중간에 있다면 그걸 끊는 것도 될 듯.
"""

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
T = int(input())

def dfs(tlst, t_vis):
    now = tlst[-1]
    nxt = lst[now]

    if t_vis[now]:
        return []
    t_vis[now] = True

    if not t_vis[nxt]:
        return dfs(tlst+[nxt], t_vis)
    else: # 방문했다면
        try:
            idx = tlst.index(nxt)
            return tlst[idx:]
        except:
            return []

for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    #print(lst)

    vis = [False]*(N+1)
    for i in range(1, N+1):
        if not vis[i]:
            #print(f"dfs{i} 호출")
            t_vis = vis[:]
            team = dfs([i], t_vis)
        for j in team:
            # if vis[j]:
                #print(f"{i}번째 확인중. {j}에서 오류 발생. {team}")
            vis[j] = True
    print("답", vis.count(False)-1)
