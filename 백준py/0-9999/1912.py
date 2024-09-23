# 백준 1912번
"""
n <= 100,000


1. 이중 for문
O(10,000,000,000) 2500만 넘음

2. 새로운 거
이진탐색? -> 정렬되어있어야 가능하다
dp로 해보자..
내 무기는 이진탐색, dp, bfs니까..
bfs도 해볼만한디?

=> dp[i]를 i번째 요소에서 끝나는 최대 부분합이라고 정의한다.
"""

# 아이디어!! 혹시 튜플로 어떤 인덱스부터 시작했는지 저장하면 어떨까?

# import sys

# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# n = int(input())
# lst = list(map(int, input().split()))

# dp = [0]*n
# dp[0] = lst[0]


# def solve(n):
#     if dp[n] != 0 or n == 0:
#         return dp[n]
#     dp[n] = max(solve(n-1)+lst[n], lst[n])
#     return dp[n]


# res = solve(n-1)
# print(max(dp))

# 처음부터 ㄱ ㄱ
"""

"""


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

dp = [0]*N
dp[0] = lst[0]

if max(lst) < 0:
    print(max(lst))

else:
    for i in range(1, N):
        dp[i] = max(0, dp[i-1]+lst[i])
    print(max(dp))
