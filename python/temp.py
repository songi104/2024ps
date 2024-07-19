import sys

T = int(input())

for _ in range(T):
    N, C = map(int, sys.stdin.readline().split())
    result = int(N/C)
    if (N % C != 0):
        result += 1
    print(result)
