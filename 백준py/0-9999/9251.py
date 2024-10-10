# 백준 9251번 LCS
"""
0/1 배낭처럼 접근했다.
가로로 문자열 두고
세로로 문자열 두고
포함하면 dp[j] = max(dp[:j]) + 1
아니면 그냥 위에꺼 그대로
"""

import sys
input = sys.stdin.readline
str1 = '0'+input().rstrip()
str2 = '0'+input().rstrip()


dp = [0]*(len(str2))

for s1 in str1[1:]:
    for j in range(len(str2)-1, 0, -1):
       # print(j)
        s2 = str2[j]
        if s1 == s2:
            dp[j] = max(dp[:j]) + 1


print(max(dp))
