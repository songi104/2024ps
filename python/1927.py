# 백준 1927번 최소 힙
"""
연산개수 N
N 줄

자연수: 배열에 x라는 값 추가
0: 가장 작은 값 출력
"""

from heapq import heappush, heappop
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    elif x > 0:
        heappush(heap, x)
