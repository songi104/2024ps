import sys

N, K = map(int, sys.stdin.readline().split())

result = 0
while True:
    if N % K == 0:
        N /= K
        result += 1
    else:
        garbage = int(N % K)
        N -= garbage
        result += garbage
    if N == 0:
        result -= 1
        break
    if N == 1:
        break

print(result)
