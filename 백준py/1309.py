# 백준 1309번 동물원
"""
가로 2칸 세로 N칸인 우리가 있다.
사자 없는 경우도 1개의 경우의 수로 친다.


입력
N (세로) <= 100000
출력
사자배치 경우의 수 % 9901



"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
dp = [[0]*2 for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + 2*dp[i-1][1]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % 9901

# print(N, dp)
res = dp[N-1][0] + 2*dp[N-1][1]
print(res % 9901)
