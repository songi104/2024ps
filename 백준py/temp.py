import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    house = N // H + 1
    if floor == 0:
        floor = H
        house -= 1  # 이 경우에는 호수 계산에서 1을 빼야 함
    if house < 10:
        house = '0' + str(house)
    else:
        house = str(house)
    print(str(floor) + house)
