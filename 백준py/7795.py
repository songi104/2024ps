# 백준 7795번 먹을 것인가 먹힐 것인가
"""
모든 A에 대해 모든 B를 돌면서
작은 것의 개수를 세면 될 것 같은데...
이렇게 쉽다고? 의심
-> N은 2만 M도 2만
NM일 것 같은데 그러면 400,000,000 => 2초다.. 줄여!!!
NlogN으로 줄여.. 그럼 이건 어때
모든 B에 대해서 B보다 큰 A가 몇 개인지 구하는거다!!

0. res = 0
1. for b in B:
2.    res += 이진탐색(A, b)

입력
T 묶음
N M (A의 수, B의 수)
A의 크기
B의 크기
"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

"""
under보다 큰 원소의 개수가 lst에 몇 개 있는지를 return
"""


def binary_search(lst, under):
    # print('---', under)
    start = 0
    end = N-1
    idx = N
    while start <= end:
        mid = (start+end)//2
        # print(f'mid: {mid}')
        if lst[mid] > under:
            # print(lst[mid], under)
            idx = mid
            end = mid - 1
        else:
            start = mid + 1

    return N-idx


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    # print(A, B)

    res = 0
    for b in B:
        res += binary_search(A, b)
    print(res)
