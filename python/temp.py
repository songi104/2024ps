import sys

input = sys.stdin.readline

numbers = []
for _ in range(9):
    numbers.append(int(input()))

result = max(numbers)
print(result)
print(numbers.index(result)+1)
