"""
lst pop해서 하기

def dfs(num, tlst):
    종료조건

    for n in tlst:
        dfs(num+1, tlst+[n])
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def dfs(num, tlst):
    if num == M:
        print(*tlst)
        return

    prev = -1
    for n in numbers:
        if prev == n or (tlst and tlst[-1] > n):
            continue
        dfs(num+1, tlst+[n])
        prev = n


dfs(0, [])
