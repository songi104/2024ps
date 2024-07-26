# 백준 1916번 최소비용 구하기
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {}
cost_map = {}
for _ in range(M):
    start, end, cost = map(int, input().split())
    if start in graph.keys():
        graph[start].append(end)
        cost_map[start].append(cost)
    else:
        graph[start] = [end]
        cost_map[start] = [cost]

# print(graph)
# print(cost_map)

start, target = map(int, input().split())

# 2. bfs를 돌 때마다 result list에 비용을 기록한다. 대신 더 작은 비용 기록


def bfs(start):
    queue = deque([])
    queue.append(start)

    # print(queue)
    result_list = [False]*(N+1)

    while queue:
        now = queue.popleft()
        if now in graph.keys():
            around = graph[now]
            # print(f'현재:{now} 주변:{around}')
        else:
            continue
        for i in range(len(around)):
            # print(next)
            next = around[i]
            plus = cost_map[now][i]
            queue.append(next)
            if not result_list[next]:
                result_list[next] = result_list[now] + plus
            else:
                result_list[next] = min(
                    result_list[next], result_list[now]+plus)

    return result_list


result_list = bfs(start)
print(result_list[target])
