# 백준 1715번 카드정렬하기
"""
1. 문제

2. 아이디어
계속계속 제일 작은 걸 더해가면 된다.

3. 시간복잡도
N^2-> 1e10이니까 100초인데
그러면 NlogN으로 줄여야한다


"""

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)
# print(lst)
result = 0
temp = 0
a = lst.pop()
b = lst.pop()
temp = a+b
result += temp
target = []
while len(lst) > 1:
    while len(target) == 3:
        target.append(lst.pop())
    target.sort()
    # print(target)
    a, b, temp = target
    result += (a+b)

result += temp
if lst:
    result += lst[0]
print(result)
