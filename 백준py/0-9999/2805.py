# 백준 2805번 나무 자르기
"""
적어도 M미터의 나무를 집에 가져가기 위해
절단기에 설정할 수 있는 높이의 최댓값.

입력
N, M <= 1e6, 2e9
나무의 높이

1. 아이디어
제일 쉬운 방법으로는 그냥 0부터 늘려가면서
res가 M보다 커질 때까지 리스트를 도는거다.
그러면 시간복잡도는 O(NM) = 2e15 절대 불가능
나무를 정렬하면 어떨까? O(N+logN) = 1e6 ㄱㄴ

2. 시간복잡도
O(N+logN)

3. 자료구조
trees = int[]
res = index or mid value

질문. 만약 
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]
res = 0
while start <= end:
    mid = (start+end) // 2
    temp = 0
    for t in trees:
        if mid < t:
            temp += t - mid
    if temp >= M:  # mid를 더 키워봐도 된다
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
