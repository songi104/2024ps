import sys

input = sys.stdin.readline
N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
# print(lines)
lines.sort(key=lambda x: x[1])

lines.sort(key=lambda x: x[0])
for x, y in lines:
    print(x, y)
