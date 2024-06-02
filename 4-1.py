import sys


# # my solution
# N = int(sys.stdin.readline())
# walks = list(sys.stdin.readline().split())
# print(walks)
# result = [1, 1]


# for walk in walks:
#     if (walk == 'U'):
#         result[0] -= 1
#         if result[0] == 0:
#             result[0] = 1
#     elif (walk == 'D'):
#         result[0] += 1
#         if result[0] == N+1:
#             result[0] = N
#     elif (walk == 'R'):
#         result[1] += 1
#         if result[1] == N+1:
#             result[1] = N
#     elif (walk == 'L'):
#         result[1] -= 1
#         if result[1] == 0:
#             result[1] = 1

# print(result[0], result[1])


# 모범 답안
N = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())
x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

            # 공간 이탈
            if nx < 1 or ny < 1 or nx > N or ny > N:
                continue

            # 이동 수행
            x = nx
            y = ny

print(x, y)
