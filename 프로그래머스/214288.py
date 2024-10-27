# 프로그래머스 상담원 인원


# i번쨰 유형에 j명 있을 때 걸리는 시간
def calc(i, j, reqs):
    lst = reqs[i]
    avail = [0]*j
    ans = 0
    for a, b in lst:
            if avail[0] <= a:
                avail[0] = a+b  # 끝나는 시간 저장
            else:  # 기다려야함
                ans += avail[0] - a
                avail[0] = avail[0]+b
            avail.sort()
    return ans



import sys
INF = sys.maxsize



"""
1. 아이디어
dp = K * N-K+1
dp[i][j] i번째 유형에 j명이 있을 때 걸리는 시간.
dp 다 계산한 다음에
각각의 tlst(멘토묶음)에 대해서 전부 더해서 최소 구하면 될 듯.

"""

from collections import defaultdict

def solution(k, n, reqs):
    # type req
    type_reqs = defaultdict(list)
    for a,b,c in reqs:
        type_reqs[c].append((a,b))

    wait_times = [[INF]*(n-k+1) for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n-k+1):
            wait_times[i][j] = calc(i, j, type_reqs)

    answer = dfs(n-k, [0]+[1]*k, INF, reqs)
    return answer

