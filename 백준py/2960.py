# 백준 2960번 에라토스테네스의 체

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

numbers = ([ n for n in range(2,N+1) ])
cnt = 0

while True:
    if cnt == K: break

    P = numbers[0]
    new_numbers = []
    for number in numbers:
        if number % P == 0:
            cnt += 1
            if cnt == K:
                print(number)
                break
        else : new_numbers.append(number)
    numbers = new_numbers


