import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def dfs(num, tlst):
    global numbers
    if num == M:
        print(*tlst)
        return

    for n in numbers:
        if n not in tlst:
            dfs(num+1, tlst+[n])


dfs(0, [])
