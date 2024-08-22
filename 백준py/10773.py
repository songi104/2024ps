"""백준 10773번 제로
K
K개 줄
0을 부르면 최근 수를 지운다 -> stack = list 사용
O(2N)

- 시간복잡도 확인하기
"""

import sys
input = sys.stdin.readline

K = int(input())
result = []

for _ in range(K):
    d = int(input())
    if d == 0 : result.pop()
    else: result.append(d)

print(sum(result))