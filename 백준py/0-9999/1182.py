# 부분수열의 합
# 몇개 골라서 더해서 S가 되어야합니다.
"""
for n in lst:
    n을 더하거나..말거나 해봅시다

dfs(i, t_sum)
if t_sum == S:
    return 1
if i == N:
    return 0

    res += dfs(i+1, t_sum+lst[i])
    res += dfs(i+1, t_sum)

-> dp로도 풀수잇을ㄷ스
"""

N, S = map(int, input().split())
lst = list(map(int, input().split()))

def dfs(i, t_sum, n):
    global N, S, lst, res


    if i == N:
        if t_sum == S and n != 0:
            res += 1
        return
    
    #print(lst[i], "생각해보자")
    dfs(i+1, t_sum+lst[i], n+1)
    dfs(i+1, t_sum, n)


res = 0
dfs(0, 0, 0)
print(res)