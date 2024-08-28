import sys

input = sys.stdin.readline
N = int(input())
d = {}
s = set()
for _ in range(N):
    num = int(input())
    if num in s:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 2
    else:
        s.add(num)

for n in s:
    if n in d.keys():
        for _ in range(d[n]):
            print(n)
    else:
        print(n)
