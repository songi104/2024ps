import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
stress = 0

for e in arr:
    stress += e
    if e < 0:
        stress = 0
    if stress >= M:
        result += 1

print(result)
