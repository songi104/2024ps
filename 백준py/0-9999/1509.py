# 백준 1509번 팰린드롬 분할
"""
N = len(str1)
으로 하고 NxN dp에 대해서
i 번째 수를 기준으로 팰린드롬했을 때 몇 개까지 나오는지..

"""


string = input()
N = len(string)

dp = [[0]*N for _ in range(N)]
res = []
for i in range(N):
    # i 번째 수 기준으로 양 옆을 봅니다
    now = i
    cnt = 1
    dp[i][now] = cnt
    nr, nl = now, now
    while True:
        nr, nl = nr + 1, nl - 1
        #print(nr, nl)
        if nr >= N or nl < 0:
            break
        if string[nr] == string[nl]:
            dp[i][nr] = cnt
            dp[i][nl] = cnt
    cnt += 1
    for j in range(N):
        if dp[i][j] == 0:
            dp[i][j] = cnt
            cnt += 1
    res.append(max(dp[i]))
    print(dp[i])

print(min(res))


