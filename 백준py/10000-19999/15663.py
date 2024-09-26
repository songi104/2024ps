import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
d = {}
for n in numbers:
    if n in d.keys():
        d[n] += 1
    else:
        d[n] = 1


def dfs(num, tlst, td):
    td = dict.copy(td)
    if num == M:
        print(*tlst)
        return

    for n in td.keys():
        if td[n] >= 1:
            td[n] -= 1
            dfs(num+1, tlst+[n], td)
            td[n] += 1


dfs(0, [], d)
