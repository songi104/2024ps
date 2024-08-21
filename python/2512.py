# 백준 2512번 예산
"""
시간제한 1초 => 2000만번
약간 그리디 깔..

일단 젤 작은걸 상한액으로 배정해보고 조금씩 늘려본다.

입력
N
1줄 N개 예산
예산 total

출력
배정예산 중 최댓값 정수


1. 입력 처리
2. 요청 정렬
3. 젤 작은 놈을 해보기
    가능하면 좀 더 높여본다
    불가능하면 좀 더 줄여본다

edge
만약 전부 안 된다면? 그냥 상한액을 줄이면 됨 -> 상한액 출력
만약 전부 된다면? 상한액이 max를 넘은 순간 그냥 최고를 출력하면 됨


무슨 알고리즘을?
N이 1만이다.. 예산범위는 10만이다 -> 그냥 하나씩 줄이면 안 된다. 확확 줄여야한다.
1만 * log(10만) 쌉가능
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
Rs = list(map(int, input().split()))
total = int(input())

Rs.sort()

start = 0
end = Rs[-1]
ans = 0
while start <= end:  # logN (2N+2)
    mid = (start + end) // 2
    cnt = 0
    for r in Rs:
        if r <= mid:
            cnt += r
        elif r > mid:
            cnt += mid
    if cnt > total:
        end = mid - 1
    elif cnt <= total:
        ans = mid
        start = mid + 1

for r in Rs:  # 2N
    if r < ans:
        continue
    elif r >= ans:
        print(ans)
        break
