# 백준 11000번 강의실 배정
"""
1. 문제분석
각 수업마다 Si, Ti 가 주어진다.
최소한의 강의실을 사용해라!

2. 아이디어
끝나는 시간으로 정렬하면 뭔가 보이지않을까?
한 강의실에 최대를 때려넣고
다음 강의실에 최대를 때려넣으면 어떨까?
- 입력 받기
- 정렬
- 한 강의실에 때려넣기
    - 못 들어가는 녀석은 다음 lst에 넘기기
- 다음 강의실에 때려넣기
- 계속...

2-1. 아이디어
너무 느리다!
시작시간 기준으로 정렬하되 (근데 왜? 끝나는 시간이랑 뭔 차이?)
끝나는 시간만 담은 리스트를 만들어보자

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    lst.append(tuple(map(int, input().split())))

# 정렬
lst.sort()
# print(lst)

# 돌면서 강의실에 때려넣기
end_times = [lst[0][1]]
for pair in lst[1:]:
    s, e = pair
    flag = False
    for i in range(len(end_times)):
        prev_e = end_times[i]
        if prev_e <= s:
            end_times[i] = e
            flag = True
            break
    if not flag:
        end_times.append(e)

print(len(end_times))
