# 백준 1920번

"""
그냥 하면 NM = 1e10
logNM = 10log10
ㄱㄴ

"""

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

M = int(input())
targets = list(map(int, input().split()))


def bs(target):
    global numbers
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if numbers[mid] < target:
            start = mid + 1
        elif numbers[mid] > target:
            end = mid - 1
        else:

            return 1
    return 0


for t in targets:
    print(bs(t))
