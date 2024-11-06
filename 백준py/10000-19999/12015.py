N = int(input())
lst = list(map(int, input().split()))
dp = [0]*(N+1)
dp[1] = 1
for i in range(2, N+1):
    # update..
    # dp[1:i-1]을 순회하면서 lst[i]>lst[j] 그리고 
    dp[i]=
    