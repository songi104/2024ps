import sys

input = sys.stdin.readline
H, M = map(int, input().split())

# 1. 리스트 풀이
# mininutes = [i for i in range(61)]
# hours = [i for i in range(24)]
# M = M - 45
# if M < 0:
#     M -= 1
#     H -= 1
# print(hours[H], mininutes[M])


# 2. 그냥 조건문
M -= 45
if M < 0:
    M += 60
    H -= 1
    if H < 0:
        H += 24
print(H, M)
