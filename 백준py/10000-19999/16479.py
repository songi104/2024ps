import sys

K = int(sys.stdin.readline())
D1, D2 = list(map(int, sys.stdin.readline().split()))
result = K**2 - ((D1-D2)/2)**2
print(result)