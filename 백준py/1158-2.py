import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [n for n in range(1, N+1)]
target = K - 1
result = []

while True:
    if target < len(numbers):
        result.append(numbers.pop(target))
        target += K - 1

    if len(numbers) == 0: break
    elif target >= len(numbers):
        target = target % len(numbers)    

print(str(result).replace('[', '<').replace(']', '>'))