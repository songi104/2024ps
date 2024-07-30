import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())
N = int(input())
result = 0
for _ in range(N):
    value = 0
    for i in range(3):
        a, b, c = map(int, input().split())
        value += a*A + b*B + c*C
    result = max(value, result)
print(result)
