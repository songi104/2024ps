# 백준 11053번 가장 긴 증가하는 부분 수열
"""
수열 A = {10, 20, 10, 30, 20, 50} 이라면 결과는 {10,20,30,50} 길이는 4이다.

입력
수열 크기 N
한 줄 N개 원소

먼저 든 생각
index i부터
앞에 제일 작은 수부터 시작해서
큰 게 있다면 그걸 더해주면 된다.
근데 그렇다면 N*N-1을 N번정도 하니까 N^3
시간제한 1초에 1000이니까 1,000,000,000
줄여야한다.

정렬을 해야하는가? : 이진탐색
공통적인 게 있는가? : DP

공통적인 게 있다. 맨 뒤에서부터 하면 그냥 저장하면 된다.
d라는 걸 만들어서 index로 접근하고
만약 d에 도착했을 떄 d가 있다면 그걸 그냥 더해주자.

1. for i in range(n-1, -1, -1):
2. i에 대해서 .. 증가하는 수열 계산
    - 만약 d에 있다면 그냥 더해주고
    - 아니라면 돌면서 계산해주기

N^2에 해결 가능하다!
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# print(numbers)
d = [1]*N
for i in range(N-1, -1, -1):
    target = numbers[i]
    prev = target
    for j in range(i+1, N):
        next = numbers[j]
        # print(target, next)

        if target < next and d[i] < 1+d[j]:
            d[i] = 1 + d[j]

print(max(d))
