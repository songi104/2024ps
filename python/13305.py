# 백준 13305번 주유소
"""
N개의 도시가 있다.
일직선 도로에 있다.
처음 출발할 때는 기름이 없다.
1km마다 1리터 쓴다.
각 주유소마다 기름 가격이 다르다.
최소 비용을 구하라.

1. 아이디어
일단 처음엔 무조건 갈만큼 충전해야한다.
제일 싼 주유소를 만날 때까지 갈 수 있도록 충전.
전부 담고 prev에 넣어서 돌면서 + 한다.


2. 시간복잡도
도시개수 1e5


3. 자료구조
"""

import sys

sys.stdin = open('input.txt' ,'r')
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
liter = list(map(int, input().split()))

prev = liter[0]
cnt = 0


for i in range(N-1):
    now = liter[i]
    if prev > now :
        prev = now
    cnt += prev*dist[i]
    
print(cnt)