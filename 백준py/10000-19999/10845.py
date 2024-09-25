from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
q = deque([])
for _ in range(N):
    line = list(input().split())
    com = line[0]
    if len(line) == 2:
        n = int(line[1])

    if com == 'push':
        q.append(n)
    elif com == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif com == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
