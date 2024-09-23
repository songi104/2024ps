
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
lst = []

for _ in range(N):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x: (x[1], x[0]))
# print(lst)
result = []
prev_e = 0
for pair in lst:
    s, e = pair
    if prev_e <= s:
        result.append((s, e))
        prev_e = e

print(len(result))
