# 백준 30802번 웰컴키트

import sys
import math

N = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

result = 0
for s in sizes:
    result += math.ceil(s/T)

print(result)
print(N//P, N%P) 