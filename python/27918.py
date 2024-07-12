# 탁구 경기

import sys

N = int(input())
lst = [(sys.stdin.readline().rstrip()) for _ in range(N)]
D = 0
P = 0

#print(lst)

for i in range(N):
    winner = lst[i]
    if winner == "D": D += 1
    elif winner == "P": P += 1

    if abs(D-P) == 2: break

print(f'{D}:{P}')