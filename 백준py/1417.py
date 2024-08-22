# 백준 1417번 국회의원 선거
"""
가장 많은 득표수를 가져야한다.

모든 득표수를 reverse=True해서 정렬한다.
그리고 처음에서 하나씩 계속 뺀다.
그리고 또 다시 정렬한다.
max(0번 혹은 -1번)이 다솜이보다 적으면 된다.

edge case:
다솜 혼자 후보일 때
"""

import sys
from heapq import heappush, heappop, heapify

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
heap = []

# 다솜 기호 1번 처리
dasom = int(input())
cnt = 0


for _ in range(N-1):  # nlogn
    num = int(input())
    heap.append((-num, num))


heapify(heap)
# print(heap)

if N == 1:
    print(0)
else:
    while heap[0][1] >= dasom:
        a, b = heappop(heap)
        heappush(heap, (a+1, b-1))
        dasom += 1
        cnt += 1
        # print(heap)
    print(cnt)


# 2번째 풀이
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
lst = []

# 다솜 기호 1번 처리
dasom = int(input())
cnt = 0

for _ in range(N-1):
    lst.append(int(input()))
lst.sort()  # 오름차순

if lst:
    while lst[-1] >= dasom:
        lst[-1] -= 1
        dasom += 1
        cnt += 1
        lst.sort()

print(cnt)
