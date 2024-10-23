# 백준 포도주 시식

N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))
#print(lst)

# dp 생성
dp = [0]*(N+1)
dp[1] = lst[1]

if N > 1:
    dp[2] = lst[1] + lst[2]

if N < 3:
    print(dp[N])
    exit()

for i in range(3, N+1):
    tlst = []
    dp[i] = max(dp[i-1], dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])

print(max(dp))