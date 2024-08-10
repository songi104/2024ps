# 백준 2839 설탕배달
"""
1. 아이디어
5를 최대부터 줄여가면서 3으로 되는지 해본다.
안 된다면 3만 해보고 그것도 안 된다면 -1이다.
- 5로 나눴을 때 몫 구하기
- range(5,0)으로 3으로 같이 되는지 해보기
- 안된다면 3만 해보기

- 반례: 5보다 작은 경우 생각해보기!
"""


import sys

input = sys.stdin.readline
N = int(input())

max5 = N // 5
cnt = 0
for i in range(max5, -1, -1):
    cnt  = i
    rest = N - i*5
    cnt += rest // 3
    rest = rest % 3
    if (rest == 0):
        break

if (rest != 0) : print(-1)
else: print(cnt)