# 백준 2108번 통계학
"""
입력:
N
N개의 줄

출력:
산술평균-소수점이하 첫재자리 반올림
중앙값-증가하는순서에서 가운데
최빈값-여러개있을때에는 두번째로 작은값
범위-최대-최소

numbers_sorted를 만들자


궁금한 점:
max, min, sum의 시간복잡도
올림내림반올림int
배열 튜플 기준 정렬 => lambda 이용
최빈값 다르게 구하는 법?

잘한 점:
Radix sort 이용하였다.

실수:
(N+1)/2 - 1 = float이다
items 길이가 1일 때는 2개인 것을 신경쓰지 않아도 된다. IndexError

"""

import sys

N = int(sys.stdin.readline())
numbers = []
count = {}

for _ in range(N):
    n = int(sys.stdin.readline())
    numbers.append(n)
    if n not in count.keys(): count[n]=1
    else: count[n] += 1

print(round(sum(numbers)/N))
numbers.sort()
print(numbers[int((N+1)/2-1)])

# 최빈값 구하는 코드
items = list(count.items())
items.sort(key=lambda x:x[0])    
items.sort(key=lambda x:x[1], reverse=True)    
if len(items) > 1 and items[0][1] == items[1][1]: print(items[1][0])
else: print(items[0][0])


print(numbers[-1] - numbers[0])