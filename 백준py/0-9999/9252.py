# 백준 9252번 LCS 2
"""
두번째 문자열 for i (dp 세로)
첫번째 문자열 for j (dp 가로)
저장할 때 숫자랑 문자열 같이
"""

str1 = '0' + input()
str2 = '0' + input()


dp = [['']*len(str1) for _ in range(len(str2))]

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str2[i] == str1[j] and len(dp[i-1][j]) < min(i,j):
            dp[i][j] = dp[i-1][j-1] + str1[j]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

res = dp[-1][-1]
if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(res)
