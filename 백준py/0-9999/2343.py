# 백준 2343번 기타레슨
"""
입력
N M
1줄에 N개 각각의 강의 길이

N개의 강의를 M개의 블루레이에 넣는다.
이 때 블루레이를 최소로 만든다. (약간 그리디 깔..! 예산문제같기도 하다)
시작은 M*제일 큰 강의로 하면 될 것 같다.
"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# print(numbers)

start = max(numbers)
end = sum(numbers)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    part = 0
    for n in numbers:
        # cnt가 M을 넘으면 불가능하기에 start를 오른쪽으로
        # cnt가 M을 안 넘으면 너무 큰 블루레이일 수 잇으니 end를 왼쪽으로 (ans 해주기)
        if part + n > mid:
            part = n
            cnt += 1
        else:
            part += n
        # print(f'{mid}: {part} {cnt}')
    if cnt > M:
        start = mid + 1
    else:
        # print('ans:', mid)
        ans = mid
        end = mid - 1
print(ans)
