# 백준 1931번
"""
회의실이 있다. N개의 회의가 있다.
시작시간, 끝나는 시간이 있을 때 겹치지않게 하면서 
회의실을 사용할 수 있는 회의 최대 개수
회의의 수 N
N줄에 시작시간, 끝나는시간

1. 아이디어...
그냥 겹치면 더작은 녀석을 넣고
안 겹치면 그냥 냅둔다
모든 곳에 일단 0으로 하고 만약
예약이면 예약되는 칸 수를 기재한다
같을 수 있으므로 start:end-1로 생각하자 즉 그냥 lst[s:e]

2. 공간복잡도 계산
int * 2**31
"""


# input = sys.stdin.readline

# N = int(input())

# # lst = [0]*(2**31)
# lst = []


# cnt = 0
# for i in range(N):
#     start, end = map(int, input().split())
#     du = end - start
#     if sum_result != 0:
#         continue
#         # 비교하고 결정하는 로직
#     else:
#         lst[start:end] = [du]
#         cnt += 1


"""
방법2.
lst에 튜플을 저장하자.


"""


import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
lst = []


cnt = 0
for i in range(N):
    s, e = map(int, input().split())
    print('---', s, e, '---')
    MAX = max(e, len(lst))
    new_lst = [0]*MAX

    # new_lst 만들기
    for pair in lst:
        if pair != 0:
            print(pair)
            a, b = pair
            new_lst[a:b] = (a, b)

    # 중복 점검하기
    influ = 0
    target = []
    flag = True
    redundunt = any(type(pair) == tuple for pair in new_lst[s:e])
    if redundunt != 0:
        for t in range(s, e):
            if new_lst[t] != 0:
                a, b = new_lst[t]
                if e-s < b-a:
                    influ += 1  # 영향 주는 개수
                    target.append((a, b))
                    break
                else:
                    flag = False

    # 새롭게 할당
    lst = new_lst

    if flag and influ == 0:  # 안 겹침
        # print(f'{s} {e} 추가합니다')
        lst.append((s, e))
    elif influ == 1:
        # print(f'{target[0]} 지웁니다')
        # print(f'{s} {e} 추가합니다')
        idx = lst.index(target[0])
        lst[idx] = (s, e)

print(len(lst))
