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

"""


import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

dp = [0]*n
dp[0] = lst[0]


def solve(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = max(solve(n-1), solve(n-1)+lst[n], lst[n])
    print('dp', n, dp[n])
    return dp[n]


res = solve(n-1)
print(res)
