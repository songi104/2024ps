# 백준 5430번 AC
# R은 배열을 뒤집는다
# D는 첫번째 글자 버림

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
#print(input().rstrip().replace('[','').replace(']','').split(','))
for _ in range(T):
    p = input().rstrip()
    N = int(input())
    if N == 0:
        lst = input()
        print('error')
        continue
    lst = deque(list(map(int, input().rstrip().replace('[', '').replace(']','').split(','))))

    error = False
    rev = False
    for action in p:
        if len(lst) == 0:
            error = True
            break

        if action == 'R': # reverse에서 오래 걸릴 수 있음.
            rev = not rev

        elif action == 'D':
            if rev:
                lst.pop()
            else:   
                lst.popleft()

    if error:
        print('error')
    else:
        if rev:
            lst.reverse()
        print('[', end='')
        for i in range(len(lst)-1):
            print(lst[i], end=',')
            
        if len(lst) != 0:
            print(lst[-1], end=']\n')
        else: print(']')

