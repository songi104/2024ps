import sys

input = sys.stdin.readline

seconds = 0
for _ in range(4):
    seconds += int(input())
x = seconds // 60
y = seconds % 60

print(x, y, sep='\n')
