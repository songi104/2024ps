import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
chickens = []
homes = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append([i, j])

# print(graph)
# print(chickens)
# print(homes)


def cal(tlst):
    """
    모든 집에 대해서
    모든 치킨집을 돌면서
    제일 작은 거리를 다 합한 걸 return해야한다
    """

    res = 0

    for house in homes:
        # print(house)
        tmp = 2*N
        for store in tlst:
            tmp = min(tmp, abs(house[0]-store[0]) + abs(house[1]-store[1]))
        res += tmp
        # print(tmp)
    return res


def dfs(n, tlst):
    global ans
    # 종료조건
    # print(n, tlst)
    if n == len(chickens) or len(tlst) == M:
        distances.append(cal(tlst))
        return

    # 유지
    dfs(n+1, tlst+[chickens[n]])

    # 폐업
    dfs(n+1, tlst)


distances = []
dfs(0, [])
print(min(distances))
