# 백준 11054번 가장 긴 바이토닉 수열
N = int(input())
lst = list(map(int, input().split()))

left = [0]*N
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if lst[j] < lst[i]:
            left[i] = max(left[i], left[j] + 1)

right = [0]*N
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if lst[i] > lst[j]:
            right[i] = max(right[i], right[j]+1)

res = 0 
for i in range(N):
    res = max(res, left[i]+right[i]+1)
print(res)
