# 백준 1003번 피보나치 함수
"""
입력
T
N

출력
0출력횟수 1출력횟수

대충 보고 든 생각: 그냥 피보나치 구현해서 내가 세면 어때?
그냥 하면 시간복잡도가 2^N 이다.. 그러니까 dp를 이용해야한다!
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solve(n):
    print(f'fibo {n}')
    global d
    res = [0, 0]

    if d[n] != [0, 0]:
        return d[n]

    fibo_minus_1 = solve(n-1)
    fibo_minus_2 = solve(n-2)
    res[0] = fibo_minus_1[0] + fibo_minus_2[0]
    res[1] = fibo_minus_1[1] + fibo_minus_2[1]

    d[n] = res
    return res


d = [[0, 0] for _ in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]

T = int(input())
for _ in range(T):
    N = int(input())
    solve(N)
    print(d[N][0], d[N][1])
