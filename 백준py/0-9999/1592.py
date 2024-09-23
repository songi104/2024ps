import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
catch = [0]*N


now = 0
catch[now] = 1
while True:
    if catch[now] % 2 == 0:
        next = now - L
        if next < 0:
            next += N
    else:
        next = now + L
        if next >= N:
            next %= N

    catch[next] += 1
    # print(next)
    if catch[next] == M:
        break
    now = next

# print(catch)
print(sum(catch)-1)
