import sys

input = sys.stdin.readline
N = int(input())

dp = [0]*(501)
dp[0] = 1
dp[1] = 1


def facto(x):
    if dp[x] != 0:
        return dp[x]
    dp[x] = x*facto(x-1)
    return dp[x]


number = str(facto(N))
# print(number)
res = 0
for i in range(len(number)-1, -1, -1):
    n = number[i]
    if n == '0':
        res += 1
    else:
        break
print(res)
