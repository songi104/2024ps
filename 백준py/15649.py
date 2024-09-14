#
"""
1. 아이디어
recursive, 백트래킹


2. 시간복잡도
<= 8

3. 자료구조
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False]*(N+1)
ans = []


def recur(num, lst):
    if num == M:  # 종료조건 및 정답처리
        ans.append(lst)
        return

    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = True
            recur(num+1, lst+[j])
            visited[j] = False


recur(0, [])

# 정답 프린트
for lst in ans:
    print(*lst)
