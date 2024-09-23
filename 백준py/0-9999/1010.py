# 백준 1010번 다리 놓기
"""
다리를 N개 지을 것이다.
근데 M개 중에 N개를 고르면 알아서 한다.
즉 m C n 개수를 구하는 문제임!

1. 처음 든 생각
5C3 생각했을 때 5!/3!2!이다.
그래서 for문으로 분자를 돌리면 밑에는 memoization 된다고 생각함.
일단 해보자!


for 

입력
T
N M (서쪽과 동쪽)
"""

# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


# def facto(x):
#     if x == 0 or x == 1:
#         return 1
#     return x*facto(x-1)


# def comb(n, r):
#     res = facto(n)/(facto(n-r)*facto(r))

#     return res


# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     print(int(comb(M, N)))

# print(facto(10)/facto(3)/facto(7))
# print(facto(10)/facto(3)/facto(7))

# 2번째 풀이 DP


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def facto(x):
    global d
    if x == 0 or x == 1:
        return 1
    if d[x] != 1:
        return d[x]
    d[x] = x*facto(x-1)
    return d[x]


def solve(n, r):
    res = facto(n)/(facto(r)*facto(n-r))
    return int(res)


T = int(input())
d = [1]*31

for _ in range(T):
    N, M = map(int, input().split())
    print(solve(M, N))
