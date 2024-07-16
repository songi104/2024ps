# 백준 10828 스택
"""
입력:
N
N개의 줄

출력:
push X: 정수X를 스택에 넣자
pop: 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력. 만약 스택에 들어잇는 정수가 없으면 -1
size: 스택에 들어있는 정수의 개수를 출력
empty: 스택 비었으면 1, 아니면 0
top: 스택 가장 위에 있는 정수를 출력하기만 함. 만약 정수 없으면 -1


궁금한 점
try-catch를 이용해서 push의 경우를 구현할 수 있을까?
{} 를 이용해서 function을 부를 수 있나?
다른 사람들은 어떻게 짰을까?

"""

import sys
input = sys.stdin.readline

N = int(input())




stack = []


for _ in range(N):
    lst = input().split()
    command = lst[0]
    if command == 'push': stack.append(lst[1])
    elif command == 'pop':
        if len(stack): print(stack.pop())
        else: print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0 :print(1)
        else: print(0)
    elif command == 'top':
        if len(stack) == 0 : print(-1)
        else: print(stack[-1])
    else: print(command)


