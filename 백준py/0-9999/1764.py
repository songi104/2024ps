import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
a = set()
for _ in range(N):
    a.add(input().strip())

b = set()
for _ in range(M):
    b.add(input().strip())

res = list(a.intersection(b))
res.sort()
print(len(res))
for name in res:
    print(name)
