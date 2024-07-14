# 왕실의 나이트
import sys

# 1. 그냥 구현
current_position = sys.stdin.readline()
column = (current_position[0])  # a
row = int(current_position[1])  # 1

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

# 2. 생각
result = 0
current_position = sys.stdin.readline()
column = (current_position[0])  # a
row = int(current_position[1])  # 1


steps = [(2, 1), (2, -1), (-2, 1), (-2, 1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

column = int(ord(column))-ord('a')+1
# print(column)

for step in steps:
    nx, ny = column+step[0], row+step[1]
    if nx < 1 or nx > 8:
        continue
    if ny < 1 or ny > 8:
        continue
    result += 1

print(result)
