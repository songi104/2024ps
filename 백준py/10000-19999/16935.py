# 백준 16935번 A -> B
"""
최단경로 문제는 bfs가 더 적합하다. (시간 면에서.)
메모리 초과 시 list 대신 딕셔너리 쓰기 (메모리초과)

"""

from collections import deque
start, target = map(int, input().split())


# def solve(num):
#     stack = [num]
#     dp = [-1]*(target+1)
#     dp[start] = 1

#     while stack:
#         now = stack.pop()

#         # 2 곱하기
#         mul2 = now * 2
#         if mul2 <= target:
#             # 기존 값보다 새로운 경로가 더 짧을 때만 업데이트
#             if dp[mul2] == -1 or dp[mul2] > dp[now] + 1:
#                 dp[mul2] = dp[now] + 1
#                 stack.append(mul2)

#         # 1 추가하기
#         add1 = int(str(now) + '1')
#         if add1 <= target:
#             if dp[add1] == -1 or dp[add1] > dp[now] + 1:
#                 dp[add1] = dp[now] + 1
#                 stack.append(add1)
#     return dp[target]


def solve(start):
    q = deque([start])
    dp = {start: 1}

    while q:
        now = q.popleft()

        # 2를 곱한다
        temp = now*2
        if temp <= target and temp not in dp:
            dp[temp] = dp[now]+1
            q.append(temp)

        # 1을 더한다
        temp = int(str(now)+'1')
        if temp <= target and temp not in dp:
            dp[temp] = dp[now]+1
            q.append(temp)

    return dp.get(target, -1)


print(solve(start))
