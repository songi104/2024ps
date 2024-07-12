import sys

N = int(sys.stdin.readline())

for _ in range(N):
    M = int(sys.stdin.readline())
    m_lst = []
    result = 0
    for m in range(M):
        mission = list(map(int, sys.stdin.readline().split()))
        mission[1] *= -1 #death
        m_lst.append(mission)
        #print(m_lst)
    kda = list(map(int, sys.stdin.readline().split()))
    for m in range(M):
        money = sum(kda[i]*m_lst[m][i] for i in range(3))
        #print(money)
        if money >0: result += money
    print(result)