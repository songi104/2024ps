# 왕실의 나이트
import sys

current_position = sys.stdin.readline()
column = (current_position[0])  # a
row = int(current_position[1])  # 1

# 1. 그냥 구현
result = 0
matching = 'abcdefgh'
column = int(matching.find(column))+1  # a-h=>1-8
# print(column)

if column < 7:
    if row >= 2 and row <= 7:
        result += 2
    else:
        result += 1

if column > 2:
    if row >= 2 and row <= 7:
        result += 2
    else:
        result += 1

if row < 7:
    if column >= 2 and column <= 7:
        result += 2
    else:
        result += 1

if row > 2:
    if column >= 2 and column <= 7:
        result += 2
    else:
        result += 1

print(result)
